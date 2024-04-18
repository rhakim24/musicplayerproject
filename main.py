import tkinter
from tkinter.ttk import Progressbar
import customtkinter
import pygame 
from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.title("Music Player")
root.geometry('400x480')
pygame.mixer.init() 

list_of_songs = ['music/goodnight!.wav', 'music/brazil.wav', 'music/calling after me.wav', 'music/m..wav']
list_of_covers = ['img/goodnight.jpg', 'img/brazil.jpg', 'img/TMTIO.jpg', 'img/m..jpg']
n = 0

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name[6:-4]
    song_name_label = tkinter.Label(text = stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.4, rely=.6)


def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(.3)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)

def threading():
    t1 = Thread(target=progress)
    t1.start()

def play_music():
    threading()
    global n
    current_song = n
    if n > 3:
        n = 0 
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album_cover(song_name, n)

    print('PLAY')
    n += 1
    

def skip_forward():
    play_music()

def skip_back():
    global n
    n -= 2
    play_music()

def volume(value):
    #print(value)
    pygame.mixer.music.set_volume(value)





#Buttons
play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5, rely= 0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2) #create skip forward button
skip_f.place(relx=0.71, rely= 0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2) #create skip back button
skip_b.place(relx=0.29, rely= 0.7, anchor=tkinter.CENTER) 

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210) #create skip back button
slider.place(relx=0.5, rely= 0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#871431', width=250)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

root.mainloop()
