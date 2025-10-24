import pygame
from pygame import Vector2 as vector

from lib.settings import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS


class MonsterIndex:
    def __init__(self, monsters, fonts):
        self.display_surface = pygame.display.get_surface()
        self.monsters = monsters
        self.fonts = fonts

        # tint surf
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)

        # dimensions
        self.main_rect = pygame.FRect(0,0, WINDOW_WIDTH * 0.6, WINDOW_HEIGHT * 0.8).move_to(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # list of monsters
        self.visible_items = 6 # show number of monsters
        self.list_width = self.main_rect.width * 0.3
        self.item_height = self.main_rect.height / self.visible_items

    def display_list(self):
        for index, monster in self.monsters.items():
            top = self.main_rect.top + index * self.item_height
            item_rect = pygame.FRect(self.main_rect.left, top, self.list_width, self.item_height)

            text_surf = self.fonts['regular'].render(monster.name, False, COLORS['white'])
            text_rect = text_surf.get_rect(midleft = item_rect.midleft + vector(90, 0))

            pygame.draw.rect(self.display_surface, 'red', item_rect)
            self.display_surface.blit(text_surf, text_rect)

    def update(self, dt):
        # get input
        self.display_surface.blit(self.tint_surf, (0, 0))
        pygame.draw.rect(self.display_surface, 'black', self.main_rect)
        # tint
        self.display_list()
        # display the main section