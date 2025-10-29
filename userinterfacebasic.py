from tkinter import *
from PIL import Image, ImageTk

# ============================================================
# 🪩 GROOVE PLAYER UI
# ============================================================

#window setup
root = Tk()
root.title("Groove Player")
root.geometry("900x600")
root.config(bg="#121212")  

#background image
bg_path = "C:/Users/nayan/Documents/music player/bg4.png" #pls update the path accordingly
original_image = Image.open(bg_path)
bg_image = ImageTk.PhotoImage(original_image)

canvas = Canvas(root, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

image_id = canvas.create_image(0, 0, anchor="nw", image=bg_image) 


#sample playlist
playlist = [
    ("Lost Frequencies - Are You With Me", "Lost Frequencies"),
    ("Kygo - Firestone", "Kygo"),
    ("Zedd - Clarity", "Zedd"),
    ("Martin Garrix - Animals", "Martin Garrix"),
    ("Calvin Harris - Feel So Close", "Calvin Harris"),
    ("Avicii - Levels", "Avicii")
]

current_song_index = 0 #current song playing


#title
title_id = canvas.create_text(
    450, 60,
    text="🎧 Groove Player",
    fill="#FFFFFF",
    font=("Segoe UI", 28, "bold")
)

#song info
song_title_id = canvas.create_text(
    450, 200,
    text=f"Now Playing: {playlist[current_song_index][0]}",
    fill="#061A0D",
    font=("Segoe UI", 15, "bold")
)

song_artist_id = canvas.create_text(
    450, 230,
    text=f"Artist: {playlist[current_song_index][1]}",
    fill="#0B3518",
    font=("Segoe UI", 12)
)

#progress bar
progress_bg_id = canvas.create_rectangle(200, 300, 700, 310, fill="#333333", outline="")
progress_fg_id = canvas.create_rectangle(200, 300, 380, 310, fill="#1DB954", outline="")

#sample timing display
time_left_id = canvas.create_text(200, 320, text="1:12", fill="#000000", font=("Segoe UI", 10), anchor="w")
time_right_id = canvas.create_text(700, 320, text="3:45", fill="#000000", font=("Segoe UI", 10), anchor="e")

#controls setup
button_bg = "#1F1F1F" 
button_fg = "#FFFFFF"   

controls_frame = Frame(canvas, bg="#121212")

controls_window = canvas.create_window(450, 500, window=controls_frame, anchor="center")

#button style for all buttons
btn_style = {"font": ("Segoe UI Symbol", 18), "width": 3, "height": 1, "bd": 0}

is_playing = False  #toggle state

#controls
def toggle_play_pause():
    #switch between play ▶ and pause ⏸ icons
    global is_playing
    play_button.config(text="▶" if is_playing else "⏸")
    is_playing = not is_playing

def update_song_display():
    current_song, current_artist = playlist[current_song_index]
    canvas.itemconfig(song_title_id, text=f"Now Playing: {current_song}")
    canvas.itemconfig(song_artist_id, text=f"Artist: {current_artist}")

def next_song():
    #go to next song
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    update_song_display()

def previous_song():
    #go back to the previous song
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    update_song_display()

def play_selected_song(event):
    #play a song from the playlist when double-clicked
    global current_song_index
    selection = event.widget.curselection()
    if selection:
        current_song_index = selection[0]
        update_song_display()

def open_playlist():
    playlist_window = Toplevel(root)
    playlist_window.title("Your Playlist")
    playlist_window.geometry("400x400")
    playlist_window.config(bg="#181818")

    Label(
        playlist_window,
        text="🎵 Your Playlist",
        font=("Segoe UI", 20, "bold"),
        fg="#1DB954",
        bg="#181818"
    ).pack(pady=20)

    #listbox for songs
    song_listbox = Listbox(
        playlist_window,
        bg="#1F1F1F",
        fg="#FFFFFF",
        font=("Segoe UI", 12),
        selectbackground="#1DB954",
        selectforeground="#FFFFFF",
        highlightthickness=0,
        relief=FLAT
    )

    #load songs into the list
    for song, artist in playlist:
        song_listbox.insert(END, song)

    song_listbox.pack(fill=BOTH, expand=True, padx=20, pady=10)

    #double-click to play selected song
    song_listbox.bind("<Double-1>", play_selected_song)

    Button(
        playlist_window,
        text="Close",
        font=("Segoe UI", 12, "bold"),
        fg="#FFFFFF",
        bg="#1DB954",
        relief=FLAT,
        width=10,
        command=playlist_window.destroy
    ).pack(pady=10)

#control buttons
prev_button = Button(controls_frame, text="⏮", bg=button_bg, fg=button_fg, command=previous_song, **btn_style)
play_button = Button(controls_frame, text="▶", bg=button_bg, fg=button_fg, command=toggle_play_pause, **btn_style)
next_button = Button(controls_frame, text="⏭", bg=button_bg, fg=button_fg, command=next_song, **btn_style)
like_button = Button(controls_frame, text="❤", bg=button_bg, fg="#FF4B5C", **btn_style)
playlist_button = Button(controls_frame, text="📂", bg=button_bg, fg=button_fg, command=open_playlist, **btn_style)

#arrange buttons neatly with spacing
for i, btn in enumerate([prev_button, play_button, next_button, like_button, playlist_button]):
    btn.grid(row=0, column=i, padx=10)

#window size adjusting
def resize_elements(event):
    """Adjust all UI elements proportionally when window is resized."""
    resized = original_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized)
    canvas.bg_image = new_bg  # prevent garbage collection
    canvas.itemconfig(image_id, image=new_bg)

    #reposition text and bars dynamically
    canvas.coords(title_id, event.width / 2, event.height * 0.1)
    canvas.coords(song_title_id, event.width / 2, event.height * 0.35)
    canvas.coords(song_artist_id, event.width / 2, event.height * 0.40)

    bar_start = event.width * 0.22
    bar_end = event.width * 0.78
    bar_y = event.height * 0.5

    canvas.coords(progress_bg_id, bar_start, bar_y, bar_end, bar_y + 10)
    canvas.coords(progress_fg_id, bar_start, bar_y, bar_start + (bar_end - bar_start) * 0.3, bar_y + 10)
    canvas.coords(time_left_id, bar_start, bar_y + 20)
    canvas.coords(time_right_id, bar_end, bar_y + 20)

    #move control buttons slightly down for better proportions
    canvas.coords(controls_window, event.width / 2, event.height * 0.82)

canvas.bind("<Configure>", resize_elements)

root.mainloop()
