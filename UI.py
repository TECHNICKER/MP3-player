import pygame as pg

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
        self.active_surface = self.surface

        self.rect = self.surface.get_rect(topleft = self.coords)

        Button.buttons.append(self)


    def button_handling(self) -> bool: 
        if self.rect.collidepoint(pg.mouse.get_pos()) == True and pg.mouse.get_pressed(num_buttons = 3)[0] == True:
            self.current_state = True
        else:
            self.current_state = False

        if self.previous_state == False and self.current_state == True:
            self.previous_state = self.current_state
            self.active_surface = self.surface_c
            return True

        elif self.previous_state == True and self.current_state == False:
            self.previous_state = self.current_state
            self.active_surface = self.surface
            return False

        else:
            self.previous_state = self.current_state
            return False