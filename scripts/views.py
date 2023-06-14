from flask import Blueprint, redirect, render_template, url_for, request

views = Blueprint("views", __name__)


@views.route("/start")
def start():
    return render_template("start_page.html")


@views.route("/")
def home():
    return ""  # redirect(url_for("/start"))


# POST_METHODS
@views.route("/posts/startvote", methods=["POST"])
def start_vote():
    if request.method == "POST":
        voter = dict()
        voter["name"] = request.form["VoterName"]
        voter["class"] = request.form["VoterClass"]
        voter["section"] = request.form["VoterSection"]
    return ""
