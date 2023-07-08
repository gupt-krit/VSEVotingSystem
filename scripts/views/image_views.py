from flask import Blueprint,send_file
from scripts import CWD
img_views = Blueprint("img_views",__name__)

@img_views.route('<post>/<name>')
def return_img(post,name):
    filename = CWD / "data" / "imgs" / f"{name.lower()}_{post.lower()}.jpg"
    if filename.exists():
        return send_file(filename,mimetype='image/jpg')
    else:
        return f"File not Found at - {filename}"