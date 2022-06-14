import UI
import sys
import pygame as pg
from pygame import mixer as mx
import file_management as FM

pg.init()
mx.init()
display = pg.display.set_mode((500, 200))
pg.display.set_caption("Music player")
icon = pg.image.load("resources/images/player.png")
pg.display.set_icon(icon)  
clock = pg.time.Clock()
pg.font.init()
Consolas = pg.font.SysFont("Consolas", 20)

loaded_song_number = 0
song_playing = False
volume_value = 0.5
prev_volume = volume_value
play = False
pause = False
stop = False
mute = False
buttons = []
playlist = FM.Folder.build_playlist()

play_pause = UI.Button(("resources/images/play_pause.png", "resources/images/play_pause_c.png"), (10, 145), (48, 48))
stop = UI.Button(("resources/images/stop.png", "resources/images/stop_C.png"), (10, 97), (48, 48))
forward = UI.Button(("resources/images/forward.png", "resources/images/forward_c.png"), (10, 49), (48, 48))
backward = UI.Button(("resources/images/backward.png", "resources/images/backward_c.png"), (10, 1), (48, 48))
volume_up = UI.Button(("resources/images/volume+.png", "resources/images/volume+_c.png"), (450, 54), (48, 48))
volume_down = UI.Button(("resources/images/volume-.png", "resources/images/volume-_c.png"), (450, 102), (48, 48))
mute = UI.Button(("resources/images/mute.png", "resources/images/mute_c.png"), (450, 150), (48, 48), True)
# list = UI.Button(("resources/images/list.png", "resources/images/list_c.png"), (20, 80), (48, 48))

buttons.extend([play_pause, stop, forward, backward, volume_up, volume_down, mute])
fill = pg.transform.scale(pg.image.load("resources/images/fill.png"), (48, 48))
fill_big = pg.transform.scale(fill, (300, 100))


def debouncer(passed_button, method):
    global song_playing
    global loaded_song_number
    global play
    global pause
    global stop
    global volume_value
    global mute
    global prev_volume

    if passed_button.previous_state == False and passed_button.current_state == True:
        passed_button.previous_state = passed_button.current_state
        passed_button.active_surface = passed_button.surface_c

        if method == "play_pause":

            if play == False and (pause == False or stop == True):
                mx.music.play()
                play = True
                stop = False

            elif pause == False:
                mx.music.pause()
                pause = True
                play = False

            elif pause == True:
                mx.music.unpause()
                pause = False
                play = True

        elif method == "stop":
            
            if play == True or pause == True:
                mx.music.stop()
                play = False
                stop = True

        elif method == "forward":
            play = False
            if loaded_song_number + 1 > len(playlist) - 1:
                loaded_song_number = 0
            else:
                loaded_song_number += 1
            

        elif method == "backward":
            play = False
            if loaded_song_number - 1 < 0:
                loaded_song_number = len(playlist) - 1
            else:
                loaded_song_number -= 1

        elif method == "volume_up":
            volume_value += 0.05

            if volume_value > 1:
                volume_value = 1

            mute = False
            prev_volume = volume_value

        elif method == "volume_down":
            volume_value -= 0.05

            if volume_value < 0:
                volume_value = 0
        

    elif passed_button.previous_state == True and passed_button.current_state == False:
        passed_button.previous_state = passed_button.current_state
        passed_button.active_surface = passed_button.surface

    else:
        passed_button.previous_state = passed_button.current_state

def flip_flop(passed_button, method):

    global prev_volume
    global volume_value
    global mute

    if volume_value < 0.05:
        passed_button.active_surface = passed_button.surface_c
    else:
        passed_button.active_surface = passed_button.surface


    if passed_button.previous_state == False and passed_button.current_state == True and passed_button.flip_state != True:
        passed_button.previous_state = passed_button.current_state
        passed_button.active_surface = passed_button.surface
        passed_button.flip_state = True

        if method == "mute":
                volume_value = prev_volume


    elif passed_button.previous_state == False and passed_button.current_state == True and passed_button.flip_state == True:
        passed_button.previous_state = passed_button.current_state
        passed_button.active_surface = passed_button.surface_c
        passed_button.flip_state = False

        if method == "mute":
            prev_volume = volume_value
            volume_value = 0


    else:
        passed_button.previous_state = passed_button.current_state


while True:

    loaded_song = playlist[loaded_song_number]
    if play == False:
        mx.music.load(loaded_song.path)
    
    display.blit(fill_big, (100, 80))
    title = Consolas.render(loaded_song.title, False, (255, 255, 255))
    display.blit(title, (100, 80))
    pg.display.flip()
    
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    for button in buttons:
        button.button_handling()
        display.blit(fill, button.coords)
        display.blit(button.active_surface, button.coords)

        if button == buttons[0]:
            debouncer(button, "play_pause")
        
        elif button == buttons[1]:
            debouncer(button, "stop")

        elif button == buttons[2]:
            debouncer(button, "forward")

        elif button == buttons[3]:
            debouncer(button, "backward") 

        elif button == buttons[4]:
            debouncer(button, "volume_up")

        elif button == buttons[5]:
            debouncer(button, "volume_down")

        elif button == buttons[6]:
            flip_flop(button, "mute")

    mx.music.set_volume(volume_value)
    clock.tick(60)
    pg.display.flip()