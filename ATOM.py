import pygame
import math
# import main


RED = (255,0,0)
BLUE = (0,103,163)
YELLO = (255, 212, 0)
BLACK = (0,0,0)

jugiulpeo = {1: ('H', 2.2), 2: ('He', 0.0), 3: ('Li', 0.98), 4: ('Be', 1.57), 5: ('B', 2.04), 6: ('C', 2.55), 7: ('N', 3.04), 8: ('O', 3.44), 9: ('F', 3.98), 10: ('Ne', 0.0), 11: ('Na', 0.93), 12: ('Mg', 1.31), 13: ('Al', 1.61), 14: ('Si', 1.9), 15: ('P', 2.19), 16: ('S', 2.58), 17: ('Cl', 3.16), 18: ('Ar', 0.0), 19: ('K', 0.82), 20: ('Ca', 1.0)}
# 주기율표 원자번호:(원자기호, 전기 음성도)

selected_atom = 0

class Atom:
    '''
    원자 기본\n
    조건 : 바닥상태, 이온이 아닌 원자, 원자번호 20번까지\n
    -display : pygame.display
    -minus : 전자 개수\n
    -pos : tuple 형태 int값 x, y 형태
    '''
    def __init__(self, display, minus:int, pos:tuple) -> None:
        self.display = display

        self.plus_pw =  minus # 원자핵의 세기(원자번호)
        atom_num_font = pygame.font.SysFont("malgungothicsemilight", 16)
        self.plustxt = atom_num_font.render(f'{jugiulpeo[self.plus_pw][0]}', True, BLACK)
        self.minus = minus
        self.pos = pos
        self.color = RED

        self.Kradius = 20 # 1주기 전자 원자핵 주위 공전 거리
        self.Lradius = 60 # 2주기 전자 
        self.Mradius = 100 # 3주기 전자
        self.Nradius = 500 # 4주기 전자

        # self.minusCount()

    def minusCount(self) -> int:
        '''
        전자 껍질 별 원자 개수 연산
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
        # self.Kcnt, self.Lcnt, self.Mcnt, self.Ncnt = mins_value
        return mins_value


    def clickEvent(self, now_pos:tuple)->bool:
        '''
        원자 클릭시 나타나는 연산되는 이벤트
        '''
        self.x_pos, self.y_pos = self.pos
        self.now_x, self.now_y = now_pos

        self.sqx = (self.now_x-self.x_pos)**2
        self.sqy = (self.now_y-self.y_pos)**2

        if math.sqrt(self.sqx + self.sqy) < 10: # 피타고라스 정리 빗변 연산

            if self.display.get_at(self.pos) == RED:
                self.color = YELLO
                return True
            elif self.display.get_at(self.pos) == YELLO:
                self.color = RED
                return True
        return False


    def drawPlus(self):
        '''
        도형 그리는 함수
        '''
        pygame.draw.circle(self.display, self.color, self.pos, 10)
        self.display.blit(self.plustxt, self.pos)



class Hydro(Atom):
    '''
    수소일 떄 호출
    -minus : 1\n
    Todo:
        소수결합 연산
    '''
    def __init__(self, display, pos: tuple) -> None:
        super().__init__(display, 1, pos)
        self.plus_pw = 1
        self.minus = 1



class Bond:
    '''
    두 원자간 결합구조
    '''
    def __init__(self, display, atom_A, atom_B) -> None:
        self.display = display
        self.atom_A = atom_A
        self.atom_B = atom_B

        self.posCal()

    
    def posCal(self):
        '''
        원과 원의 둘래를 지나는 두 점의 길이의 최솟값을 반환하는 함수
        '''
        def graph(x):
            nonlocal x1,x2,tan0
            graphYval = tan0*(x-x1)+y1
            return graphYval
        x1, y1 = self.atom_A.pos
        x2, y2 = self.atom_B.pos

        dx = x1-x2
        dy = y1-y2
        tan0 = dy/dx

        bit = math.sqrt(dx**2 + dy**2)
        cos0 = dx/bit

        
        x_val = cos0*10 # 10은 원자의 반지름
        
        # if x1 < x2:
        atom_Ax = x1-x_val
        atom_Ay = graph(atom_Ax)

        atom_Bx = x2+x_val
        atom_By = graph(atom_Bx)

        # elif x1> x2:
        #     atom_Ax = x1-x_val
        #     atom_Ay = graph(atom_Ax)

        #     atom_Bx = x2+x_val
        #     atom_By = graph(atom_Bx)
        self.atom_A_pos, self.atom_B_pos = (atom_Ax, atom_Ay), (atom_Bx, atom_By)

        


    def drawBond(self):
        pygame.draw.line(self.display, BLACK, self.atom_A_pos, self.atom_B_pos)