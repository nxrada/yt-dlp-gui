import tkinter as tk
import yt_dlp_wrapper as wrapper

class GUI:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.master, text="Enter the URL of the video to download:")
        label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        button = tk.Button(self.master, text="Download Video", command=self.download())
        button.pack()

    def download(url):
        wrapper.download_video(url)

