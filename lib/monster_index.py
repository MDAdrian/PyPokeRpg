import pygame

from lib.settings import WINDOW_WIDTH, WINDOW_HEIGHT


class MonsterIndex:
    def __init__(self, monsters, fonts):
        self.display_surface = pygame.display.get_surface()
        self.monsters = monsters
        self.fonts = fonts

        # tint surf
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)

    def update(self, dt):
        # get input
        self.display_surface.blit(self.tint_surf, (0, 0))
        # tint
        # display the list
        # display the main section