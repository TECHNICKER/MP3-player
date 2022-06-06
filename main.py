import os
import sys
from tkinter import N
import music_tag as mtg
import pygame as pg
from pygame import mixer as mx
from datetime import timedelta

subdirectory_scan_limit = 2
supported_formats = (".ogg", ".mp3", ".wav")
character_whitelist = set("0123456789")
volume = 0.5
play = False
pause = False
mute = False

pg.init()
pg.key.set_repeat(700, 100)
mx.init()
mx.music.set_volume(volume)

display = pg.display.set_mode((500, 200))
pg.display.set_caption("Music player")
icon = pg.image.load("logo/player.png")
pg.display.set_icon(icon)    


class Folder:

    playlist = []
    update_list =[]
    scanned_subdirectory_layers = 0

    def __init__(self, name, path):
        self.name = name
        self.path = path
        if path == "music":
            self.parent = None
        else:
            self.parent = os.path.dirname(self.path)
        self.subs_exist = False
        self.subs = []
        self.songs = []


    @classmethod
    def build_playlist(cls):

        Folder.playlist = Folder.f_music_files()
        Folder.playlist += Folder.f_directories()
 
        for object in Folder.playlist:
            if isinstance(object, Folder) == True:
                object.songs = Folder.f_music_files(object.path)
                object.subs = Folder.f_directories(object.path)



        # Folder.f_directories()
        # if len(Folder.playlist) != 0:
        #     for folder in Folder.playlist:
        #         Folder.f_sub_directories(folder)
        #         Folder.f_music_files(folder)
        # else:
        #     Folder.f_music_files(Folder("music", "music"))
        # return Folder.playlist
    


    
    @classmethod
    def f_directories(cls, dir = "music"):
        pass





        # for item in os.scandir(dir):
        #     if item.is_dir() == True and len(os.listdir(dir)) != 0:
        #         Folder.update_list.append(Folder(item.name, item.path))

    def f_sub_directories(self):
        self.songs = Folder.f_music_files(self.path)
        self.subs = Folder.f_directories(self.path)
        




        # for item in os.scandir(self.path):
        #     if item.is_dir() == True:
        #         self.subs.append(Folder(item.name, item.path))

        # if len(self.subs) != 0:
        #     self.subs_exist = True

    def f_music_files(self):



        pass




        # if self.subs_exist == False:

        #     for item in os.scandir(self.path):
        #         for format in supported_formats:
        #             if item.is_file() == True and item.name.endswith(format):
        #                 if self.path == "music":
        #                     Folder.update_list.append(Song(item.path))
        #                 else:
        #                     self.songs.append(Song(item.path))

        # elif Folder.scanned_subdirectory_layers <= subdirectory_scan_limit:
        #     for subdir in self.subs:
        #         for item in os.scandir(subdir.path):
        #             for format in supported_formats:
        #                 if item.is_file() == True and item.name.endswith(format):
        #                     subdir.songs.append(Song(item.path))
                            
        #     Folder.scanned_subdirectory_layers += 1


class Song:

    def __init__(self, path):
        self.path = path
        self.number = ""
        self.music_tag = mtg.load_file(self.path)
        self.length = timedelta(seconds = int(self.music_tag["#length"]))

        if path == "music":
            self.parent = None
        else:
            self.parent = os.path.dirname(self.path)

        if len(self.music_tag["tracktitle"]) >= 1:
            self.title  = self.music_tag["tracktitle"]
        else:
            self.title = os.path.splitext(os.path.basename(self.path))[0]

        if len(self.music_tag["albumartist"]) >= 1:
            self.artist = self.music_tag["albumartist"]
        else:
            self.artist = "Unknown artist"

        if len(self.music_tag["tracknumber"]) >= 1:
            self.number = self.music_tag["tracknumber"]
        else:
            for char in self.title:
                if char in character_whitelist:
                    self.number += char
            self.number = int(self.number)


x = Folder.build_playlist()
print(x)
# testovací printy - je možné vyzkoušet se "Sto chvalospevov"


# for folder in Folder.playlist:
    
#     print(folder.name)
#     print(folder.path)
#     print(folder.parent)
#     print(folder.subs)
#     for sub in folder.subs:
#         print(sub.name)
#         print(sub.path)
#         print(sub.parent)
#         print(sub.subs)
#         print(sub.songs)
#         for song in sub.songs:

#             print(song.title)
#             print(song.path)
#             print(song.parent)
#             print(song.artist)
#             print(song.length)
#             print(song.number)

#     for song in folder.songs:

#         print(song.title)
#         print(song.path)
#         print(song.parent)
#         print(song.artist)
#         print(song.length)
#         print(song.number)


# for song in Folder.playlist[0].songs: # pro Song class testing

#     print(song)

#     print(song.title)
#     print(song.path)
#     print(song.parent)
#     print(song.artist)
#     print(song.length)
#     print(song.number)

# pro jednu složku obsahující hudbu vloženou do music
# print(Folder.playlist[0])
# print(Folder.playlist[0].title)
# print(Folder.playlist[0].path)
# print(Folder.playlist[0].parent)
# print(Folder.playlist[0].artist)
# print(Folder.playlist[0].length)
# print(Folder.playlist[0].number)


# pro hudbu čistě ve složce music - tady budou velké změny
# print(Folder.playlist)

# pro jednu složku obsahující hudbu vloženou do music
# print(Folder.playlist[0])
# print(Folder.playlist[0].name)
# print(Folder.playlist[0].path)
# print(Folder.playlist[0].parent)
# print(Folder.playlist[0].subs)
# print(Folder.playlist[0].songs)


# x = Folder.playlist[0].length
# print (x)
# print(type(x))

# while x > timedelta(seconds = 0):
#     x -= timedelta(seconds = 1)
#     print(x)


# for i in range(8): # range = max. počet složek pokud vložíme do music složeky s písněmi 
#     print(Folder.playlist[i])
#     print(Folder.playlist[i].name)
#     print(Folder.playlist[i].path)
#     print(Folder.playlist[i].parent)
#     print(Folder.playlist[i].subs)
#     print(Folder.playlist[i].songs)

# for i in range (8): # range = max. číslo vnočených složek pokud vložíme do music složeku obsahující složky s písněmi
#     print(Folder.playlist[0].subs[i].name)
#     print(Folder.playlist[0].subs[i].path)
#     print(Folder.playlist[0].subs[i].parent)
#     print(Folder.playlist[0].subs[i].subs)
#     print(Folder.playlist[0].subs[i].songs)



def was_pressed(key, events):
    for event in events:
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and key == "SPACE":
                    return True

                elif event.key == pg.K_RETURN and key == "ENTER":
                    return True

                elif event.key == pg.K_n and key == "N":
                    return True

                elif event.key == pg.K_b and key == "B":
                    return True

                elif event.key == pg.K_k and key == "K":
                    return True

                elif event.key == pg.K_m and key == "M":
                    return True

                elif event.key == pg.K_l and key == "L":
                    return True

                elif event.key == pg.K_j and key == "J":
                    return True

                elif event.key == pg.K_h and key == "H":
                    return True
                
                elif event.key == pg.K_COMMA and key == "COMMA":
                    return True
        else:
            return False

# tady, a v ramci hlavni smycky, bude proper loading (+ preskakovani, apod.) system

# testovaci pisnicka
# mx.music.load("music/10 O, MOJ BOH.mp3")

while True:
    events = pg.event.get()
    # program exit_enable
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # play-stop
    if was_pressed("ENTER", events) == True:
        if play == False:
            mx.music.play()
            play = True
            pause = False

        elif play == True:
            mx.music.stop()
            play = False
            pause = False
    # pause-unpause
    elif was_pressed("SPACE", events) == True:
        if play == False and pause == False:
            mx.music.play()
            play = True

        elif pause == False:
            mx.music.pause()
            pause = True
            play = False

        elif pause == True:
            mx.music.unpause()
            pause = False
            play = True
    # mute-unmute
    elif was_pressed("M", events) == True:
        if mute == False:
            prev_volume = volume
            volume = 0
            mute = True
        
        elif mute == True:
            volume = prev_volume
            mute = False
    # volume up
    elif was_pressed("K", events) == True:
        volume += 0.05

        if volume > 1:
            volume = 1

        mute = False
        prev_volume = volume

    #volume down
    elif was_pressed("COMMA", events) == True:
        volume -= 0.05

        if volume < 0:
            volume = 0

    mx.music.set_volume(volume)

