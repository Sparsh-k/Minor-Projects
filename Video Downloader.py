import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

root=Tk()
root.title('Video Downloader')
canvas=Canvas(root, width=400, height=300, bg='grey')
canvas.pack()

## file opener

def open_file():
    filename=filedialog.askdirectory(initialdir='/',title='Choose a file to download video')
    path_label.config(text=filename)

## Download button

def download():
    video_path=URL_entry.get()
    file_path=path_label.cget('text')
    print("Downloading.....")
    mp4= YouTube(video_path).streams.get_highest_resolution().download()
    video_clip= VideoFileClip(mp4)
    video_clip.close()
    shutil.move(mp4, file_path)
    print("Download Complete")


## App labels

app_label= Label(root, text='Video Downloader', bg='grey', fg='red', font='Calibri')

URL_label= Label(root, text='Enter your URL', bg='grey', fg='black')

path_label= Label(root, text='Select the path to download', bg='grey', fg='black')

## App Entry

URL_entry=Entry(root)


## Buttons

path_button= Button(root,text='Select', command=lambda:open_file())
download_button= Button(root, text='Download', command=download)

## Grid

canvas.create_window(200, 28, window=app_label)
canvas.create_window(200, 88, window=URL_label)
canvas.create_window(200, 118, window=URL_entry)
canvas.create_window(100, 148, window=path_label)
canvas.create_window(200, 148, window=path_button)
canvas.create_window(200, 218, window=download_button)

root.mainloop()