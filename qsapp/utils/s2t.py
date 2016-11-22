# coding=utf-8
import requests
import os
import glob

MAXSIZE = 9216


class S2T(object):
    def __init__(self, post_url="http://opencc.byvoid.com/convert", config='s2twp.json'):
        self.url = post_url
        self.config = config
        self.session = requests.session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'})

    def simple_to_traditional(self, input_file):
        print "covert %s" % input_file
        name, file_type = os.path.splitext(input_file)
        if not file_type.endswith(".html") and not file_type.endswith(".htm"):
            return "error file type"
        with open(input_file, 'r') as input_page, open("".join([name, '_tw', file_type]), 'w') as output_page:
            while True:
                text = input_page.read(MAXSIZE)
                if not text:
                    break
                response = self.session.post(self.url, data={'text': text, "config": self.config, "precise": 0})
                output_page.write(response.content)
        print "success"

    def multi_task(self, root_path):
        for root, dirs, files in os.walk(root_path):
            for f in files:
                path = os.path.join(root, f)
                print path
                self.simple_to_traditional(path)


def file_format_convert(path, origin_format="vtt", dest_format="srt"):
    """字幕转换程序，将vtt格式转换为srt格式
    :param path: 文件夹路径
    """
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith("." + origin_format):
                filename = f[:-4]
                with open(os.path.join(root, f)) as vttfile, \
                        open(os.path.join(root, filename + "." + dest_format), "w") as srtfile:
                    vttstr = vttfile.readlines()[1:]
                    for line in vttstr:
                        if line.find("-->"):
                            line.replace(r".", r",")
                        srtfile.write(line + "\n")
                os.remove(os.path.join(root, f))
    print u"转换结束"


if __name__ == '__main__':
    file_format_convert(r"C:\MLpyNoteBook")

    # 初始化
    # service = S2T()

    # 转换目录下所有页面
    # service.multi_task(r'..\templates')
    # 简单的转换单个页面
    # service.simple_to_traditional(r"..\templates\Public\login.html")
