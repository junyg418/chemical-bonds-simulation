import pygame

RED = (255,0,0)
BLUE = (0,103,163)
BLACK = (0,0,0)

jugiulpeo = {1: ('H', 2.2), 2: ('He', 0.0), 3: ('Li', 0.98), 4: ('Be', 1.57), 5: ('B', 2.04), 6: ('C', 2.55), 7: ('N', 3.04), 8: ('O', 3.44), 9: ('F', 3.98), 10: ('Ne', 0.0), 11: ('Na', 0.93), 12: ('Mg', 1.31), 13: ('Al', 1.61), 14: ('Si', 1.9), 15: ('P', 2.19), 16: ('S', 2.58), 17: ('Cl', 3.16), 18: ('Ar', 0.0), 19: ('K', 0.82), 20: ('Ca', 1.0)}
# 주기율표 원자번호:(원자기호, 전기 음성도)

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
        self.plustxt = atom_num_font.render(f'{jugiulpeo[self.plus_pw][0]}', True, BLACK)
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


class Hydro(Atom):
    def __init__(self, display, pos: tuple) -> None:
        super().__init__(display, 1, pos)
        self.plus_pw = 1
        self.minus = 1
