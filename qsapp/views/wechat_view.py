from flask import Blueprint, request, render_template


wechat = Blueprint("wechat", __name__)


@wechat.route("/wechat", methods=["GET", "POST"])
def index():
	return "success"
