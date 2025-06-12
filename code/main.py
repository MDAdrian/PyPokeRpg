from pygame import Clock

from config import COAST_PATH, CHARACTERS_PATH
from config import HOSPITAL_PATH
from config import WATER_PATH
from config import WORLD_PATH
from entities import Player, Character
from groups import AllSprites
from sprites import AnimatedSprite, Sprite
from support import *


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("PyPokeRpg")
        self.clock = Clock()

        # groups
        self.all_sprites = AllSprites()

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')
    
    def import_assets(self):
        self.tmx_maps = {
            'world': load_pygame(WORLD_PATH),
            'hospital': load_pygame(HOSPITAL_PATH)
        }
        self.overworld_frames = {
            'water': import_folder(WATER_PATH),
            'coast': coast_importer(24, 12, COAST_PATH),
            'characters': all_character_import(CHARACTERS_PATH)
        }
        

    def setup(self, tmx_map, player_start_pos):
        # terrain
        for layer in ['Terrain', 'Terrain Top']:        
            for x,y,surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
            
        # objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        # entities
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['pos'] == player_start_pos:
                    self.player = Player(
                        pos = (obj.x, obj.y),
                        frames= self.overworld_frames['characters']['player'],
                        groups= self.all_sprites,
                        facing_direction = obj.properties['direction'])

            else:
                Character(
                    pos = (obj.x, obj.y),
                    frames = self.overworld_frames['characters'][obj.properties['graphic']],
                    groups = self.all_sprites,
                    facing_direction = obj.properties['direction'])

        # water
        for obj in tmx_map.get_layer_by_name('Water'):
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    AnimatedSprite((x,y), self.overworld_frames['water'], self.all_sprites)
        
        # coast
        for obj in tmx_map.get_layer_by_name('Coast'):
            terrain = obj.properties['terrain']
            side = obj.properties['side']
            AnimatedSprite((obj.x, obj.y), self.overworld_frames['coast'][terrain][side], self.all_sprites)
            

    def run(self):
        while True:
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.all_sprites.update(dt)
            self.display_surface.fill("black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()