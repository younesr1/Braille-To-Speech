#!/usr/bin/python3

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
slow = True
myobj = gTTS(text=mytext, lang=language, slow=slow) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3") 
