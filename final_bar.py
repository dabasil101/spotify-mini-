# import tkinter as tk
# import subprocess

# def spotify_cmd(action):
#     subprocess.run(["playerctl", "-p", "spotify", action],
#                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# class BasilFinalBar:
#     def __init__(self, root):
#         self.root = root
#         self.root.overrideredirect(True)
#         self.root.attributes("-topmost", True)

#         # Dimensions
#         self.width = 460
#         self.height = 40
#         self.root.geometry(f"{self.width}x{self.height}+100+100")

#         self.bg_color = "#0d0d0d"
#         self.root.configure(bg=self.bg_color)

#         self.canvas = tk.Canvas(self.root, width=self.width, height=self.height,
#                                 bg=self.bg_color, highlightthickness=0)
#         self.canvas.pack()

#         # Extra Round Corners for the main bar (Radius increased to 18)
#         self.draw_rounded_rect(2, 2, 458, 38, 18, fill="#121212", outline="#222222")

#         # Single Line Info
#         self.info_text = self.canvas.create_text(20, 15, text="Loading...", fill="white",
#                                                 font=("Ubuntu Sans", 9, "bold"), anchor="w")

#         # Sleek Progress Bar
#         self.progress_bg = self.canvas.create_line(20, 28, 320, 28, fill="#252525", width=2)
#         self.progress_fg = self.canvas.create_line(20, 28, 20, 28, fill="#9141e2", width=2)

#         self.setup_circular_buttons()

#         # Dragging logic
#         self.canvas.bind('<Button-1>', self.click_win)
#         self.canvas.bind('<B1-Motion>', self.drag_win)

#         self.update_loop()

#     def draw_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
#         points = [x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1]
#         return self.canvas.create_polygon(points, **kwargs, smooth=True)

#     def setup_circular_buttons(self):
#         # We use a very small font and tight padding for circular look
#         btn_params = {
#             "fg": "#e0e0e0",
#             "bg": "#121212",
#             "relief": "flat",
#             "activebackground": "#9141e2",
#             "activeforeground": "white",
#             "bd": 0,
#             "font": ("Arial", 10),
#             "width": 2,
#             "cursor": "hand2"
#         }

#         self.prev_btn = tk.Button(self.root, text="⏮", command=lambda: spotify_cmd("previous"), **btn_params)
#         self.play_btn = tk.Button(self.root, text="⏯", command=lambda: spotify_cmd("play-pause"), **btn_params)
#         self.next_btn = tk.Button(self.root, text="⏭", command=lambda: spotify_cmd("next"), **btn_params)

#         # Horizontal placement in the last 100px of the bar
#         self.canvas.create_window(360, 20, window=self.prev_btn)
#         self.canvas.create_window(395, 20, window=self.play_btn)
#         self.canvas.create_window(430, 20, window=self.next_btn)

#     def click_win(self, event):
#         self._offsetx, self._offsety = event.x, event.y

#     def drag_win(self, event):
#         x = self.root.winfo_x() + event.x - self._offsetx
#         y = self.root.winfo_y() + event.y - self._offsety
#         self.root.geometry(f"+{x}+{y}")

#     def update_loop(self):
#         try:
#             title = subprocess.check_output(["playerctl", "-p", "spotify", "metadata", "title"], stderr=subprocess.DEVNULL).decode("utf-8").strip()
#             artist = subprocess.check_output(["playerctl", "-p", "spotify", "metadata", "artist"], stderr=subprocess.DEVNULL).decode("utf-8").strip()

#             combined = f"{title[:20]} • {artist[:15]}"

#             pos = float(subprocess.check_output(["playerctl", "-p", "spotify", "position"], stderr=subprocess.DEVNULL))
#             length_mu = float(subprocess.check_output(["playerctl", "-p", "spotify", "metadata", "mpris:length"], stderr=subprocess.DEVNULL))
#             length = length_mu / 1_000_000

#             ratio = pos / (length if length > 0 else 1)
#             # Bar width is 300 pixels (320 - 20)
#             new_x = 20 + (ratio * 300)

#             self.canvas.itemconfig(self.info_text, text=combined)
#             self.canvas.coords(self.progress_fg, 20, 28, new_x, 28)
#         except:
#             self.canvas.itemconfig(self.info_text, text="Basil Box • Ready")

#         self.root.after(1000, self.update_loop)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = BasilFinalBar(root)
#     root.mainloop()







# import tkinter as tk
# import subprocess
# import sys
# import shutil

# # Fix: Find the absolute path of playerctl to ensure the binary sees it
# PLAYERCTL_PATH = shutil.which("playerctl")

# def spotify_cmd(action):
#     if not PLAYERCTL_PATH:
#         return
#     try:
#         subprocess.run([PLAYERCTL_PATH, "-p", "spotify", action],
#                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     except Exception:
#         pass

# class BasilFinalBar:
#     def __init__(self, root):
#         self.root = root
#         self.root.overrideredirect(True)
#         self.root.attributes("-topmost", True)

#         # Dimensions
#         self.width = 460
#         self.height = 40
#         self.root.geometry(f"{self.width}x{self.height}+100+100")

#         self.bg_color = "#0d0d0d"
#         self.root.configure(bg=self.bg_color)

#         self.canvas = tk.Canvas(self.root, width=self.width, height=self.height,
#                                 bg=self.bg_color, highlightthickness=0)
#         self.canvas.pack()

#         # Extra Round Corners for the main bar
#         self.draw_rounded_rect(2, 2, 458, 38, 18, fill="#121212", outline="#222222")

#         # Single Line Info
#         self.info_text = self.canvas.create_text(20, 15, text="Basil Box • Ready", fill="white",
#                                                 font=("Ubuntu Sans", 9, "bold"), anchor="w")

#         # Sleek Progress Bar
#         self.progress_bg = self.canvas.create_line(20, 28, 320, 28, fill="#252525", width=2)
#         self.progress_fg = self.canvas.create_line(20, 28, 20, 28, fill="#9141e2", width=2)

#         self.setup_circular_buttons()
#         self.create_context_menu()

#         # Bindings
#         self.canvas.bind('<Button-1>', self.click_win)
#         self.canvas.bind('<B1-Motion>', self.drag_win)

#         # Right-Click Menu Binding
#         self.root.bind("<Button-3>", self.show_menu)

#         self.update_loop()

#     def create_context_menu(self):
#         self.menu = tk.Menu(self.root, tearoff=0, bg="#161616", fg="white",
#                             activebackground="#9141e2", bd=0)
#         self.menu.add_command(label="Close App", command=sys.exit)

#     def show_menu(self, event):
#         self.menu.post(event.x_root, event.y_root)

#     def draw_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
#         points = [x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1]
#         return self.canvas.create_polygon(points, **kwargs, smooth=True)

#     def setup_circular_buttons(self):
#         btn_params = {
#             "fg": "#e0e0e0", "bg": "#121212", "relief": "flat",
#             "activebackground": "#9141e2", "activeforeground": "white",
#             "bd": 0, "font": ("Arial", 10), "width": 2, "cursor": "hand2"
#         }

#         self.prev_btn = tk.Button(self.root, text="⏮", command=lambda: spotify_cmd("previous"), **btn_params)
#         self.play_btn = tk.Button(self.root, text="⏯", command=lambda: spotify_cmd("play-pause"), **btn_params)
#         self.next_btn = tk.Button(self.root, text="⏭", command=lambda: spotify_cmd("next"), **btn_params)

#         self.canvas.create_window(360, 20, window=self.prev_btn)
#         self.canvas.create_window(395, 20, window=self.play_btn)
#         self.canvas.create_window(430, 20, window=self.next_btn)

#     def click_win(self, event):
#         self._offsetx, self._offsety = event.x, event.y

#     def drag_win(self, event):
#         x = self.root.winfo_x() + event.x - self._offsetx
#         y = self.root.winfo_y() + event.y - self._offsety
#         self.root.geometry(f"+{x}+{y}")

#     def update_loop(self):
#         if not PLAYERCTL_PATH:
#             self.canvas.itemconfig(self.info_text, text="Error: playerctl not found")
#             return

#         try:
#             # Fetch metadata using absolute path
#             title = subprocess.check_output([PLAYERCTL_PATH, "-p", "spotify", "metadata", "title"], stderr=subprocess.DEVNULL).decode("utf-8").strip()
#             artist = subprocess.check_output([PLAYERCTL_PATH, "-p", "spotify", "metadata", "artist"], stderr=subprocess.DEVNULL).decode("utf-8").strip()

#             pos = float(subprocess.check_output([PLAYERCTL_PATH, "-p", "spotify", "position"], stderr=subprocess.DEVNULL))
#             length_mu = float(subprocess.check_output([PLAYERCTL_PATH, "-p", "spotify", "metadata", "mpris:length"], stderr=subprocess.DEVNULL))
#             length = length_mu / 1_000_000

#             ratio = pos / (length if length > 0 else 1)
#             new_x = 20 + (ratio * 300)

#             self.canvas.itemconfig(self.info_text, text=f"{title[:20]} • {artist[:15]}")
#             self.canvas.coords(self.progress_fg, 20, 28, new_x, 28)
#         except Exception:
#             self.canvas.itemconfig(self.info_text, text="Basil Box • Ready")

#         self.root.after(1000, self.update_loop)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = BasilFinalBar(root)
#     root.mainloop()




import tkinter as tk
import sys
from pydbus import SessionBus

class BasilProBar:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.geometry("460x40+100+100")
        self.root.configure(bg="#0d0d0d")

        # Initialize DBus for Spotify
        self.bus = SessionBus()
        self.player = None
        self.connect_spotify()

        self.canvas = tk.Canvas(self.root, width=460, height=40, bg="#0d0d0d", highlightthickness=0)
        self.canvas.pack()

        # UI Design
        self.draw_rounded_rect(2, 2, 458, 38, 18, fill="#121212", outline="#222222")
        self.info_text = self.canvas.create_text(20, 15, text="Basil Box • Connecting...", fill="white",
                                                font=("Ubuntu Sans", 9, "bold"), anchor="w")
        self.progress_bg = self.canvas.create_line(20, 28, 320, 28, fill="#252525", width=2)
        self.progress_fg = self.canvas.create_line(20, 28, 20, 28, fill="#9141e2", width=2)

        self.setup_buttons()

        # Right-Click Menu
        self.menu = tk.Menu(self.root, tearoff=0, bg="#161616", fg="white", activebackground="#9141e2")
        self.menu.add_command(label="Close Basil Box", command=sys.exit)
        self.root.bind("<Button-3>", lambda e: self.menu.post(e.x_root, e.y_root))

        # Movement
        self.canvas.bind('<Button-1>', self.start_move)
        self.canvas.bind('<B1-Motion>', self.do_move)

        self.update_loop()

    def connect_spotify(self):
        try:
            self.player = self.bus.get("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        except:
            self.player = None

    def draw_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1]
        return self.canvas.create_polygon(points, **kwargs, smooth=True)

    def setup_buttons(self):
        style = {"fg": "#e0e0e0", "bg": "#121212", "relief": "flat", "bd": 0, "font": ("Arial", 10), "width": 2}
        tk.Button(self.root, text="⏮", command=lambda: self.player.Previous() if self.player else None, **style).place(x=345, y=10)
        tk.Button(self.root, text="⏯", command=lambda: self.player.PlayPause() if self.player else None, **style).place(x=380, y=10)
        tk.Button(self.root, text="⏭", command=lambda: self.player.Next() if self.player else None, **style).place(x=415, y=10)

    def start_move(self, event): self.x, self.y = event.x, event.y
    def do_move(self, event): self.root.geometry(f"+{self.root.winfo_x()+(event.x-self.x)}+{self.root.winfo_y()+(event.y-self.y)}")

    def update_loop(self):
        if not self.player:
            self.connect_spotify()
            self.canvas.itemconfig(self.info_text, text="Basil Box • Spotify Offline")
        else:
            try:
                meta = self.player.Metadata
                title = meta.get('xesam:title', 'Unknown')
                artist = meta.get('xesam:artist', ['Unknown'])[0]
                length = meta.get('mpris:length', 0)
                pos = self.player.Position

                self.canvas.itemconfig(self.info_text, text=f"{title[:20]} • {artist[:15]}")
                ratio = pos / length if length > 0 else 0
                self.canvas.coords(self.progress_fg, 20, 28, 20 + (ratio * 300), 28)
            except:
                self.player = None
        self.root.after(1000, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    BasilProBar(root)
    root.mainloop()
