import sys
import pygame as pg

display = pg.display.set_mode((500, 200))
pg.display.set_caption("Music player")
icon = pg.image.load("resources/images/player.png")
pg.display.set_icon(icon)  

class Button:

    buttons = []
    fill = pg.transform.scale(pg.image.load("resources/images/fill.png"), (48, 48))

    def __init__(self, paths:tuple, coords:tuple, scale:tuple):
        self.path = paths[0]
        self.path_c = paths[1]
        self.coords = coords
        self.previous_state = False
        self.current_state = False

        self.surface = pg.transform.scale(pg.image.load(self.path), scale)
        self.surface_c = pg.transform.scale(pg.image.load(self.path_c), scale)

        self.rect = self.surface.get_rect(topleft = self.coords)

        display.blit(self.surface, self.coords)

        Button.buttons.append(self)


    def button_handling(self) -> bool: 
        if self.rect.collidepoint(pg.mouse.get_pos()) == True and pg.mouse.get_pressed(num_buttons = 3)[0] == True:
            self.current_state = True
        else:
            self.current_state = False

        if self.previous_state == False and self.current_state == True:
            self.previous_state = self.current_state
            display.blit(Button.fill, self.coords)
            display.blit(self.surface_c, self.coords)
            return True

        elif self.previous_state == True and self.current_state == False:
            self.previous_state = self.current_state
            display.blit(Button.fill, self.coords)
            display.blit(self.surface, self.coords)
            return False

        else:
            self.previous_state = self.current_state
            return False

# volume_icon = pg.transform.scale(pg.image.load("resources/images/volume.png"), (48, 48))

play_pause = Button(("resources/images/play_pause.png", "resources/images/play_pause_c.png"), (20, 20), (48, 48))
list = Button(("resources/images/list.png", "resources/images/list_c.png"), (20, 80), (48, 48))
forward = Button(("resources/images/forward.png", "resources/images/forward_c.png"), (20, 120), (48, 48))
backward = Button(("resources/images/backward.png", "resources/images/backward_c.png"), (20, 160), (48, 48))

while True:
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    for button in Button.buttons:
        button.button_handling()
 
    pg.display.flip()