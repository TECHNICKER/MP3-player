import UI
import sys
import pygame as pg

display = pg.display.set_mode((500, 200))
pg.display.set_caption("Music player")
icon = pg.image.load("resources/images/player.png")
pg.display.set_icon(icon)  

play_pause = UI.Button(("resources/images/play_pause.png", "resources/images/play_pause_c.png"), (20, 20), (48, 48))
list = UI.Button(("resources/images/list.png", "resources/images/list_c.png"), (20, 80), (48, 48))
forward = UI.Button(("resources/images/forward.png", "resources/images/forward_c.png"), (20, 120), (48, 48))
backward = UI.Button(("resources/images/backward.png", "resources/images/backward_c.png"), (20, 160), (48, 48))
mute = UI.Button(("resources/images/mute.png", "resources/images/mute_c.png"), (450, 160), (48, 48))
fill = pg.transform.scale(pg.image.load("resources/images/fill.png"), (48, 48))

# pg.mixer.init()
# pg.mixer.music.set_volume(0.5)
# pg.mixer.music.load("music/10 O, MOJ BOH.mp3")

while True:
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    for button in UI.Button.buttons:
        button.button_handling()
        display.blit(fill, button.coords)
        display.blit(button.active_surface, button.coords)

    # if play_pause.button_handling() == True:
    #     pg.mixer.music.play()
 
    pg.display.flip()