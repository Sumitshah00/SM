#owner @Byteassassins
import os
from pytube import YouTube, Playlist
import instaloader
import requests
from rich.console import Console
from rich.panel import Panel

def download_youtube_video(url, download_path='./'):
    yt = YouTube(url)
    stream = yt.streams.filter(res="1080p", file_extension='mp4').first()
    if not stream:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(download_path)
    print(f"Downloaded YouTube video: {yt.title}")

def download_youtube_shorts(url, download_path='./'):
    yt = YouTube(url)
    stream = yt.streams.filter(res="1080p", file_extension='mp4').first()
    if not stream:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(download_path)
    print(f"Downloaded YouTube Short: {yt.title}")

def download_youtube_playlist(url, download_path='./'):
    pl = Playlist(url)
    for video in pl.videos:
        stream = video.streams.filter(res="1080p", file_extension='mp4').first()
        if not stream:
            stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download(download_path)
        print(f"Downloaded video from playlist: {video.title}")

def download_instagram_post(url, download_path='./'):
    loader = instaloader.Instaloader(download_pictures=False, download_videos=True, download_video_thumbnails=False)
    post_shortcode = url.split('/')[-2]
    post = instaloader.Post.from_shortcode(loader.context, post_shortcode)
    loader.download_post(post, target=download_path)
    print(f"Downloaded Instagram post: {post.title}")

def print_banner():
    banner_text = """
[red]</dev> BYTEASSASSINS </dev>[/red]

[red]</git> https://github.com/SumitShah00 </git>[/red]
"""
    console = Console()
    panel = Panel(
        banner_text,
        border_style="blue",
        title="[bold red]BYTEASSASSINS[/bold red]",
        subtitle="SM-Video downloader V1.0",
    )
    console.print(panel)

def main():
    print_banner()
    print("Welcome! Please select the platform:")
    print("1. Instagram")
    print("2. YouTube")

    platform_choice = input("Please select which you want to download (1/2): ")

    if platform_choice == '1':
        url = input("Please enter the Instagram video URL: ")
        download_instagram_post(url)
    elif platform_choice == '2':
        print("Please select the YouTube option:")
        print("1. YouTube Video")
        print("2. YouTube Shorts")
        print("3. YouTube Playlist")

        youtube_choice = input("Please select which you want to download (1/2/3): ")

        url = input("Please enter the YouTube URL: ")

        if youtube_choice == '1':
            download_youtube_video(url)
        elif youtube_choice == '2':
            download_youtube_shorts(url)
        elif youtube_choice == '3':
            download_youtube_playlist(url)
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
