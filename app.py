from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skills/")
def skills():
    return render_template("skills.html")

@app.route("/resume/")
def resume():
    return render_template("resume.html")

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(directory='static/documents', path=filename)

@app.route("/transcripts/")
def transcripts():
    return render_template("transcripts.html")

@app.route("/military/")
def military():
    return render_template("military.html")

@app.route("/links/")
def links():
    return render_template("links.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == "__main__": # If this app is not being called as part of a module, then:
    app.run(debug=True)