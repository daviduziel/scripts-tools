#!/usr/bin/python3

import getopt
import logging
import os
import sys
from pathlib import Path

from file_helper import get_list_videos

logger = logging.getLogger('com.einsoft')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('videos_downloads.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


def create_dlfolder(path):
    if not os.path.isdir(path):
        logger.error(f'The folder {path} doesn\'t exist')
        os.mkdir(path)


def execute_youtube_dl(url):
    download_path = f'{str(Path.home())}/video_downloads'
    logger.info(f'Trying to download {url}')
    create_dlfolder(download_path)
    try:
        os.system(
            f'youtube-dl "{url}" -f bestvideo+bestaudio --recode-video mkv --output "{download_path}/%(title)s.%(ext)s"')
    except Exception:
        logger.error(f'The download of {url} failed')


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
    for video in videos:
        try:
            execute_youtube_dl(video)
        except Exception as e:
            logger.error(
                f'Error  trying to save the video {e}')


if __name__ == "__main__":
    if sys.argv[1:]:
        run_script(sys.argv[1:])
    else:
        sys.exit(
            'get_videos_from_list.py -f <file>')
