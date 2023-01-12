import pygame
from settings import *

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura',player.rect.center,groups)
            self.animation_player.create_particles('heal',player.rect.center + pygame.math.Vector2(0,-60),groups)

    def flame(self,player,cost,groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.stats.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.stats.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.stats.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)

            for i in range(1,6):
                if direction.x: # horizontal
                    offset_x = 
                else: # vertical
                    pass