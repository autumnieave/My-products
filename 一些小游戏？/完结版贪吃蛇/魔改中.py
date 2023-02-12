#基本内容
import pygame
import random
import PySimpleGUI as sg
import time
#初始化pygame
pygame.init()
pygame.mixer.init()

#颜色参数
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (160, 32, 240)
grey = (128,128,128)
orange = (255,153,51)
#屏幕大小参数
dis_width = 700
dis_height = 500

#音乐
eat_music = pygame.mixer.Sound("eat.wav")
end_music = pygame.mixer.Sound("end.wav")
start_music = pygame.mixer.Sound("start.wav")
break_music = pygame.mixer.Sound("break.wav")
speed1 = pygame.mixer.Sound("speed1.wav")
speed2 = pygame.mixer.Sound("speed2.wav")
#屏幕大小设置
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('贪吃蛇小游戏')


#帧数设置
clock = pygame.time.Clock()

#字体参数设置
font_style = pygame.font.SysFont(['华文宋体', "bahnschrift"], 25)
score_font = pygame.font.SysFont('华文宋体', 35)
lost_style = pygame.font.SysFont('华文宋体', 50)

a = pygame.font.get_fonts()

#速度输出函数
def Your_speed(speed):
    s = score_font.render("你的速度：{}".format(speed),True,red)
    dis.blit(s,[400,0])
    pygame.display.update()


#得分输出函数
def Your_score(score):
    value = score_font.render("你的分数：" + str(score), True, blue)
    dis.blit(value, [0, 0])
    pygame.display.update()

#消息输出函数
def message(msg, color, ft, pos):
    mesg = ft.render(msg, True, color)
    dis.blit(mesg, pos)

hard=1.2
bool=False
def start():
    sg.theme("SystemDefault")
    layout=[[sg.Text("         贪吃蛇小游戏",font=("微软雅黑",50))],
            [sg.Text()],
            [sg.Text("               ",font=("微软雅黑",40)),sg.Button("开始游戏",font=("微软雅黑",40))],
            [sg.Text()],
            [sg.Text("                ",font=("微软雅黑",40)),sg.Button("  备注  ",font=("微软雅黑",40))],
            [sg.Text()],
            [sg.Text("                ",font=("微软雅黑",40)),sg.Button("  退出  ",font=("微软雅黑",40))]]
    window=sg.Window("开始",layout,size=(800,600))
    while True:
        event,values=window.read()
        if event in(None,"  退出  "):
            exit()
        if event in ("开始游戏"):
            bool=True
            break
        if event in ("  备注  "):
            sg.Print("游戏有四种颜色的食物，且每过一段时间会生成新的食物：")
            sg.Print("1.绿色：分数加1，无特殊变化")
            sg.Print("2.紫色：分数加2，但长度加2")
            sg.Print("3.蓝色：分数加1，速度增加")
            sg.Print("4.橙色：分数加1，速度降低")
            sg.Print("基础操作：键盘的上下左右键控制运动")
            sg.Print("注意：此为成人版，请小心游玩")
    window.close()
    return bool


class Snake:

    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
        self.block=5
        self.speed=10 
        self.length=1
        self.List=[]
        self.Head=[]
    def our_snake(self,game_close,x1,y1,block,snake_list):
        if(game_close==False):
            if(60<=y1<=460):
                pygame.draw.rect(dis, black, [x1, y1, block, block])
                for x in snake_list[1:-1]:
                    pygame.draw.rect(dis, grey, [x[0], x[1], block, block])
                pygame.display.update()

class Food:
    def __init__(self,snake_block,snake,list):
        same=False
        c_s = 0
        self.foodx = round(random.randrange(70, dis_width - snake_block-60) / 10.0) * 10.0
        self.foody = round(random.randrange(70, dis_height - snake_block-60) / 10.0) * 10.0
        for i in snake.List:
            if i==[self.foodx,self.foody]:
                same=True
        self.type=random.randint(0,3)
        for i in list:
            if pow(pow((i[0]-self.foodx),2)+pow((i[1]-self.foody),2),1/2)<=20:
                same = True
                while same:
                    print("回炉重造了,原坐标是:({},{})".format(self.foodx,self.foody))
                    self.foodx = round(random.randrange(70, dis_width - snake_block-60) / 10.0) * 10.0
                    self.foody = round(random.randrange(70, dis_height - snake_block-60) / 10.0) * 10.0    
                    if pow(pow((i[0]-self.foodx),2)+pow((i[1]-self.foody),2),1/2)<=20:
                        same = True
                    else:
                        same = False
                        print("重生后的是:({},{})".format(self.foodx,self.foody)) 
            if i[2]==3:
                c_s+=1
                if c_s >=1:
                    print("原type为{}".format(self.type))
                    self.type=random.randint(0,2)
                    print("现type为{}".format(self.type))


        while same:
            self.foodx = round(random.randrange(70, dis_width - snake_block-60) / 10.0) * 10.0
            self.foody = round(random.randrange(70, dis_height - snake_block-60) / 10.0) * 10.0    
            for i in snake.List:
                if i==[self.foodx,self.foody]:
                    same=True
                else:
                    same = False
            for i in list:
                if pow((i[0]-self.foodx),2)+pow((i[1]-self.foody),2)<=20:
                    same = True
                

                else:same = False               

        self.block = snake_block
        self.Head=[self.foodx,self.foody,self.type]
    def appear(self,list):
        for i in list:
            if i[2]==0:
                pygame.draw.rect(dis, green, [i[0],i[1], self.block, self.block])
            if i[2]==1:
                pygame.draw.rect(dis, purple, [i[0],i[1], self.block, self.block])
            if i[2]==2:
                pygame.draw.rect(dis, blue, [i[0],i[1], self.block, self.block])
            if i[2]==3:
                pygame.draw.rect(dis, orange, [i[0],i[1], self.block, self.block])

def gameLoop():
    
    list=[]
    num=[0,0]
    numm=[]
    count=0
    countt=0
    s1 = False
    s2 = False
    s=[25]

    x1_change=0
    y1_change=0

    game_over = False
    game_close = False

    snake=Snake(80,80)
    food=Food(snake.block,snake,list)
    list.append(food.Head)
    bo0 = True
    bo1 = True

    while not game_over:



        while game_close==True:
            dis.fill(white)
            message("失败", red, lost_style, [dis_width / 2 - 50, dis_height / 3 - 25])
            message("接下来请按C键重新开始或者Q键退出游戏。", red, font_style, [dis_width / 2 - 9*25, dis_height / 3 + 25 + 1*25])
            if(eat==0):
                message("死因：创墙！",red, font_style, [280, dis_height / 3 - 50])
            if(eat==1):
                message("死因：自己咬自己！",red,font_style,[250, dis_height / 3 - 50])             
            Your_score(snake.length - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        gameLoop()
        bo = False
        #移动（如果w,a,s,d之类的chang就对应相应的值，移动长度为snake.block，即为蛇的大小）
        if pygame.event.peek():
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:                 
                        x1_change = -snake.block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake.block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake.block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake.block
                        x1_change = 0  
        
        #add
        bo = False
        mykeyslist = pygame.key.get_pressed()
        if (mykeyslist[pygame.K_RIGHT] or mykeyslist[pygame.K_LEFT] or mykeyslist[pygame.K_DOWN] or mykeyslist[pygame.K_UP]) :  # 如果按键按下，这个值为1
            bo=True
            countt+=1
            if countt>2:
                pygame.mixer.Sound.play(break_music)
            if countt==1:
                pygame.mixer.Sound.play(start_music,fade_ms=1)
            if bo or countt>=1:         
                n=int(time.time())
                if len(numm)<1:
                    numm.append(n)
                else:
                    if(n-numm[len(numm)-1]>=2):
                        numm.append(n)
                        food.__init__(snake.block,snake,list)
                        food.appear(list)
                        list.append(food.Head)

        if snake.x1 > dis_width-70 or snake.x1 < 60 or snake.y1 > dis_height-60 or snake.y1 < 70:
            pygame.mixer.Sound.play(end_music)
            eat=0
            game_close = True

        snake.x1 += x1_change
        snake.y1 += y1_change

        #设置颜色
        dis.fill(white)
        if snake.speed+hard*snake.length>40:
            dis.fill(orange)
            if s1 == False:
                s1 = True
                pygame.mixer.Sound.play(speed1)
        if snake.speed+hard*snake.length>50:
            color = [red,orange,black,green,grey]
            type = random.randint(0,4)
            dis.fill(color[type])
            if s2 == False:
                s2 = True
                pygame.mixer.Sound.play(speed2)
        food.appear(list)

        #框
        pygame.draw.rect(dis, (0, 0, 0), [50,60,600,400],1)

        snake.Head=[]
        snake.Head.append(snake.x1)
        snake.Head.append(snake.y1)
        snake.List.append(snake.Head)

        if len(snake.List) > snake.length:
            del snake.List[0]


        #对于蛇的每个点若与蛇头重复则寄，除头外（有第二个的bug）
        for x in snake.List[:-1]:
            if x == snake.Head:
                pygame.mixer.Sound.play(end_music)            
                game_close = True
                eat=1

        
        snake.our_snake(game_close,snake.x1,snake.y1,snake.block,snake.List)
        Your_score(snake.length-1)
        Your_speed(s[count])

        pygame.display.update()

        for i in list:
            if snake.x1 == i[0] and snake.y1 == i[1]:
                list.remove([i[0],i[1],i[2]])
                pygame.mixer.Sound.play(eat_music)
                if i[2]==0:
                    snake.length+=1
                if i[2]==1:
                    snake.length+=2
                if i[2]==2:
                    snake.speed+=4
                    snake.length+=1
                if i[2]==3:
                    snake.speed-=3
                    snake.length+=1



        clock.tick(snake.speed+0.5*snake.length)
        s.append(snake.speed+hard*snake.length)
        count+=1

    pygame.display.quit()

if(start()):
    gameLoop()
                


    