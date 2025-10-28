# pydub for loading/editing and a playback library like simpleaudio to actually hear the sound

from pydub import AudioSegment
from pydub.playback import play

# Install a simple playback library
# cmd: pip install simpleaudio (some error is occuring during installation)

class audio_Control:
    def __init__(self):
        self.current_song = None
        self.songs = []
        pass

    def play_Audio(self):
        try:    
            song = AudioSegment.from_mp3("./music_files/song1.mp3")
            self.songs.append(str(song))
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