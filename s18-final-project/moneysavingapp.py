# Import required flask modules
from flask import Flask, render_template, request
# Import datetime to handle date format
from datetime import datetime, date
# Import regex
from re import match

# Name of App
app = Flask("moneysavingapp")

##
# Classes
##
class configStoreList:
    def __init__(self, store_name, store_type):
        # String prepared for DB
        self.store_name_type = store_name.lower() + "-" + store_type.lower()
        
    # Check if store already in list
    def add_store(self, db_name):
        # Read the stores from DB
        get_stores = read_db(db_name)
       
        # Check the items from the file-DB
        if self.store_name_type not in get_stores:
            # Add store to DB
            db_write_mode = "a"
            add_db(db_name, db_write_mode, self.store_name_type)
            
            return "Store successful added to DB"

        # Store already in DB
        return "Store not added to DB because already exist"
    
    # Check if store already in list
    def remove_store(self, db_name):
        # Read the stores from DB
        get_stores = read_db(db_name)
        
        # Check if store in DB
        if self.store_name_type in get_stores:
            # Remove store
            get_stores.remove(self.store_name_type)
            
            # Add stores to DB
            db_write_mode = "w"
            add_db(db_name, db_write_mode, get_stores)
            
            # Delete emtpy line from file
            get_stores = read_db(db_name)
            clean_db(db_name, get_stores)
            
            return "Store successful deleted from DB"
        
        # Store not in DB
        return "Store does not exist in DB"

##
# Functions
##
# Read DB: Open and prepare DB-file
def read_db(db_name):
    file = open(db_name)
    content_from_db = file.read()
    file.close()
    
    return content_from_db.split("\n")

# Create a new DB-entry
def add_db(db_name, db_write_mode, text):
    # Open and prepare DB-file
    file = open(db_name, db_write_mode)
    
    # If delete statement else is add statement
    if type(text) is list:
        for text_line in text:
            file.write(text_line + "\n")
    else:
        file.write(text + "\n")
    file.close()

# Delete emtpy lines from file
def clean_db(db_name, text):
    # Open and prepare DB-file
    file = open(db_name, "w")
    for text_line in text:
        # Check text_line is not empty or has just spaces
        if text_line.strip(): 
            file.write(text_line + "\n")
    file.close()

# Create values for HTML form elements for store like select list and radio button
def html_form_elem_stores(html_elem, get_stores):  
    # Declare variables and set initial value
    val_html_elem_store = ""
    counter_id = 1

    # Prepare stores for HTML elements
    for store in get_stores:
        # If empty string, just ignore
        if store != "":
            # Show clear name in elements
            store_clear_name = store.replace("-", " ").title()
            
            # Create HTML-form elements for stores
            if html_elem == "select":
                val_html_elem_store += "<option value=\"" + store + "\">" + store_clear_name + "</option>"
            elif html_elem == "radio": 
                val_html_elem_store += "<div> <input type=\"radio\" id=\"" + str(counter_id) + "\" name=\"store\" value=\"" + store + "\"> <label for=\"" + str(counter_id) + "\">" + store_clear_name + "</label> </div>"
            
            # Counter +1
            counter_id += 1

    # Return the HTML form element
    return val_html_elem_store

# Create values for HTML form elements for store like select list and radio button
def html_form_elem_savings(get_savings):  
    # Declare variables and set initial value
    val_html_elem_saving = ""
    counter_id = 1

    # Sort savings (date)
    get_savings.sort() 

    # Prepare savings
    for saving in get_savings:
        # If empty string, just ignore
        if saving != "":
            # Display the savings
            saving_display_names = saving_display(saving)
            # Split into date, store, amount
            saving_date_store_amount = saving_display_names.split("|")

           # Create HTML-form elements for savings
            val_html_elem_saving += "<div> <input type=\"radio\" id=\"" + str(counter_id) + "\" name=\"saving\" value=\"" + saving + "\"> <label for=\"" + str(counter_id) + "\">" + saving_date_store_amount[0] + " - " + saving_date_store_amount[1] + " - " + saving_date_store_amount[2] + "</label> </div>"

            # Counter +1
            counter_id += 1

    # Return the HTML form element
    return val_html_elem_saving

# Show display date
def date_display(db_date):
    # Date format YYYY-MM-DD to display format DD.MM.YYYY
    return datetime.strptime(db_date, "%Y-%m-%d").strftime("%d.%m.%Y")

def saving_display(db_saving):
    # Show clear name in elements
    saving_date_store_amount = db_saving.split("|")

    # Display date format DD.MM.YYYY
    val_sdate = date_display(saving_date_store_amount[0])
    # Display store with clean name
    val_sstore = saving_date_store_amount[1].replace("-", " ").title()
    # Display amount with CHF
    val_samount = "CHF " + saving_date_store_amount[2]

    return val_sdate + "|" + val_sstore + "|" + val_samount

##
# Routings
##
@app.route("/")
def home():
    # Declare variables and set initial value
    out_stores = ""

    # Get stores from DB
    db_name = "storesdb.txt"
    get_stores = read_db(db_name)

    for store in get_stores:
        if not store == "":
            out_stores += store

    if len(out_stores) == 0:
        out_stores = "zero"


    return render_template("index.html", display_stores = out_stores)

@app.route("/add_saving", methods=["GET", "POST"])
def add_saving():
    # Declare variables and set initial value
    error_msg = ""
    error_sdate = ""
    error_store = ""
    error_samount = ""
    
    # Save form values in variables
    val_sdate = request.args.get("sdate")
    val_store = request.args.get("store")
    val_samount = request.args.get("samount")

    # Get stores from DB
    db_name = "storesdb.txt"
    get_stores = read_db(db_name)

    # Get content for HTML element
    val_select_store = html_form_elem_stores("select", get_stores)
    
    # Get todays date as max date to enter for savings
    date_maxdate = str(date.today())

    # Check if form values filled out
    if val_sdate is not None and val_store is not None and val_samount is not None:
        # Check if correct date format
        # If date format is pattern with digits like yyyy-mm-dd and a valid year, month and day -> min date: 2000-01-01
        if not match(r'^(20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', val_sdate) or val_sdate > date_maxdate:
            error_sdate = "<p class=\"error\">-Invalid Date</p>"
            error_msg = "error"
        
        # Check if store in storesdb
        if val_store not in get_stores:
            error_store = "<p class=\"error\">-Invalid Store Name<p>"
            error_msg = "error"

        # Check if amount is valid -> Digit must be < 1000
        if val_samount == "" or not match(r'^[0-9]{0,3}(?:\.[0-9][05]{0,1})?$', val_samount) or float(val_samount) == 0:
            error_samount = "<p class=\"error\">- Invalid Amount<p>"
            error_msg = "error"
        
        # If all checks successful and no error -> save to DB and return message
        if error_msg == "":
            # Prepare and save to DB
            db_name = "moneysavingdb.txt"
            db_text = val_sdate + "|" + val_store + "|" + "%.2f"%float(val_samount)
            db_write_mode = "a"
            add_db(db_name, db_write_mode, db_text)

            # Display the savings
            saving_display_names = saving_display(db_text).replace("|", " - ")
            
            return render_template("add_saving.html", out_message = "<p class=\"success\">All fine. The entry has been added</p>", out_added_entry = "<p class=\"success\">" + saving_display_names + "</p>", max_date = date_maxdate, select_store = val_select_store)
        else:
            return render_template("add_saving.html", out_message = "<p class=\"error\">The entry has not been added</p>", out_sdate = error_sdate, out_store = error_store, out_samount = error_samount, max_date = date_maxdate, select_store = val_select_store)

    else:
        # Initial view or not all fields were filled out
        return render_template("add_saving.html", max_date = date_maxdate, select_store = val_select_store)

@app.route("/view_savings", methods=["GET", "POST"])
def view_savings():
    # Declare variables and set initial value
    val_date_store_amount = ""
    total_saving_amount = 0.0
    
    # Save form values in variables
    val_sdate_from = request.args.get("sdate_from")
    val_sdate_to = request.args.get("sdate_to")

    # If date format is pattern with digits like yyyy-mm-dd and a valid year, month and day
    if val_sdate_from is not None and match(r'^(20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', val_sdate_from):
        # Define date format YYYY-MM-DD to compare with other dates
        val_sdate_from = datetime.strptime(val_sdate_from, "%Y-%m-%d")
    if val_sdate_to is not None and match(r'^(20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', val_sdate_to):
        # Define date format YYYY-MM-DD to compare with other dates
        val_sdate_to = datetime.strptime(val_sdate_to, "%Y-%m-%d")

    # Get savings from DB
    db_name = "moneysavingdb.txt"
    get_savings = read_db(db_name)

    # Sort savings (date)
    get_savings.sort() 

    # Prepare savings
    for saving in get_savings:
        # If empty string, just ignore
        if saving != "":
            # Split DB format
            db_date_store_amount = saving.split("|")
            # Display the savings
            saving_display_names = saving_display(saving)
            # Split into date, store, amount
            saving_date_store_amount = saving_display_names.split("|")

            db_date = datetime.strptime(db_date_store_amount[0], "%Y-%m-%d")

            # If date format is pattern with digits like yyyy-mm-dd and a valid year, month and day
            if (val_sdate_from is not None and val_sdate_from is not None) and (type(val_sdate_from) != str and type(val_sdate_to) != str):
                # Check date from DB is in range of defined dates
                if val_sdate_from <= db_date <= val_sdate_to:
                    val_date_store_amount += "<p>" + saving_date_store_amount[0] + " - " + saving_date_store_amount[1] + " - " + saving_date_store_amount[2] + "</p>"
                    # Get total saving amount
                    total_saving_amount += float(db_date_store_amount[2])
            else:
                # Display savings
                val_date_store_amount += "<p>" + saving_date_store_amount[0] + " - " + saving_date_store_amount[1] + " - " + saving_date_store_amount[2] + "</p>"
                # Get total saving amount
                total_saving_amount += float(db_date_store_amount[2])
            
    
    # Display total savings with rounded 2 decimals as string
    total_saving_amount = "%.2f"%total_saving_amount
    
    return render_template("view_savings.html", out_date_store_amount = val_date_store_amount, out_total_save_amount = "<p><strong>Total Savings: CHF " + total_saving_amount + "</strong></p>")

@app.route("/remove_saving")
def remove_saving():
    # Declare variables and set initial value
    out_message_remove_saving = ""

    # Get savings from DB
    db_name = "moneysavingdb.txt"
    get_savings = read_db(db_name)

    # Get content for HTML element
    val_radio_saving = html_form_elem_savings(get_savings)

    # Check if values from arguments not empty
    if request.args:
        saving = request.args.getlist('saving')
        
        # Convert Flask ImmutableMultiDict to string
        saving = ''.join(saving)

        # Check if store in DB
        if saving in get_savings:
            # Remove store
            get_savings.remove(saving)
            
            # Add stores to DB
            db_write_mode = "w"
            add_db(db_name, db_write_mode, get_savings)
            
            # Delete emtpy line from file
            get_savings = read_db(db_name)
            clean_db(db_name, get_savings)
            
            out_message_remove_saving =  "Saving successful removed"
        else:
            # Store not in DB
            out_message_remove_saving = "Saving does not exist"

        return render_template("remove_saving_save.html", out_message = out_message_remove_saving)

    else:
        # Not all field were filled out correctly
        return render_template("remove_saving.html", radio_saving = val_radio_saving)    

    

@app.route("/configuration")
def configuration():
    # Get stores from DB
    db_name = "storesdb.txt"
    get_stores = read_db(db_name)

    # Get content for HTML element
    val_radio_store = html_form_elem_stores("radio", get_stores)

    return render_template("configuration.html", radio_store = val_radio_store)

@app.route("/config_addstore", methods=["GET", "POST"])
def config_addstore():
    # Save form values in variables
    val_store_name = request.args.get("storename")
    val_store_type = request.args.get("storetype")

    # Get stores from DB
    db_name = "storesdb.txt"
    get_stores = read_db(db_name)

    # Get content for HTML element
    val_radio_store = html_form_elem_stores("radio", get_stores)
    
    # Check if form values correct filled out
    if (val_store_name.count("-") == 0) and (val_store_name and val_store_type) and (val_store_type == "local" or val_store_type == "online"):
        # Create Objects with properties
        new_store = configStoreList(val_store_name, val_store_type)
        
        # Check if store name not already in list -> Call method to check DB
        check_store_in_list = new_store.add_store(db_name)
        
        return render_template("configuration_save.html", out_message = check_store_in_list)
    
    else:
        # Not all field were filled out correctly
        return render_template("configuration.html", out_message_add_store = "<p class=\"error\">Does store name contains \"-\" or is a field empty? Please try again<p>", radio_store = val_radio_store)
    
@app.route("/config_removestore")
def config_removestore():
    # Get stores from DB
    db_name = "storesdb.txt"
    get_stores = read_db(db_name)

    # Get content for HTML element
    val_radio_store = html_form_elem_stores("radio", get_stores)

    # Check if values from arguments not empty
    if request.args:
        store = request.args.getlist('store')
        
        # Convert Flask ImmutableMultiDict to string
        store = ''.join(store)
        
        # Check if string contains more than one "-"
        if not store.count("-") == 1:
            return render_template("configuration.html", out_message_remove_store = "<p class=\"error\">Store name not exists. Please try again<p>", radio_store = val_radio_store)

        # Split the store into "store_name" and "store_type"       
        store_name_type = store.split("-")
        
        # Create Objects with properties
        del_store = configStoreList(store_name_type[0], store_name_type[1])
        
        # Check if store is in list
        remove_store_in_list = del_store.remove_store(db_name)
        
        return render_template("configuration_save.html", out_message = remove_store_in_list)

    else:
        # Not all field were filled out correctly
        return render_template("configuration.html", radio_store = val_radio_store)        

# Error Routings - Page not found    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
