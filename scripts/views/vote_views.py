from flask import Blueprint, redirect, jsonify,render_template, url_for, request,send_file,Response
from flask_cors import CORS, cross_origin
from scripts import Voters,CANDIDATES,RESULTS_PATH
from scripts.funcs import save_response, split_list
from scripts.objects import Voter
views = Blueprint("vote_views", __name__)
CORS(views)
Voters = Voters
POSTS = list(CANDIDATES.keys())

@views.route("/voterinfo")
def getvoterinfo():
    return render_template("voterinfo.html")


@views.route("/start_voting")
def start_voting():
    return redirect(url_for("vote_views.vote"))

@views.route('/vote')
def vote():
    posts =list(CANDIDATES.keys())
    data = list(split_list(posts,3))
    return render_template('vote.html',posts=POSTS,data=data,candidates=CANDIDATES)

@views.route("/vote_for/<post>")
def vote_for(post):
    try:
        names = CANDIDATES[post]
    except KeyError:
        return "<h1>This post does not exist!</h1>"
    return render_template("vote_post.html",post=post,names=names)

@views.route('/nextroute/<current_post>')
def next_route(current_post):
    if current_post in POSTS:
       curr_index = POSTS.index(current_post)
       return jsonify(POSTS[curr_index+1])

@views.route("/completed")
def show_complete():
    return render_template("completed.html")

# POST_METHODS
@views.route("/post/voterinfo", methods=["POST"])
def start_vote():
    if request.method == "POST":
        name = request.form["name"]
        # Mismatch between grade and class as class is reserved keyword in Python
        grade = request.form["class"]
        section = request.form["section"]
        admin_number = request.form['admin_number']
        Voters.append(Voter(name,grade,section))
    return redirect(url_for("vote_views.vote"))

@views.route("/post/submitvote",methods=["POST"])
def sumbit_vote():
    data=dict(request.json)
    response = dict()
    for post in list(CANDIDATES.keys()):
        if post in data:
            response[post] = data[post]
            save_response(response=response,posts=list(CANDIDATES.keys()),path=RESULTS_PATH / "results.json")
        else:
            response[post]=''
    return redirect(url_for('vote_views.show_complete'))
    # except Exception as e:
    #     return Response(response="Failed!",status=400,mimetype="text/plain")