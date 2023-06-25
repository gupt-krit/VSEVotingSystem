from flask import Blueprint, redirect, render_template, url_for, request

views = Blueprint("vote_views", __name__)


@views.route("/voterinfo")
def getvoterinfo():
    return render_template("voterinfo.html")


@views.route("/start_voting")
def start_voting():
    return redirect(url_for("vote_views.headboy"))


@views.route("/headboy")
def headboy():
    return render_template("base.html")


# POST_METHODS
@views.route("/post/voterinfo", methods=["POST"])
def start_vote():
    if request.method == "POST":
        voter = dict()
        # Do something with this!
        voter["name"] = request.form["name"]
        voter["class"] = request.form["class"]
        voter["section"] = request.form["section"]
    return redirect(url_for("vote_views.start_voting"))
