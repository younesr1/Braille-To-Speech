#!/usr/bin/python3
from gtts import gTTS as gspeak

class Speaker:
    # language: IETF language tag
    def __init__(self, language, slow=True) :
        self.language = language
        self.slow = slow
        self.msg = ""

    def speak(self, sentence) :
        self.msg += sentence

    def save(self, file) :
        out = gspeak(text=self.msg, lang=self.language, slow=self.slow)
        out.save(file)
        self.msg = ""
