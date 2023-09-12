# Clipboard-Translator-with-Hotkeys
A python project i was interested in doing for in-Game chat (League of Legends). Basically u press a hot key and the selected text gets translated.
The hotkeys are set as follows ctrl + t allows u to translate a text to a certain language of your chosing where as alt + t translates it back to the default language (in my case its arabic) and as a handy plus it shows u the original language of the text so if u want to communicate back all u have to do is remember the original language and type ur reply in the following format:
original language//Hello world!
than copy it, paste it and send it.
# How to install it
- DISCLAIMER : this script works only in linux. In order to use it elsewhere u need to alter the program, all u need to do is change the method with which u get the clipboard data since i used the terminal.
- download xclip using this command sudo apt install xclip (for ubunto users)
- download the used libraries googletrans 3.1 (i used this version because the latest one didn't work for me 4.0), pynput using pip install library_name
- run the code before u start the game and you are good to go.
