NeteaseMusicLyricDownloader
===========================
**English**|[简体中文](./README_cn.md)

A simple tool to download lyrics in Netease Music

## How does it work?
It uses the module `requests` to fetch the lyric on music.163.com

Netease Music supply us an api that we can get the lyric of the current song, so I make this program...

## Installation
First, you need a python environment, and use `pip` to install these packages: `requests` `mutagen` `pycryptodome`
>Feel complex? just copy this command to your terminal: `python3 -m pip install requests mutagen pycryptodome`

Second, clone the entire project and run the command `python3 main.py` in the project folder.

## What can it do?
Just download lyrics.

You need to provide the id or the share link of the song, and the program will download the lyrics automatically.

Now it can recognize 163 key in music files that download from Netease Cloudmusic client.

- 2022/8/13 Now it has the function from `ncmdump`, it can decrypt the ncm files and fetch the specific lyric.

## Todo

Add more functions like searching...

## Others

Just a easy program...

I haven't much time to focus on it...
