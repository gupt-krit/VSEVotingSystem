from flask import Blueprint, redirect, jsonify,render_template, url_for, request,send_file
from flask_cors import CORS, cross_origin
import requests,os,pathlib
from scripts.config import DataStore
from scripts.funcs import load_imgs
from scripts.objects import Voter
views = Blueprint("vote_views", __name__)
CORS(views)
Voters = DataStore.Voters
routes = list(DataStore.CANDIDATES.keys())

@views.route("/voterinfo")
def getvoterinfo():
    return render_template("voterinfo.html")


@views.route("/start_voting")
def start_voting():
    return redirect(url_for("vote_views.vote_for",post="headboy"))

@views.route("/vote_for/<post>")
def vote_for(post):
    #print("This is the post: "+post)
    #print(load_imgs(post))
    try:
        names = DataStore.CANDIDATES[post]
    except KeyError:
        return "<h1>This post does not exist!</h1>"
    return render_template("vote.html",post=post,names=names)

@views.route('/nextroute/<current_post>')
def next_route(current_post):
    if current_post in routes:
       curr_index = routes.index(current_post)
       return jsonify(routes[curr_index+1])

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

@views.route("/post/submitvote",methods=["POST"])
def sumbit_vote(post):
    return ""