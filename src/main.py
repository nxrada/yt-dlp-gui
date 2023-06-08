'''
Main function for yt-dlp-gui
'''
import tkinter as tk
import gui

def main():
    root = tk.Tk()
    local_gui = gui.GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
