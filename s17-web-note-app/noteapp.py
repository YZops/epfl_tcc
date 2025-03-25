import flask

app = flask.Flask("noteapp")

# Prepare and get HTML pages
def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

# Open and prepare DB-file
def prepare_dbfile_notes():
    file = open("notedb.txt")
    content_from_db = file.read()
    file.close()
    return content_from_db.split("\n")

# Create a note
def add_note(text):
    # Open and prepare DB-file
    file = open("notedb.txt", "a")
    file.write(text + "\n")
    file.close()
    # Note is successfully added to the file
    note_status = "<p class=\"success\">Note was successfully added</p><p>Add another note if you like.</p>"
    return note_status

# Get all notes from DB-file
def get_notes():
    # Get the notes from file
    notes = prepare_dbfile_notes()
    # Initialize variables
    result = ""
    counter = 0
    note_amount = "notes"
    # Check the notes from the file-DB
    for note in notes:
        result += "<p>" + note + "</p>"
        counter += 1
    # Because of new line in file-DB, we need to substract -1 from counter to get the real amount of notes
    if (counter == 2):
        note_amount = "note"
    
    result += "<p class=\"result\">" + str(counter - 1) + " " + note_amount + " found</p>"
    return result

# Search through notes
def searchs_note(text):
    # Get the notes from file
    notes = prepare_dbfile_notes()
    # Initialize variables
    result = ""
    counter = 0
    note_amount = "notes"
    # Check the notes from the file-DB
    for note in notes:
        if note.lower().find(text.lower()) != -1:
            result += "<p>" + note + "</p>"
            counter += 1
    # If 1 note, so write it in singular
    if (counter == 1):
        note_amount = "note"
    # If search result no empty
    if result != "":
        result += "<p class=\"result\">" + str(counter) + " " + note_amount + " found</p>"
    else:
        result = "<p class=\"error\">No notes found</p>"
    return result

@app.route("/")
def homepage():
    return get_html("index")

@app.route("/add_note")
def add_notes():
    html_page = get_html("note_add")
    # Get Argument from URL
    note_add_text = flask.request.args.get("q")
    # Check if argument exists and make additionals checks
    if note_add_text is None:
        note_status = "<p>Enter a note</p>"
    elif (note_add_text == ""):
        note_status = "<p class=\"error\">An empty note text cannot be added</p>"
    elif (note_add_text.count("") < 4):
        note_status = "<p class=\"error\">Please enter at least 3 characters</p>"
    else:
        # Call function to add the note
        note_status = add_note(note_add_text)
    # Return Template-Variable with content to HTML-file
    return html_page.replace("$$ADDNOTESTATUS$$", note_status)

@app.route("/view_notes")
def view_notes():
    html_page = get_html("note_view")
    # Call function to get notes
    notes = get_notes()
    # Return Template-Variable with content to HTML-file
    return html_page.replace("$$SHOWNOTES$$", notes)

@app.route("/search_notes")
def search_notes():
    html_page = get_html("note_search")
    # Get Argument from URL
    search_string = flask.request.args.get("q")
    # Check if argument exists and make additionals checks
    if search_string is None:
        search_status = ""
    elif (search_string == ""):
        search_status = "<p class=\"error\">Please enter a search string</p>"
    elif (search_string.count("") < 4):
        search_status = "<p class=\"error\">Please enter at least 3 characters</p>"
    else:
        # Call function search for notes
        search_status = searchs_note(search_string)
    # Return Template-Variable with content to HTML-file
    return html_page.replace("$$NOTESEARCHRESULT$$", search_status)
