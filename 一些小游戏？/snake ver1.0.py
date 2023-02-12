import pygame
import time
import random
import sys
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

#蛇的大小和速度参数
snake_block = 10
snake_speed = 15


#绘制蛇函数       
def our_snake(game_close,x1,y1,snake_block, snake_list):
    if(game_close==False):
        if(60<=y1<=460):
            pygame.draw.rect(dis, red, [x1, y1, snake_block, snake_block])
            for x in snake_list[1:]:
                pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
            pygame.display.update()

#消息输出函数
def message(msg, color, ft, pos):
    mesg = ft.render(msg, True, color)
    dis.blit(mesg, pos)

#主体函数
def gameLoop():

    game_over = False
    game_close = False
 
    #蛇的起始位置
    x1 = 80
    y1 = 80
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    
    #食物出现的位置(10,60是框的位置)
    foodx = round(random.randrange(70, dis_width - snake_block-60) / 10.0) * 10.0
    foody = round(random.randrange(70, dis_height - snake_block-60) / 10.0) * 10.0
 
    while not game_over:


    
        #挂掉之后
        while game_close == True:
            dis.fill(white)
            message("失败", red, lost_style, [dis_width / 2 - 50, dis_height / 3 - 25])
            message("接下来请按C键重新开始或者Q键退出游戏。", red, font_style, [dis_width / 2 - 9*25, dis_height / 3 + 25 + 1*25])
            if(eat==0):
                message("死因：创墙！",red, font_style, [280, dis_height / 3 - 50])
            if(eat==1):
                message("死因：自己咬自己！",red,font_style,[250, dis_height / 3 - 50])
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #移动（如果w,a,s,d之类的chang就对应相应的值，移动长度为snake_block，即为蛇的大小）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop()        
        #死亡条件
        if x1 > dis_width-70 or x1 < 60 or y1 > dis_height-60 or y1 < 70:
            eat=0
            game_close = True

            

        #if x1>dis_width-50 or x1<50 or y1 >= dis_height+50 or y1 < 70:
            #game_close=True
        
        #更新蛇头的位置
        x1 += x1_change
        y1 += y1_change
        
        #设置颜色
        dis.fill(white)
        
        #显示食物
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        #框
        pygame.draw.rect(dis, (0, 0, 0), [50,60,600,400],1)
        
        #把蛇头的坐标加入至列表中
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        print("Head:({},{})".format(x1,y1))
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            print("已删除")
 
        #对于蛇的每个点若与蛇头重复则寄，除头外（有第二个的bug）
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                eat=1

                


 
        our_snake(game_close,x1,y1,snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(70, dis_width - snake_block-60) / 10.0) * 10.0
            foody = round(random.randrange(70, dis_height - snake_block-60) / 10.0) * 10.0
            Length_of_snake += 1
        
        #用帧率设置蛇的移动速度(目前倍速为2.5长度加原有速度)
        clock.tick(snake_speed+2.5*Length_of_snake)
 
    pygame.display.quit()

#开始运行
gameLoop()
