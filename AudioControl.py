# pydub for loading/editing and a playback library like simpleaudio to actually hear the sound

from pydub import AudioSegment
from pydub.playback import play

# Install a simple playback library
# cmd: pip install simpleaudio (installing C++ tools from Visual Studio)
# must have simpleaudio installed for play to work

class audio_Control:
    """
    Manages music playback using pydub for loading and simpleaudio
    (via pydub.playback) for playing.
    """

    def __init__(self, playlist_paths: list):
        # Args: playlist_paths (list): A list of string file paths to the audio files.

        if not playlist_paths:
            raise ValueError("Playlist cannot be empty.")

        # --- State Management ---
        self.playlist: list = list(playlist_paths) # A copy of the paths to work on
        self.current_index: int = 0
        self.volume_db: float = 0.0 # Volume in decibels

        # --- Playback Objects ---
        self.original_segment: AudioSegment | None = None # Raw loaded file
        self.current_segment: AudioSegment | None = None  # Volume-adjusted file
        self.playback_handle = None # The simpleaudio PlayObject
        self.is_playing: bool = False
        self.is_paused: bool = False

    def play_Audio(self, file_name: str): # file_name = "./music_files/mySong1.mp3" is an example
        try:    
            song = AudioSegment.from_mp3(file_name)
            play(song)
        except Exception as e:
            print("Error: ", e)

    def pause_Audio(self):
        pass

    def prev_Audio(self):
        pass

    def next_Audio(self):
        pass

    def repeat_Audio(self):
        pass

    def shuffle_Playlist(self):
        pass

    def seek_Audio(self):
        pass

    def change_Volume(self, Inc = False, Dec = False):
        if Inc:
            #increase volume
            return
        elif Dec:
            #decrease volume
            return
        else:
            #do nothing
            return
        
    def add_to_Favourites(self):
        pass

    def view_Playlist(self):
        pass

    def view_Lyrics(self):
        pass

    def organize_Folder(self):
        pass