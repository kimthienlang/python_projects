import pygame
import random

class Particle:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = random.uniform(1.6, 4.8)
        self.height = random.uniform(9.6, 19.2)
        self.color = "#2596be"
        
        self.vel_x = 0
        self.vel_y = self.width * 2
    
    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        if self.pos_y > 600:
            self.pos_y = -10
            
    def show(self, window):
        pygame.draw.rect(window, self.color, (self.pos_x, self.pos_y, self.width, self.height))