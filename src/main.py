'''
yt-dlp-gui: simple GUI wrapper for yt-dlp
hosted at <https://www.github.com/nxrada/yt-dlp-gui/> 
'''
import tkinter as tk
from yt_dlp import YoutubeDL
import logging

DOWNLOAD_DIR = "../downloads/%(title)s.%(ext)s"
handler = None
    
# Handles event hooks passed from YouTubeDL during download process. 
def my_hook(d, console_log):
    if d['status'] == 'finished':
        filename = d['_filename']
        console_log['state'] = 'normal'
        console_log.insert(tk.END, f'\nFile downloaded to f{filename}.\n')
        console_log['state'] = 'disabled'


# Sets options for YoutTubeDL.download() function. 
def set_ydl_options(console_log):
    global handler
    logger = logging.getLogger()
    if handler:
        logger.removeHandler(handler)
    logger = logging.getLogger()
    handler = TextHandler(console_log)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    ydl_options = {
        'outtmpl': DOWNLOAD_DIR,
        'logger': logger,
        'progress_hooks': [lambda d: my_hook(d, console_log)],
    }
    return ydl_options

def download_video(url: str, console_log):
    console_log['state'] = 'normal'
    console_log.delete('1.0', tk.END)
    console_log['state'] = 'disabled'
    try:        
        # Download video
        YoutubeDL(set_ydl_options(console_log)).download([url])        

    except Exception as e:
        # Print to console log window
        console_log['state'] = 'normal'
        console_log.insert(tk.END, str(e)+'\n')
        console_log['state'] = 'disabled'


# Logging handler
class TextHandler(logging.Handler):
    def __init__(self, console_log):
        logging.Handler.__init__(self)
        self.console_log = console_log

    def emit(self, record):
        log_entry = self.format(record)
        self.console_log['state'] = 'normal'
        self.console_log.insert(tk.END, log_entry + '\n')
        self.console_log['state'] = 'disabled'
        self.console_log.see(tk.END)  # Scroll to end


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
