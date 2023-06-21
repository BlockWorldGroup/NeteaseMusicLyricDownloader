#!/usr/bin/env python3
# ↑ For Linux & macOS to run this program directly if the user currently installed python and third-party packages.
# -*- coding: utf-8 -*-
# author: David-123

from sys import exit

from colorama import init

from modules.utils.inputs import rinput
from modules.utils.prints import print_info, print_menu
from modules.functions.mainly.multi_download import mdl
from modules.functions.mainly.one_download import download_one_lyric
from modules.submenus.settings import settings_menu
from modules.functions.settings.save_load_settings import load_settings
from modules.utils.clear_screen import cls_stay
from modules.functions.mainly.load_file_song import get_lyric_from_folder


class MainProcess(object):
    def __init__(self):  # 项目初始化
        self.settings = load_settings()
        self.version = "1.0"

    def mainloop(self):
        """程序主循环"""
        while True:
            cls_stay(self, "[程序主菜单]")
            print_menu({
                "0": "退出程序",
                "1": "单个歌曲的歌词下载",
                "2": "多个歌曲的歌词下载",
                "3": "从网易云下载的歌曲中获取歌词",
                "s": "进入设置",
                "i": "程序信息",
            })
            r = rinput("请选择:")

            if r == "1":
                download_one_lyric(self)
            elif r == "2":
                mdl(self)
            elif r == "3":
                get_lyric_from_folder(self)
            elif r == "0":
                exit(0)
            elif r == "i":
                print_info(self)
            elif r == "s":
                settings_menu(self)
            else:
                input("请输入正确的选项\n按回车键继续...")


if __name__ == "__main__":
    init(autoreset=True)
    app = MainProcess()
    try:
        app.mainloop()
    except KeyboardInterrupt:
        exit(-1)
