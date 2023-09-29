#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:48:03 2023

@author: bekdouche
"""

import googletrans
import subprocess
from pynput import keyboard

# initiating a google translator
translator = googletrans.Translator()
# default language
default = 'ar'

# keybinds that activates the translating functions
cmb = [{keyboard.Key.ctrl, keyboard.KeyCode(char='t')},{keyboard.Key.alt, keyboard.KeyCode(char='t')}]
# set for keys that are being pressed
current = set()

# get the coppied text from the clipboard
def getClipboardData():
    # executes a terminal command to get it using xclip
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def translate(text,dest):
    src = translator.detect(text).lang
    new_text = translator.translate(text,dest,src).text
    return new_text

# set the clipboard coppied text to data
def setClipboardData(data):
    # executes a terminal command to set it using xclip
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def translate2Default():
    text = getClipboardData().decode('utf-8')
    src = translator.detect(text).lang
    data = src + "/--/" + translate(text, default)
    data = data.encode('utf-8')
    setClipboardData(data)

# translation format "destination//text", example : "eng//hello world"
def translate2Other():
    text = getClipboardData().decode('utf-8')
    dest1 = text.split("/--/")[0]
    text1 = text.split('/--/')[1]
    data = translate(text1, dest1).encode('utf-8')
    setClipboardData(data)

# detect a key being pressed
def on_press(key):
    # check if the keys being pressed are in the hotkey section
    if any([key in z for z in cmb]):
        current.add(key)
    # if a hotkey has been pressed do something
    if all(k in current for k in cmb[0]):
        translate2Other()
    elif all(k in current for k in cmb[1]):
        translate2Default()

# detect a key being released
def on_release(key):
    # remove keys from current to distinguish the current pressed keys from the others 
    if any([key in z for z in cmb]):
        current.remove(key)

# start monitoring the keyboard for inputs
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
    