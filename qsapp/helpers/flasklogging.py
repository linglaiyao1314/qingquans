# coding=utf-8
import logging
import os
import datetime
import platform

LOGPREFIX = "ds_"
system_type = platform.system().lower()
if system_type.find("windows") >= 0:
    LOGNAME = "%s%s.log" % (LOGPREFIX, str(datetime.datetime.now().strftime('%Y.%m.%d')))
else:
    if not os.path.exists("/var/log/DS/"):
        os.mkdir("/var/log/DS/")
    LOGNAME = "/var/log/DS/%s%s.log" % (LOGPREFIX, str(datetime.datetime.now().strftime('%Y.%m.%d')))


INFO = logging.INFO
WARN = logging.warn
DEBUG = logging.DEBUG
ERROR = logging.ERROR

COLOR = {
    INFO: '\033[92m',  # 绿
    ERROR: '\033[91m',  # 红
    WARN: '\033[93m',
    DEBUG: '\033[43m',  # 黄
    "end": "\33[0m"
}

formatter = logging.Formatter('%(asctime)s-[%(filename)s line:%(lineno)03d]-%(levelname)-7s: %(message)s')


def create_file_handler():
    file_handler = logging.FileHandler(LOGNAME)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    return file_handler


def create_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    return stream_handler


# 打印上色
def wrapstring(string, level=INFO):
    return COLOR[level] + string + COLOR["end"]

