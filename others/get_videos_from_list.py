#!/usr/bin/python3

import getopt
import logging
import os
import sys
import youtube_dl
from pathlib import Path

from file_helper import get_list_videos

logger = logging.getLogger('com.einsoft')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('videos_downloads.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


# def create_dlfolder(path):
#     if not os.path.isdir(path):
#         logger.error(f'The folder {path} doesn\'t exist')
#         os.mkdir(path)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def execute_youtube_dl(urls):
    # download_path = f'{str(Path.home())}/video_downloads'
    logger.info(f'Trying to download {urls}')
    # create_dlfolder(download_path)
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mkv',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


def run_script(argv):
    command = 'get_videos_from_list.py -f <file>'
    f_videos = ''

    try:
        opts, args = getopt.getopt(
            argv, "hf:", ["file="])
    except getopt.GetoptError:
        print(command)
        sys.exit(2)

    for opt, arg in opts:
        if opt is None:
            print(command)
            sys.exit()
        elif opt == '-h':
            print(command)
            sys.exit()
        elif opt in ('-f', "--file"):
            f_videos = arg

    videos = get_list_videos(f_videos)
    logger.info(f"Videos: {len(videos)} ")
    execute_youtube_dl(videos)


if __name__ == "__main__":
    if sys.argv[1:]:
        run_script(sys.argv[1:])
    else:
        sys.exit(
            'get_videos_from_list.py -f <file>')
