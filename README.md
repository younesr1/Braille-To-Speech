# Braille To Speech

This project was developed over the course of 2 days as part of the Hack The North hackathon.

## Input
Image of braille (letter, word, or sentence)

## Output
Audio recording of the words being spoken

## Process
The incoming image is processed through a Julia script and converted to a 3x2 logical matrix where dark spots are 1 and blanks are 0s.
The logical matrix is converted to a letter through a simple lookup table.
Finally, the letters are collected and output as audio using Google's Text-To-Speech API

## Limitations
The images must be normal to the braille
The software sometimes fails in unexpected ways
