from flask import Flask, render_template, redirect, url_for, request
from .views import vote_views,image_views
from .funcs import load_json
#from .config import DataStore


def create_app():
    app = Flask("votingsystemserver")
    app.register_blueprint(vote_views.views, url_prefix="/vote/")
    app.register_blueprint(image_views.img_views,url_prefix="/image/")
    @app.route("/")
    def index():
        return redirect(url_for("vote_views.getvoterinfo"))

    return app
