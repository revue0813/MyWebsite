from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume/")
def resume():
    return render_template("resume.html")

@app.route("/skills/")
def skills():
    return render_template("skills.html")

@app.route("/links/")
def links():
    return render_template("links.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == "__main__": # If this app is not being called as part of a module, then:
    app.run(debug=True)