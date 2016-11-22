# coding=utf-8
from flask import Flask

from helpers import template_filters


def create_app_by_config(config=None, profile=False):
    app = Flask(__name__)
    # 初始化环境配置
    app.config.from_object("config.default")
    if config:
        try:
            app.config.from_object(config)
        except:
            raise ValueError("[%s] config is not exists" % config)

    from qsapp.views.qsmain_view import qsmain
    app.register_blueprint(qsmain)

    # 增加过滤器
    for value in template_filters.__dict__.values():
        if callable(value):
            app.add_template_filter(value)
    return app






