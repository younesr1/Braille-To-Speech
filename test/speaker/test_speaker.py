#!/usr/bin/python3
import sys
sys.path.append("../../")
from lib.speech.speaker import Speaker

foo = Speaker(language="en")

foo.speak("this is a sentence")

foo.speak( "this is the continuation of a sentence")

foo.speak(" dsdsfsfsdfs")

foo.save("audio.mp3")
