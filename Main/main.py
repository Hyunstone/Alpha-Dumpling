import pygame
import time
import threading
import random
import sys
sys.path.append('')
from Algorithm.Synergy import Synergy
from Algorithm.algorithm import *

# 일반 버튼 클래스
class Button():
    
    # 인자로 받는 값:
    # 버튼 x, y 좌표 | 버튼 길이, 너비 | 텍스트 x, y 좌표 | 텍스트 | 클릭 시 실행할 함수 | 버튼 이미지 
    def __init__(self, x, y, width, height, text_x, text_y, buttonText = 'Button', onclickFunction = None, onePress = False, buttonImage = None):
        
        # 버튼 x, y좌표
        self.x = x
        self.y = y

        # 버튼 길이, 너비
        self.width = width
        self.height = height

        # 텍스트 x, y좌표
        self.text_x = text_x
        self.text_y = text_y

        # 버튼을 눌렀을 때 실행될 함수
        self.onclickFunction = onclickFunction

        # 커서의 위치
        mouse = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pos()

        # 클릭 여부
        # click = pygame
        click = pygame.mouse.get_pressed()

        # 버튼 
        self.buttonSurface = pygame.Surface((self.width, self.height))

        # 네모 모양
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        # 텍스트
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        # 버튼 색 (일반/커서가 위에 있을 때/버튼이 눌렸을 때)
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        # 버튼 이미지
        self.buttonImage = buttonImage
        

        # (1) 마우스가 버튼 안에 있을 때
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            # 버튼 색 변경
            self.buttonSurface.fill(self.fillColors['hover'])
            screen.blit(self.buttonSurface, (x, y))

            if self.buttonImage is None:
                screen.blit(self.buttonSurf, (self.text_x, self.text_y))
            else:
                screen.blit(self.buttonImage, (self.x, self.y))
                
            # (2) 마우스가 버튼 안에서 클릭되었을 때
            if click[0] and onclickFunction is not None:
                # 버튼 색 변경
                self.buttonSurface.fill(self.fillColors['pressed'])
                time.sleep(0.2)
                
                # 클릭 함수 실행
                print(onclickFunction)
                onclickFunction()

                
        # (3) 마우스가 버튼 안에 있지 않을 때
        else:
            # 버튼 색 변경
            self.buttonSurface.fill(self.fillColors['normal'])
            screen.blit(self.buttonSurface, (x, y))
            if self.buttonImage is None:
                screen.blit(self.buttonSurf, (self.text_x, self.text_y))
            else:
                screen.blit(self.buttonImage, (self.x, self.y))

# 메인 게임화면 상에 나오는
# 재료 선택 버튼 클래스
class ingredient_button():

    # 인자로 받는 값:
    # 버튼 x, y 좌표 | 버튼의 길이, 너비 | 재료 번호 
    def __init__(self, x, y, width, height, buttonIndex = 0, onePress = False):

        # 버튼 x, y 좌표
        self.x = x
        self.y = y

        # 버튼 길이, 너비
        self.width = width
        self.height = height

        # 재료 번호
        self.buttonIndex = buttonIndex

        # 커서의 위치
        self.mouse = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pos()
        
        # 클릭 여부
        #click = pygame
        click = pygame.mouse.get_pressed()
            
        # 버튼 표면
        self.buttonSurface = pygame.Surface((self.width, self.height))

        # 네모 모양
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        # 버튼 텍스트
        self.buttonSurf = font.render(str(buttonIndex), True, (20, 20, 20))

        # 버튼 색(일반 / 커서가 버튼 위에 있을 때 / 커서를 눌렀을 때)
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        
        index = 0
        
        

        # 해당 재료를 user 또는 robot이 이미 선택했을 때
        
        if (buttonIndex in total_ingredient):

            # 버튼 색 변경
            self.buttonSurface.fill((0, 0, 0))
            screen.blit(self.buttonSurface, (x, y))
            screen.blit(self.buttonSurf, (self.x + 15, self.y + 10))

        # 해당 재료를 user 또는 robot이 아직 선택하지 않았을 때
        else:

            # (1) 마우스가 버튼 안에 있을 때
            if x + width > mouse[0] > x and y + height > mouse[1] > y:

                # 버튼 색 변경
                self.buttonSurface.fill(self.fillColors['hover'])
                screen.blit(self.buttonSurface, (x, y))  # 버튼 이미지 변경
                screen.blit(self.buttonSurf, (self.x + 40, self.y + 10))

                # (2) 마우스가 버튼 안에서 클릭되었을 때
                if click[0]:

                    # 버튼 색 변경
                    self.buttonSurface.fill(self.fillColors['pressed'])
                    screen.blit(self.buttonSurf, (self.x + 40, self.y + 10))
                    
                    # user가 선택한 재료를 리스트에 추가
                    ingredient_user.append(buttonIndex)
                    total_ingredient.append(buttonIndex)
                        
                    # 유저가 처음 선택했을때 시너지DP를 만듭니다
                    if (len(ingredient_user) == 1):
                        firstSynergyList = Synergy.getSynergyList()
                        firstSynergyList.remove(buttonIndex)
                        botRandomChoice = random.choice(firstSynergyList)
                        initSynergy(botRandomChoice, ingredient_robot)
                        print(botRandomChoice)
                    else:
                        botSelect = Greedy()
                        ingredient_robot.append(botSelect)
                        total_ingredient.append(botSelect)
                        updateDP(index, botSelect, total_ingredient)
                    print(ingredient_user)
                    print(ingredient_robot)
                            
                   
                    time.sleep(0.2)
                    
            # (3) 마우스가 버튼 안에 있지 않을 때      
            else:

                # 버튼 색 변경
                self.buttonSurface.fill(self.fillColors['normal'])
                screen.blit(self.buttonSurface, (x, y))
                screen.blit(self.buttonSurf, (self.x + 40, self.y + 10))


#--------------------------
# 게임시작 전 초기화
#--------------------------

# pygame 라이브러리 초기화 (안하면, 일부 기능 사용 불가)
pygame.init()

# 화면 크기 설정
screen_width = 1000
screen_height = 562

# 화면 세팅
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀 설정
title = "Alpha Dumpling"
pygame.display.set_caption(title)

# 배경 이미지 로딩
background = pygame.image.load("image/Japanese Alley, Anastasia Ermakova.png")

# 폰트 설정
font = pygame.font.SysFont('Arial', 40)

# 재료 선택 리스트 초기화
global ingredient_user
ingredient_user = []

global ingredient_robot
ingredient_robot = []

# 봇의 선택 제약을 위한 리스트
global total_ingredient 
total_ingredient = []

# 유저의 재료 선택 개수
global userSelectCount
userSelectCount = 0

maxSelectCount = 4

#--------------------------
# 캐릭터 로딩 및 세팅
#--------------------------

global ajussi
global robot


# [1] 유저(아저씨) 캐릭터 로딩

ajussi = pygame.image.load("image/testimage.png")

# 캐릭터 이미지 사이즈 구하기
ajussi_size = ajussi.get_rect().size 
ajussi_width = ajussi_size[0]
ajussi_height = ajussi_size[1]

# 캐릭터 이미지 사이즈 조절
ajussi = pygame.transform.scale(ajussi, (ajussi_width * 0.9, ajussi_height * 0.9))

# 캐릭터 x, y 좌표 설정
ajussi_x_pos = (screen_width / 2) + 100
ajussi_y_pos = screen_height - ajussi_height + 100



# [2] 로봇 캐릭터 로딩

robot = pygame.image.load("image/robot.png")

# 캐릭터 이미지 사이즈 구하기
robot_size = robot.get_rect().size
robot_width = robot_size[0]
robot_height = robot_size[1]

# 캐릭터 이미지 사이즈 조절
robot = pygame.transform.scale(robot, (robot_width * 1, robot_height * 1))

# 캐릭터 x, y 좌표 설정
robot_x_pos = 0
robot_y_pos = screen_height - robot_height


global running_menu
global running_info
global running_game
    

#--------------------------
# 메인 게임 로딩 화면 로딩
#--------------------------

# 로딩 화면 이미지
loading_images = ["image/loading1.png", "image/loading2.png", "image/loading3.png", "image/loading4.png", "image/loading5.png"]

def loading():
    for loading_image in loading_images:
        screen.fill((0,0,0))
        loading_image = pygame.image.load(loading_image)
        screen.blit(loading_image, (280, 150))
        pygame.display.flip()
        time.sleep(0.2)
    game()
    
    
#-----------------
# 게임 화면 로딩
#-----------------

def game():

    # 텍스트 설정
    text_robot= font.render("Alpha", True, [0,0,0])
    text_ajussi= font.render("Ajussi", True, [0,0,0])

    # 재료 버튼 y 좌표 설정
    ingredient_line1_y_pos = 370
    ingredient_line2_y_pos = 470

    # 배경화면 설정
    game_background = pygame.image.load("image/game_background.png")

    # 돌아가기 버튼 설정
    home_button = pygame.image.load("image/home.png")
    
    running_game = True
    while running_game:
        for event in pygame.event.get():

            # 창을 닫는 이벤트가 발생하였을 때
            if event.type == pygame.QUIT:
                running_menu = False # 종료
                
        if userSelectCount == maxSelectCount:
            userScore = sumSynergy(ingredient_user)
            botScore = sumSynergy(ingredient_robot)
            if (userScore >  botScore):
                win()
            lose()

        # 화면 설정
        screen.fill((0,0,0)) # 배경화면 칠하기
        screen.blit(game_background, (0,0)) # 배경화면 로드
        screen.blit(text_robot, [20, 20]) # 텍스트 로드
        screen.blit(text_ajussi, [900, 20]) # 텍스트 로드
        pygame.draw.line(screen, (0,0,0), [500, 0], [500,350], 5) # 가운데 선 로드
        Button(475, 0, 50, 50, 0, 0, onclickFunction=menu, buttonImage = home_button) # 홈버튼 로

        # 재료 버튼 로드 (1번-5번)
        ingredient_button(83, ingredient_line1_y_pos, 100, 70, "MINT_CHOCOLATE")
        ingredient_button(266, ingredient_line1_y_pos, 100, 70, "SESAME_OIL")
        ingredient_button(449, ingredient_line1_y_pos, 100, 70, "KOCHUJANG")
        ingredient_button(632, ingredient_line1_y_pos, 100, 70, "MAYONNAISE")
        ingredient_button(815, ingredient_line1_y_pos, 100, 70, "SOJU")

        # 재료 버튼 로드 (6번-10번)
        ingredient_button(83, ingredient_line2_y_pos, 100, 70, "CHEESE")
        ingredient_button(266, ingredient_line2_y_pos, 100, 70, "GALIC")
        ingredient_button(449, ingredient_line2_y_pos, 100, 70, "ONION")
        ingredient_button(632, ingredient_line2_y_pos, 100, 70, "JUICE")
        ingredient_button(815, ingredient_line2_y_pos, 100, 70, "WATER")

        # 화면 업데이트
        pygame.display.flip()
        

#-----------------
# 설명 화면 로딩
#-----------------

def info():

    # 타이틀 설정
    font_title = pygame.font.SysFont('Arial', 80)
    text = font_title.render("Alpha Dumpling", True, (0,0,0))

    # 돌아가기 버튼 설정
    home_button = pygame.image.load("image/home.png")
    
    running_info = True
    while running_info:
        for event in pygame.event.get():

            # 창을 닫는 이벤트가 발생하였을 때
            if event.type == pygame.QUIT:
                running_menu = False # 종료

        # 화면 설정
        screen.blit(background, (0,0)) # 배경 화면 이미지 로드
        screen.blit(text, (300,0)) # 타이틀 로드
        pygame.draw.rect(screen, (0, 0, 0), [250, 50, 500, 500], 400) # 사각형 로드
        Button(250, 50, 50, 50, 0, 0, onclickFunction = menu, buttonImage = home_button)
        
        # 화면 업데이트
        pygame.display.flip()
        

#-----------------
# 메뉴 화면 로딩
#-----------------

def menu():

    # 타이틀 설정
    font_title = pygame.font.SysFont('Arial', 80)
    text = font_title.render("Alpha Dumpling", True, (0,0,0))

    running_menu = True
    while running_menu:
        for event in pygame.event.get():

            # 창을 닫는 이벤트가 발생하였을 때
            if event.type == pygame.QUIT:
                running_menu = False # 종료

        # 화면 설정
        screen.fill((0, 0, 0)) # 배경 화면 칠하기
        screen.blit(background, (0, 0)) # 배경 화면 이미지 로드
        screen.blit(ajussi, (ajussi_x_pos, ajussi_y_pos)) # user(아저씨) 캐릭터 로드
        screen.blit(robot, (robot_x_pos, robot_y_pos)) # robot 캐릭터 로드
        Button(300, 200, 400, 100, 410, 230, 'Game Start', onclickFunction = loading) # 시작 버튼 로드
        Button(300, 350, 400, 100, 365, 380, 'Game Information', onclickFunction = info) # 설명 버튼 로드
        screen.blit(text, (300,0)) # 타이틀 로드

        # 화면 업데이트
        pygame.display.flip()
        

#------------------
# 인트로 화면 로딩
#------------------

# 인트로 사진
intro_images = ["image/intro1.png", "image/intro2.png", "image/intro3.png", "image/intro4.png", 
                "image/intro5.png", "image/intro6.png", "image/intro7.png", "image/intro8.png"]

def intro():
    for intro_image in intro_images:
        intro_image = pygame.image.load(intro_image)
        screen.blit(intro_image, (280, 150))
        pygame.display.flip()
        time.sleep(0.5)
    menu()

#------------------
# 승리 화면 로딩
#------------------

# 인트로 사진
win_images = ["image/win.jpg", "image/win2.jpg"]

def win():
    for win_image in win_images:
        screen.blit(win_image, (0,0))
        pygame.display.flip()
        time.sleep(5)

#------------------
# 패배 화면 로딩
#------------------

# 인트로 사진
lose_images = ["image/lose.jpg", "image/lose2.jpg"]

def lose():
    for lose_image in lose_images:
        screen.blit(lose_image, (0,0))
        pygame.display.flip()
        time.sleep(0.2)



# 메뉴 화면으로 게임 시작
intro()

# pygame 종료
pygame.quit()
