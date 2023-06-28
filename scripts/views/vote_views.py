from flask import Blueprint, redirect, render_template, url_for, request,current_app
import requests
from scripts.config import DataStore
from scripts.funcs import load_imgs
from scripts.objects import Voter
views = Blueprint("vote_views", __name__)
Voters = DataStore.Voters
routes = DataStore.CANDIDATE_LIST.keys()
print(routes)
@views.route("/voterinfo")
def getvoterinfo():
    return render_template("voterinfo.html")


@views.route("/start_voting")
def start_voting():
    return redirect(url_for("vote_views.vote_for",post="headboy"))


@views.route("/vote_for/<post>")
def vote_for(post):
    print("This is the post: "+post)
    print(load_imgs(post))
    return render_template("vote.html",post=post,imgs=load_imgs(post))

# POST_METHODS
@views.route("/post/voterinfo", methods=["POST"])
def start_vote():
    if request.method == "POST":
        name = request.form["name"]
        # Mismatch between grade and class as class is reserved keyword in Python
        grade = request.form["class"]
        section = request.form["section"]
        Voters.append(Voter(name,grade,section))
    return redirect(url_for("vote_views.start_voting"))
