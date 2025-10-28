# Groove
*Groove* is a simple Music player that keeps record of your favourite tracks and makes your listening experience more fluent.

# Built by
- Aranya Rayed
- Nayanika Chatterjee
- Ankan Sadhu

# currently under production

# Import necessary Libraries
1. PyDub:
```
pip install pydub
```

2. ffmpeg: (for playing .mp3 files)
- This method uses Winget, the built-in Windows Package Manager. It's a single command.
- Open PowerShell or Command Prompt as an Administrator.
- Click the Start menu, type "PowerShell," right-click it, and select "Run as administrator."
- Copy and paste the following command, then press Enter:
```
winget install --id Gyan.FFmpeg.Shared
```
- Winget will automatically download, install, and set up the system PATH for you.
- Once it's finished, close your terminal window and open a new one.
- Open a new Command Prompt or PowerShell window. Any terminals you had open before changing the PATH will not work.
- Type the following command and press enter.
```
ffmpeg -version
```
- If it's installed correctly, you will see a bunch of text starting with ffmpeg version ..., along with configuration details.

3. simpleaudio:
```
pip install simpleaudio
```

4. Tkinter:
```
pip install tkinter
```

