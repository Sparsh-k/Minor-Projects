import tkinter as tk
from compressmodule import compression,decompression
from tkinter import filedialog
window=tk.Tk()

def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title='Choose a file to be compressed')
    return filename
def compressor(i,o):
    compression(i,o)

def decompressor(i,o):
    decompression(i,o)

## For compression
input_entry=tk.Entry(window)
output_entry=tk.Entry(window)
input_label=tk.Label(window,text='Enter the file to be compressed')
output_label=tk.Label(window,text='Name of the compressed file   ')
compress_button=tk.Button(window,text='COMPRESS',command=lambda:compressor(input_entry.get() or open_file(),output_entry.get()))
browsefile_button_compression=tk.Button(window,text='Browse File..',command=lambda:open_file())

## For decompression
input2_entry=tk.Entry(window)
output2_entry=tk.Entry(window)
input2_label=tk.Label(window,text='Enter the file to be decompressed')
output2_label=tk.Label(window,text="Name the decompressed file     ")
decompress_button=tk.Button(window,text='Decompress',command=lambda:decompressor(input2_entry.get(),output2_entry.get()))
browsefile_button_decompression=tk.Button(window,text='Browse file..',command=lambda:open_file())

## Layout Compression
input_label.grid(row=0, column=0,)
input_label.config(bg='grey')
input_entry.grid(row=0, column=1)
output_label.grid(row=1, column=0)
output_label.config(bg='grey')
output_entry.grid(row=1, column=1)
compress_button.grid(row=2, column=1)
compress_button.config(bg='black',fg='white')
browsefile_button_compression.grid(row=0, column=2)
browsefile_button_compression.config(bg='black',fg='white')

## Layout decompression
input2_label.grid(row=3, column=0)
input2_label.config(bg='grey')
input2_entry.grid(row=3, column=1)
output2_label.grid(row=4,column=0)
output2_label.config(bg='grey')
output2_entry.grid(row=4,column=1)
decompress_button.grid(row=5, column=1)
decompress_button.config(bg='black',fg='white')
browsefile_button_decompression.grid(row=3, column=2)
browsefile_button_decompression.config(bg='black',fg='white')

## Window Settings
window.config(bg='grey')
window.title("Compressor")
window.geometry("600x400")
window.mainloop()
