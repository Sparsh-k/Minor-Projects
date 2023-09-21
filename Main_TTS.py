from gtts import gTTS
import os
import tkinter as tk
from tkinter import *

root=tk.Tk()
canvas= Canvas(root,width=400, height=300 )
canvas.pack()

entry=Entry(root)
canvas.create_window(200,100, window=entry)

def TextToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')

button= Button(text="Start", command=TextToSpeech)
canvas.create_window(200,230, window=button)

root.mainloop()
