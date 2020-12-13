# to convert clone_voy.py to .exe

i) pip install pyinstaller
ii)pip install pywin32 and pywin

# ValueError: Unable to find token seed! Did https://translate.google.com change?

python -m pip install --upgrade gtts
python -m pip install --upgrade gtts-token

# To  make your python portable (one file program)
Follow step 1 or step 2
Step 1: command line "pyinstaller --hidden-import=pyttsx3.drivers.sapi5 --onefile cloner_voy.py"

Step 2: command line "pyinstaller --hidden-import=pyttsx3.drivers --onefile cloner_voy.py"
