from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        image_url=url_for("static", filename="images/dark_header_image_home.jpg"),
    )

@app.route("/resume/")
def resume():
    return render_template(
        "resume.html",
        image_url=url_for("static", filename="images/dark_header_image_resume.jpg"),
    )


@app.route("/transcripts/")
def transcripts():
    return render_template(
        "transcripts.html",
        image_url=url_for(
            "static", filename="images/dark_header_image_transcripts.jpg"
        ),
    )


@app.route("/military/")
def military():
    return render_template(
        "military.html",
        image_url=url_for("static", filename="images/header_image_military.jpg"),
    )


@app.route("/skills/")
def skills():
    return render_template(
        "skills.html", 
        image_url=url_for("static", filename="images/header_image_skills.jpg"),
    )


@app.route("/portfolio/")
def portfolio():
    return render_template(
        "portfolio.html",
        image_url=url_for("static", filename="images/header_image_portfolio.jpg"),
    )


@app.route("/links/")
def links():
    return render_template(
        "links.html",
        image_url=url_for("static", filename="images/header_image_links.jpg"),
    )


@app.route("/contact/")
def contact():
    return render_template(
        "contact.html",
        image_url=url_for("static", filename="images/header_image_contact.jpg"),
    )


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(directory="static/documents", path=filename)


if __name__ == "__main__":  # If this app is not being called as part of a module, then:
    app.run(debug=True)
