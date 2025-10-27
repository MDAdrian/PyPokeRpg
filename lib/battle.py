import pygame


class Battle:
    def __init__(self, player_monsters, opponent_monsters, monster_frames, bg_surface, fonts):
        self.display_surface = pygame.display.get_surface()
        self.bg_surface = bg_surface
        self.monster_frames = monster_frames
        self.fonts = fonts
        self.monster_data = {
            'player': player_monsters,
            'opponent_monsters': opponent_monsters,
        }

    def update(self, dt):
        self.display_surface.blit(self.bg_surface, (0,0))
