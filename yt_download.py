"""
This module downloads and processes YouTube videos.

Functions:
- `get_youtube_video(url)`: Downloads video and audio streams from a YouTube URL and merges them.
- `merge_video_audio(yt_object, video_file, audio_file)`: Merges downloaded video and audio files
using FFmpeg.
- `delete_sep_streams(files)`: Deletes the specified video and audio files.
- `main()`: Runs the module with a sample YouTube URL.

Dependencies:
- `ffmpeg`, `pytubefix`, `pytubefix.exceptions`, `os`
"""

import os
import ffmpeg
from pytubefix import YouTube
from pytubefix.cli import on_progress
import pytubefix.exceptions

def get_youtube_video(url):
    """Function creates YouTube Object, selects a video,
    and audio stream and downloads both streams."""

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except pytubefix.exceptions.VideoUnavailable:
        print('Video is unavailable.')

    # Initiate audio/video stream file names.
    video_file = f'{yt.title}_video.mp4'
    audio_file = f'{yt.title}_audio.mp4'

    # Select the first video stream with 1080p resolution and download it.
    video = yt.streams.filter(resolution='1080p', adaptive=True).first()
    if video:
        print('Downloading Video...')
        video.download(filename = video_file)
    else:
        print('No video stream found.')

    # Select the first audio stream to be downloaded.
    audio = yt.streams.filter(only_audio=True, adaptive=True).first()
    if audio:
        print('Downloading Audio...')
        audio.download(filename = audio_file)
    else:
        print('No audio stream found.')

    merge_video_audio(yt, video_file, audio_file)


def merge_video_audio(yt_object, video_file, audio_file):
    """Function Merges audio and video stream into one file
    and calls the delete_sep_streams function."""

    # Check if the files exist.
    if os.path.exists(video_file) and os.path.exists(audio_file):
        input_video = ffmpeg.input(video_file)
        input_audio = ffmpeg.input(audio_file)

        # Store the seperate files in list to be deleted later.
        streams = [video_file, audio_file]

        # Set path for where to download the merged file.
        path = '/Users/deshaud/Downloads/'

        # Merge the audio and video stream.
        ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'{path}'
                                                                 f'{yt_object.title}.mp4').run()
        delete_sep_streams(streams)
    else:
        print('File does not exist.')


def delete_sep_streams(files):
    """Function deletes the two individual audio and video files."""

    if files:
        print('\nDeleting seperate audio & video files...')
        for file in files:
            os.remove(file)
        print('Files deleted.')
    else:
        print('No files found.')


def main():
    """Main part of the program which calls get_youtube_video
    function with a URL. """

    while True:

        url = input('Enter URL: ').strip()
        
        if url.lower() == 'q':
            break
        else:
            get_youtube_video(url)

if __name__ == '__main__':
    main()
