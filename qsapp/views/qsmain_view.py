from flask import Blueprint, request, render_template


qsmain = Blueprint("qsmain", __name__)


@qsmain.route("/", methods=["GET", "POST"])
@qsmain.route("/index", methods=["GET", "POST"])
def index():
	return render_template("index.html")
