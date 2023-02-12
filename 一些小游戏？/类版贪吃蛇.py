#基本内容
import pygame
import random
#初始化pygame
pygame.init()

#颜色参数
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
ching = (0, 128, 128)
 
#屏幕大小参数
dis_width = 700
dis_height = 500


#屏幕大小设置
dis = pygame.display.set_mode((dis_width, dis_height))
#(全屏)dis = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('贪吃蛇小游戏')
pygame.display.set_palette

#帧数设置
clock = pygame.time.Clock()

#字体参数设置
font_style = pygame.font.SysFont(['华文宋体', "bahnschrift"], 25)
score_font = pygame.font.SysFont('华文宋体', 35)
lost_style = pygame.font.SysFont('华文宋体', 50)

a = pygame.font.get_fonts()

#得分输出函数
def Your_score(score):
    value = score_font.render("你的分数：" + str(score), True, blue)
    dis.blit(value, [0, 0])
    pygame.display.update()

#消息输出函数
def message(msg, color, ft, pos):
    mesg = ft.render(msg, True, color)
    dis.blit(mesg, pos)


class Snake:
   
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
        self.block=10
        self.speed=15 
        self.length=1
        self.List=[]
        self.Head=[]
    def our_snake(self,game_close,x1,y1,block,snake_list):
        if(game_close==False):
            if(60<=y1<=460):
                pygame.draw.rect(dis, red, [x1, y1, block, block])
                for x in snake_list[1:]:
                    pygame.draw.rect(dis, black, [x[0], x[1], block, block])
                pygame.display.update()

class Food:
    def __init__(self,snake_block):
        self.foodx = round(random.randrange(70, dis_width - snake_block-60) / 10.0) * 10.0
        self.foody = round(random.randrange(70, dis_height - snake_block-60) / 10.0) * 10.0
        self.block = snake_block
        print("调用构造函数")

    def appear(self):
        pygame.draw.rect(dis, green, [self.foodx,self.foody, self.block, self.block])
        print("已调用,坐标({},{})".format(self.foodx,self.foody))

def gameLoop():

    x1_change=0
    y1_change=0

    game_over = False
    game_close = False

    snake=Snake(80,80)
    food=Food(snake.block)

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
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        #移动（如果w,a,s,d之类的chang就对应相应的值，移动长度为snake.block，即为蛇的大小）
        for event in pygame.event.get():
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

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop()      

        if snake.x1 > dis_width-70 or snake.x1 < 60 or snake.y1 > dis_height-60 or snake.y1 < 70:
            eat=0
            game_close = True

        snake.x1 += x1_change
        snake.y1 += y1_change

        #设置颜色
        dis.fill(white)
        
        food.appear()

        #框
        pygame.draw.rect(dis, (0, 0, 0), [50,60,600,400],1)

        snake.Head=[]
        snake.Head.append(snake.x1)
        snake.Head.append(snake.y1)
        snake.List.append(snake.Head)
        print("Head:({},{})".format(snake.x1,snake.y1))

        if len(snake.List) > snake.length:
            del snake.List[0]
            print("已删除")

        print("snake_List:{}".format(snake.List))

        #对于蛇的每个点若与蛇头重复则寄，除头外（有第二个的bug）
        for x in snake.List[:-1]:
            if x == snake.Head:
                game_close = True
                eat=1
        
        snake.our_snake(game_close,snake.x1,snake.y1,snake.block,snake.List)
        Your_score(snake.length-1)

        pygame.display.update()

        if snake.x1 == food.foodx and snake.y1 == food.foody:
            food.__init__(snake.block)
            food.appear()
            snake.length+=1
            print(snake.length)
        
        clock.tick(snake.speed+2.5*snake.length)

    pygame.display.quit()


gameLoop()
                


    