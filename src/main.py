'''
yt-dlp-gui: simple GUI wrapper for yt-dlp
hosted at <https://www.github.com/nxrada/yt-dlp-gui/> 
'''
import tkinter as tk
from yt_dlp import YoutubeDL
from yt_dlp import utils
import re

DOWNLOAD_DIR = "../downloads/%(title)s.%(ext)s"


# Sanatizes error before print to GUI. 
def sanitize_error(e):
    error = str(e)
    match = re.search(r"'(.*?)' is not a valid URL.", error)
    if match:
        sanitized_string = f"ERROR: {match.group(0)}"
        return sanitized_string
    else:
        return e
def set_ydl_options():
    ydl_options = {
        'outtmpl': DOWNLOAD_DIR,
    }
    return ydl_options

def download_video(url: str, console_log):
    try:
        # Re-enable the console log, insert text, then disable it
        console_log['state'] = 'normal'
        console_log.delete('1.0', tk.END)
        console_log['state'] = 'disabled'
        
        # Download video
        YoutubeDL(set_ydl_options()).download([url])        
        
        # Re-enable the console log, insert text, then disable it
        console_log['state'] = 'normal'
        console_log.insert(tk.END, '\nFile downloaded to ../downloads/.')
        console_log['state'] = 'disabled'

    except utils.DownloadError as e:
        # Print to console log window
        console_log['state'] = 'normal'
        console_log.insert(tk.END, sanitize_error(e)+'\n')
        console_log['state'] = 'disabled'

# Main function
def main():
    # Sets up main application window, with title "yt-dlp"
    root = tk.Tk()
    root.title("yt-dlp")

    # Creates content frame to hold widgets of user interface
    mainframe = tk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'), padx=3, pady=3)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Widgets for URL input 
    url = tk.StringVar()
    url_entry = tk.Entry(mainframe, width=43, textvariable=url)
    url_entry.grid(column=1, row=1, sticky=('W', 'E'))
    tk.Label(mainframe, text="Input URL:").grid(column=0, row=1, sticky='E')

    # Widget for download button
    download_button = tk.Button(mainframe, text="Download", command=lambda: download_video(str(url.get()), console_log))
    download_button.grid(column=2, row=1, sticky='W')

    # Widgets for Console log
    console_log = tk.Text(mainframe, width=60, height=10)
    console_log['state'] = 'disabled'
    console_log.grid(column=0, row=2, columnspan=3, sticky='WE')

    # Padding forchildren
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    
    # Directs input focus to URL entry bar
    url_entry.focus()
    
    # Runs tk event loop 
    root.mainloop()

# Executes code. 
if __name__ == "__main__":
    main()
