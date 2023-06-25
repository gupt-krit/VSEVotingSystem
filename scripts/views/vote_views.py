from flask import Blueprint, redirect, render_template, url_for, request

views = Blueprint("vote_views", __name__)


@views.route("/voterinfo")
def getvoterinfo():
    return render_template("voterinfo.html")


@views.route("/")
def index():
    return redirect(url_for("views.voterinfo"))


# POST_METHODS
@views.route("/posts/startvote", methods=["POST"])
def start_vote():
    if request.method == "POST":
        voter = dict()
        voter["name"] = request.form["VoterName"]
        voter["class"] = request.form["VoterClass"]
        voter["section"] = request.form["VoterSection"]
    return ""
