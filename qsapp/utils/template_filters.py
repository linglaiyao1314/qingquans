# coding=utf-8
"""
该模块包含模版渲染过程中的所有过滤器
"""
import time
from datetime import datetime


def date2timestamp(s):
    # date = "yyyy-mm-dd"
    return int(time.mktime(datetime.strptime(s, "%Y-%m-%d").timetuple()))


def timestamp2date(s, format_str="%Y-%m-%d %H:%M:%S"):
    # default date = "yyyy-mm-dd"
    return datetime.fromtimestamp(int(s)).strftime(format_str)