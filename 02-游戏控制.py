# coding=utf-8
import pygame

from pygame.locals import *
from sys import exit
# 初始化pygame，为使用硬件做准备
pygame.init()

# 创建一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)

'''font=pygame.font.Font(None,20)
line_height=font.get_linesize()
position=0'''
speed=[-2,1]
python=pygame.image.load("p.png")#加载图片
position=python.get_rect()#获取图形位置
pygame.display.set_caption("hello,world!")
bg=(255,255,255)
screen.fill(bg)
r_head=pygame.transform.flip(python,True,False)
# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出时间后退出程序
            exit()
        '''screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
        position+=line_height
        if position >480:
            position=0'''
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                python=python
                speed=[-1,0]
            if event.key==K_UP:
                speed=[0,-1]
            if event.key==K_RIGHT:
               python=pygame.transform.flip(python,True,False)
               speed=[1,0]
            if event.key==K_DOWN:
                speed=[0,1]

                
    position=position.move(speed)
    if position.left<0 or position.right>640:
        python=pygame.transform.flip(python,True,False)
        speed[0]=-speed[0]
    if position.top<0 or position.bottom>480:
        speed[1]=-speed[1]
        
    screen.fill(bg)
    screen.blit(python,position)#更新图像
    pygame.display.flip()
    pygame.time.delay(10)

    pygame.display.update()
