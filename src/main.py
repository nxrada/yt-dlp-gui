'''
yt-dlp-gui: simple GUI wrapper for yt-dlp
hosted at <https://www.github.com/nxrada/yt-dlp-gui/> 
'''
import tkinter as tk
from yt_dlp import YoutubeDL
from yt_dlp import utils


# Downloads video using YoutubeDL
def download_video(url: str):
    try:
        with YoutubeDL() as ydl:
            ydl.download(url)
    except utils.DownloadError as e:
        print(e)


root = tk.Tk()
root.title("Feet to Meters")

mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"), padx=3, pady=3)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = tk.StringVar()
feet_entry = tk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=("W", "E"))

meters = tk.StringVar()
tk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=("W", "E"))

tk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky="W")

tk.Label(mainframe, text="feet").grid(column=3, row=1, sticky="W")
tk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky="E")
tk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="W")

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()