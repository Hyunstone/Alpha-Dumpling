import pygame
import time

screen_width = 1200
screen_heiht = 800
startImg = pygame.image.load("C:/Users/leehyunseok/Desktop/algo_team/Alpha-Dumpling/src/image/clickedStartIcon.png")
screen = pygame.display.set_mode((screen_width, screen_heiht))

class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.display.set_caption("Alpha Dumpling")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font('arial')

class Button():
    def __init__(self, img, x, y, buttonText='Button', onclickFunction = None, onePress=False):
        self.image = img
        self.x = x
        self.y = y
        self.onePress = onePress
        self.onclickFunction = onclickFunction
        self.alreadyPressed = False
        
        screen.blit(img, [x, y])
        
    
    
    def process(self):
        mousePos = pygame.mouse.get_pos()
        if (pygame.mouse.get_pressed(num_buttons=3)[0]) :
            #if self.onePress:
                
            if not self.alreadyPressed:
                self.onclickFunction()
                self.alreadyPressed = True
        else:
            self.alreadyPressed = False
def printhello():
        print("hello")

game = Game()

while game.running:    
    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
    
    startButton = Button(startImg, 20, 20, 'Button One (onePress)', printhello)
    startButton.process()
    pygame.display.update()

pygame.quit()