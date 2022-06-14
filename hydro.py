import pygame

RED = (255,0,0)
BLUE = (0,103,163)
BLACK = (0,0,0)


class Atom:
    '''
    원자 기본\n
    -minus : 전자 개수\n
    조건 : 바닥상태, 이온이 아닌 원자, 원자번호 20번까지
    '''
    def __init__(self, display, minus:int, pos:tuple) -> None:
        self.display = display

        self.plus_pw =  minus # 원자핵의 세기(원자번호)
        atom_num_font = pygame.font.SysFont("malgungothicsemilight", 16)
        self.plustxt = atom_num_font.render(f'{self.plus_pw}', True, BLACK)
        self.minus = minus
        self.plusPos = pos

        self.Kradius = 20 # 1주기 전자 원자핵 주위 공전 거리
        self.Lradius = 60 # 2주기 전자 
        self.Mradius = 100 # 3주기 전자
        self.Nradius = 500 # 4주기 전자

        self.minusCount()

    def minusCount(self) -> int:
        '''
        전자 주기별 개수 분류
        '''
        mins_value = [0,0,0,0] # 원자 주기
        cnt = 0
        for _ in range(self.minus):
            if cnt <= 2:
                mins_value[0] += 1
                cnt += 1
            elif cnt <= 10:
                mins_value[1] += 1
                cnt += 1
            elif cnt <= 18:
                mins_value[2] += 1
                cnt += 1
            else:
                mins_value[3] += 1
                cnt += 1
        self.Kcnt, self.Lcnt, self.Mcnt, self.Ncnt = mins_value

    def drowPlus(self):
        # self.display.fill(128,128,128)
        pygame.draw.circle(self.display, RED, self.plusPos, 10)
        self.display.blit(self.plustxt, self.plusPos)

# print(pygame.font.get_fonts)