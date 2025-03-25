import flask

app = flask.Flask("correctcontact")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_contacts():
    contactdb = open("contactsdb.txt")
    content = contactdb.read()
    contactdb.close()
    contacts = content.split("\n")
    contacts.sort()
    return contacts

@app.route("/")
def homepage():
    return get_html("index")

@app.route("/guests")
def guests():
    html_page = get_html("guests")
    contacts = get_contacts()
    db_values = "<ul>"
    for contact in contacts:
        db_values += "<li>" + contact + "</li>"
    db_values += "</ul>"
    db_values += "<br>"
    db_values += "<a href=\"/\">Back to Start Page</a>"
    return html_page.replace("$$CONTACTS$$", db_values)

@app.route("/result")
def result():
    html_page = get_html("result")
    search = flask.request.args.get("search")
    contacts = get_contacts()
    res_arr = [k for k in contacts if search.lower() in k.lower()]
    if not res_arr:
        res_arr = ["No Contact Found"]
    contact_values = "<ul>"
    for contact in res_arr:
        contact_values += "<li>" + contact.title() + "</li>"
    contact_values += "</ul>"
    contact_values += "<br>"
    contact_values += "<a href=\"/\">Back to Start Page</a>"
    return html_page.replace("$$CONTACTS_RESULT$$", contact_values)
