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
fill = pg.transform.scale(pg.image.load("resources/images/fill.png"), (48, 48))

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
 
    pg.display.flip()