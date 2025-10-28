# pydub for loading/editing and a playback library like simpleaudio to actually hear the sound

from pydub import AudioSegment
from pydub.playback import play
from os import path

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
    

    def _load_song(self, index: int):
        """Internal helper to load and prepare a song."""
        if not (0 <= index < len(self.playlist)):
            print(f"Error: Index {index} is out of range.")
            return False
        try:
            song_path = self.playlist[index]
            self.current_index = index
            # Load the file
            self.original_segment = AudioSegment.from_file(song_path)
            # Apply current volume to create the segment we will play
            self.current_segment = self.original_segment + self.volume_db
            base_name = path.basename(song_path)
            song_name = path.splitext(base_name)[0] # This will get only the song name
            print(f"Loaded: {song_name}")
            return True
        except Exception as e:
            print(f"Error loading file {song_path}: {e}")
            self.original_segment = None
            self.current_segment = None
            return False


    def _play_segment(self):
        """Internal helper to start playback of the current segment."""
        if self.current_segment:
            # Stop any sound that is currently playing
            self.stop_audio()
            
            # Start new playback
            self.playback_handle = play(self.current_segment)
            self.is_playing = True
            self.is_paused = False
        else:
            print("No audio segment loaded to play.")


    def stop_audio(self):
        """Stops any currently playing audio."""
        if self.playback_handle:
            self.playback_handle.stop()
        self.playback_handle = None
        self.is_playing = False
        self.is_paused = False # Stopping is not pausing


    def play_Audio(self, file_name: str): # file_name = ".\music_files\mySong1.mp3" is an example
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