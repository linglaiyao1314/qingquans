# coding=utf-8
from flask import Flask

from helpers import template_filters


def create_app_by_config(config="config.BaseConfig", logger=False):
    app = Flask(__name__)
    app.config.from_object(config)
    # 测试环境下就不打印日志了
    app.logger.level = 1000

    from qsapp.views.qsmain_view import qsmain
    app.register_blueprint(qsmain)


    # @app.errorhandler(404)
    # def page_not_found(e):
    #     return render_template("Public/404.html"), 404
    #
    # @app.errorhandler(500)
    # def internal_server_error(e):
    #     return render_template('Public/500.html'), 500

    # 增加过滤器
    for value in template_filters.__dict__.values():
        if callable(value):
            app.add_template_filter(value)

    return app




