import pygame

def wait_for_key(self):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYUP:
                waiting = False
                
def user_select():
    