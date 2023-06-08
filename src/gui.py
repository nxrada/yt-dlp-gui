import tkinter as tk
import yt_dlp_wrapper as wrapper

class GUI:
    default_file_directory = "../downloads/"

    def __init__(self, master):
        self.master = master
        self.create_widgets()

    # Creates GUI elements
    def create_widgets(self):
        url_entry_prompt = tk.Label(self.master, text="Enter the URL of the video to download:")
        url_entry_prompt.pack()

        self.url_entry = tk.Entry(self.master)
        self.url_entry.pack()
        

        button = tk.Button(self.master, text="Download Video", command=wrapper.download_video(self.url_entry.get()))
        button.pack()


    def set_download_file_directory(directory):
        pass
