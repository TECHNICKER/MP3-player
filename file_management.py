import os
import music_tag as mtg
from datetime import timedelta


class Folder:

    subdirectory_scan_limit = 3
    supported_formats = (".ogg", ".mp3", ".wav")

    update_list = []
    song_list = []
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
    def get_songs(cls, list):
        for object in list:
            if isinstance(object, Song) and object not in Folder.song_list:
                Folder.song_list.append(object)

            elif isinstance(object, Folder):
                Folder.sub_unpacking(object)

    def sub_unpacking(object):
        for song in object.songs:
            if song not in Folder.song_list:
                Folder.song_list.append(song)
        
        if object.subs_exist == True:
            for sub in object.subs:
                Folder.sub_unpacking(sub)

    @classmethod
    def build_playlist(cls):
        Folder.f_directories()
        if len(Folder.update_list) != 0:
            for folder in Folder.update_list:
                if isinstance(folder, Folder) == True:
                    Folder.f_sub_directories(folder)
                    Folder.f_music_files(folder)
        else:
            Folder.f_music_files(Folder("music", "music"))

        return Folder.update_list
        
    
    
    @classmethod
    def f_directories(cls, dir = "music"):
        for item in os.scandir(dir):
            if item.is_dir() == True and len(os.listdir(dir)) != 0:
                Folder.update_list.append(Folder(item.name, item.path))

    def f_sub_directories(self):
        for item in os.scandir(self.path):
            if item.is_dir() == True:
                self.subs.append(Folder(item.name, item.path))

        if len(self.subs) != 0:
            self.subs_exist = True


    def f_music_files(self):

        for item in os.scandir(self.path):
            for format in Folder.supported_formats:
                if item.is_file() == True and item.name.endswith(format):
                    if self.path == "music":
                        Folder.update_list.append(Song(item.path))
                    else:
                        self.songs.append(Song(item.path))                                                        

        if Folder.scanned_subdirectory_layers <= Folder.subdirectory_scan_limit:
            for subdir in self.subs:
                for item in os.scandir(subdir.path):
                    for format in Folder.supported_formats:
                        if item.is_file() == True and item.name.endswith(format):
                            subdir.songs.append(Song(item.path))
                            
            Folder.scanned_subdirectory_layers += 1


class Song:

    character_whitelist = set("0123456789")

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
            self.title  = str(self.music_tag["tracktitle"])
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
                if char in Song.character_whitelist:
                    self.number += char
            self.number = int(self.number)