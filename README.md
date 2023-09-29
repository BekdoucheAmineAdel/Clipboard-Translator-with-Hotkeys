# Clipboard-Translator-with-Hotkeys
# History
A python project i was interested in doing for in-Game chat (League of Legends). Basically u press a hot key and the selected text gets translated.
# How to install it
- DISCLAIMER : this script works only in linux. In order to use it elsewhere u need to alter the program, all u need to do is change the method with which u get the clipboard data since i used the terminal.
- download xclip using this command sudo apt install xclip (for ubunto users)
- download the used libraries googletrans 3.1 (i used this version because the latest one didn't work for me 4.0), pynput using pip install library_name
- run the code before u start the game and you are good to go.

# How to use it
1. Copy some txt (shortcut ctrl + c)
2. Press
  -ctrl + t: if u want to translate the txt to a specific language
     *Note the txt syntax must be as follows : lang/--/txt
     *The introduction of the lang/--/ is necessary for the code to know which specific language u want the translation to be in.
     *Language is coded in specific abreviations for example english is written as en/--/txt
  -alt + t: if u want to translate the txt to a default language in my case its arabic if u want to change it just modify the string default
     *You will notice that the previous lang/--/ will be introduced into the translated txt to tell you which is the original language of the txt before it got translated which is really handy in communicating.
4. Paste the txt (shortcut ctrl + v)
