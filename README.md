# YouTube-Video-Dowloader
This Python module facilitates the downloading and processing of YouTube videos. It handles downloading both video and audio streams from YouTube, merging them into a single file, and then cleaning up the individual stream files.

Features:

- Download YouTube Video and Audio: Downloads video and audio streams from a given YouTube URL.
- Merge Video and Audio: Combines downloaded video and audio streams into a single file using FFmpeg.
- Clean Up: Deletes the separate video and audio files after merging.
- Sample Execution: Includes a sample YouTube URL for testing the functionality.

Functions:

- get_youtube_video(url): Downloads video and audio streams from the provided YouTube URL and merges them.
- merge_video_audio(yt_object, video_file, audio_file): Merges the downloaded video and audio files using FFmpeg.
- delete_sep_streams(files): Deletes the specified video and audio files.
- main(): Runs the module with a sample YouTube URL.

Dependencies:

- ffmpeg: Required for merging video and audio streams.
- pytubefix: Used for downloading YouTube streams.
- pytubefix.exceptions: Handles exceptions related to video availability.
- os: For file operations.

Usage:

- Install the required dependencies.

- Run the script. It will download and merge the video and audio streams from the sample YouTube URL provided in the main() function.
Feel free to modify the main() function to test with different YouTube URLs.

Installation
You can install the required dependencies using pip.

```pip install ffmpeg-python``` or
```python3 -m pip install ffmpeg-python```

Ensure that FFmpeg is installed on your system. You can download it from FFmpeg's official website.
 
