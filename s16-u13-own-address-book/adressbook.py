import flask

app = flask.Flask("adressbook")

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
