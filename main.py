import sys
import pygame
from pygame.locals import *
import hydro

WHITE = (255,255,255)
GRAY = (128,128,128)
BLACK = (0,0,0)

pygame.init()

size = (1080,700)
FPS = 100
FramePerSec = pygame.time.Clock()
GameDisplay = pygame.display.set_mode(size)
GameDisplay.fill(GRAY)
pygame.display.set_caption("Bond simulation")

info_font = pygame.font.SysFont("malgungothicsemilight", 16)
atom_select = 1 # 원자번호 : defult 수소원자

def simulationRun():
    global atom_select
    atom_list = [] # fill 하고 난 후 리스트 for 문으로 전부 drow -> 원자번호 삭제됨  
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT: # x 버튼 눌렀을 떄
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP: # 마우스 클릭시 원자 생성
                mouse_pos = pygame.mouse.get_pos()
                if atom_select == 1:
                    pass # 수소 원자 생성
                    #hydro
                else:
                    atom = hydro.Atom(GameDisplay, atom_select, mouse_pos) # 원자 인스턴트 생성
                    atom.drowPlus()
                    atom_list.append(atom)
            if event.type == KEYDOWN: # 원자번호 설정 - k
                if event.key == K_k:
                    atom_select = atomNumInput()

def atomNumInput():
    '''
    원자번호 설정 입력함수
    k 로 실행
    숫자 입력
    Enter 로 반환
    '''
    atom_num = ''
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_0 or event.key == K_KP0:
                    atom_num = atom_num + '0'
                elif event.key == K_1 or event.key == K_KP1:
                    atom_num = atom_num + '1'
                elif event.key == K_2 or event.key == K_KP2:
                    atom_num = atom_num + '2'
                elif event.key == K_3 or event.key == K_KP3:
                    atom_num = atom_num + '3'
                elif event.key == K_4 or event.key == K_KP4:
                    atom_num = atom_num + '4'
                elif event.key == K_5 or event.key == K_KP5:
                    atom_num = atom_num + '5'
                elif event.key == K_6 or event.key == K_KP6:
                    atom_num = atom_num + '6'
                elif event.key == K_7 or event.key == K_KP7:
                    atom_num = atom_num + '7'
                elif event.key == K_8 or event.key == K_KP8:
                    atom_num = atom_num + '8'
                elif event.key == K_9 or event.key == K_KP9:
                    atom_num = atom_num + '9'
                elif event.key == K_RETURN: # ENTER 눌렀을 때 
                    return int(atom_num)

        GameDisplay.fill(GRAY)
        atom_text = info_font.render(f'atomNum : {atom_num}', True, BLACK)
        GameDisplay.blit(atom_text, (10,0))
simulationRun()