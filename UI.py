import pygame as pg

class Button:

    def __init__(self, paths:tuple, coords:tuple, scale:tuple, flip = False):
        self.path = paths[0]
        self.path_c = paths[1]
        self.coords = coords
        self.previous_state = False
        self.current_state = False
        self.flip_state = flip

        self.surface = pg.transform.scale(pg.image.load(self.path), scale)
        self.surface_c = pg.transform.scale(pg.image.load(self.path_c), scale)
        self.active_surface = self.surface

        self.rect = self.surface.get_rect(topleft = self.coords)


    def button_handling(self): 
        if self.rect.collidepoint(pg.mouse.get_pos()) == True and pg.mouse.get_pressed(num_buttons = 3)[0] == True:
            self.current_state = True
        else:
            self.current_state = False
            