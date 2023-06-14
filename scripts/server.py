from flask import Flask, render_template, redirect, url_for, request
from .views import views


def create_app():
    app = Flask("votingsystemserver")
    app.register_blueprint(views)
    return app
