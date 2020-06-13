import csv


def get_list_videos(f_path):
    urls_videos = []
    with open(f_path) as f_videos:
        csv_data = csv.reader(f_videos)
        for url_video in csv_data:
            urls_videos.append(url_video[0])
    return urls_videos
