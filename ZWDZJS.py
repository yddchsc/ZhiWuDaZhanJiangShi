#!/usr/bin/env python
#coding:utf-8
import pygame#导入pygame库
import os, sys
from pygame.locals import *#导入一些常用的函数和常量
from sys import exit#向sys模块借一个exit函数用来退出程序
from os import _exit as exit
from pygame.sprite import Sprite

pygame.display.init()
pygame.font.init()
x1 = (1366 - 800)/2
y1 = (768 - 600)/2
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d"%(x1,y1)
pygame.event.set_allowed([QUIT,MOUSEMOTION,MOUSEBUTTONDOWN,MOUSEBUTTONUP,KEYDOWN])
pygame.display.set_caption("植物大战僵尸")#设置窗口标题
screen = pygame.display.set_mode((800, 600))#创建了一个窗口

a_0 = '0'
a_1 = '1'
a_2 = '2'
a_3 = '3'

z_0 = 5

card = {}
card[a_0] = pygame.image.load('jianguo_1_card.gif').convert_alpha()
'''card[a_1] = pygame.image.load('jiangshi_1_card.gif').convert_alpha()'''
card[a_1] = pygame.image.load('wandou_1_card.gif').convert_alpha()
card[a_2] = pygame.image.load('xiangrikui_card.gif').convert_alpha()
card[0] = pygame.image.load('SeedPacket_Larger.png').convert_alpha()
card[1] = pygame.image.load('SeedPacket_Larger.png').convert_alpha()
card[2] = pygame.image.load('SeedPacket_Larger.png').convert_alpha()

imageDict = {}
imageDict[a_0] = pygame.image.load('jianguo_1.gif').convert_alpha()
imageDict_z = {}
imageDict_z[z_0] = pygame.image.load('jiangshi1.gif').convert_alpha()

background_1 = pygame.image.load('background_1.gif').convert()
background_2 = pygame.image.load('background_2.jpg').convert()
SeedBank = pygame.image.load('SeedBank.png').convert()

pygame.mouse.set_cursor(*pygame.cursors.tri_left)

nums = {}
nums[a_0] = [7,5,100,100]
nums_z = {}
nums_z[z_0] = [9,4,86.15,150]

image = {}
image[a_0] = [imageDict[a_0].subsurface(Rect((i*nums[a_0][2],0),(nums[a_0][2],nums[a_0][3])))
                        for i in xrange(12)]
image_z = {}
image_z[z_0] = [imageDict_z[z_0].subsurface(Rect((i*nums_z[z_0][2],0),(nums_z[z_0][2],nums_z[z_0][3])))
                        for i in xrange(13)]
rect_1 = (0,0,0,0,)
u = 0
b = True
pl = {}
class Choose:
    def __init__(self):
        pass
    def choose(self):
        global a_0,a_1,a_2,a_3,z_0
        for event in pygame.event.get():
            pass
    def mainloop(self):
        global b,a_0,a_1,a_2,a_3,z_0,pl
        i = 0
        while b:
            a = 0
            screen.blit(background_2, (0,0))#将背景图画上去
            screen.blit(pygame.transform.scale(SeedBank, (670, 87)),(60,0))
            screen.blit(card[a_0], (25,90))
            screen.blit(card[a_1], (78,90))
            screen.blit(card[a_2], (131,90))
            for event in pygame.event.get():
                if event.type == QUIT:#接收到退出事件后退出程序
                    sys.exit(0)
                if event.type == KEYDOWN:
                    b = False 
                x,y = pygame.mouse.get_pos()   
                if event.type == pygame.MOUSEBUTTONDOWN and 25<x<78 and 90<y<165:
                    card[i] = card[a_0]
                    pl[i] = a_0
                    i = i + 1
                    break
                x,y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and 78<x<131 and 90<y<165:
                    card[i] = card[a_1]
                    pl[i] = a_1
                    i = i + 1
                    break
                x,y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and 131<x<184 and 90<y<165:
                    card[i] = card[a_2]
                    pl[i] = a_2
                    i = i + 1
                    break
            while a<i:
                screen.blit(card[a], (175+a*55,5))
                a = a + 1
            pygame.display.update()#刷新一下画面
            pygame.time.Clock().tick(0)
        g = Game()
        g.mainloop()
class Game:
    def __init__(self):
        pass
    def mainloop(self):
        global b
        r_Zom = Rect(805,200,86.15,150)     
        Zomb = Zombie(image_z[z_0],r_Zom,[-5,0])
        r_Pla = Rect(400,240,100,100)
        Plan = Plants(image[a_0],r_Pla)
        while True:#游戏主循环
            screen.blit(background_1, (0,0))#将背景图画上去
            screen.blit(card[a_0], (75,5))
            for event in pygame.event.get():
                if event.type == QUIT:#接收到退出事件后退出程序
                    sys.exit(0)
            Plan.update(screen)
            Zomb.update(screen)
            pygame.display.update()#刷新一下画面
            pygame.time.Clock().tick(3)

class Plants:
    def __init__(self,imgs,rect):
        self.imgs = imgs
        self.rect = rect
        self.num = 0
        self.n = -1
    def update(self,screen):
        global rect_1,u
        if rect_1 == (470,200,86.15,150):
            u += 1
            if u < 10:
                self.n += 1
                if self.n%3 ==0:
                    self.n = 0
                screen.blit(self.imgs[self.n+nums[a_0][0]],self.rect)
            if u >= 10 and u <20:
                screen.blit(self.imgs[nums[a_0][0]+3],self.rect)
            if u >= 20 and u <30:
                screen.blit(self.imgs[nums[a_0][0]+4],self.rect)
        if rect_1 != (470,200,86.15,150) and u == 0:
            self.num += 1
            if self.num%nums[a_0][0] == 0:
                self.num = 0
            screen.blit(self.imgs[self.num],self.rect)    
        return 0        
class Zombie:
    def __init__(self,imgs,rect,speed):
        global rect_1,u 
        self.imgs = imgs
        rect_1 = rect
        self.speed = speed
        self.num = 0
        self.nu = 0
    def move():
        pass
    def update(self,screen):
        global rect_1
        if rect_1 != (470,200,86.15,150) or u >= 30:
            self.num += 1
            rect_1=rect_1.move(self.speed)
            if self.num%nums_z[z_0][0] == 0:
                self.num = 0
            screen.blit(self.imgs[self.num],rect_1)
        else:
            self.nu += 1
            if self.nu%nums_z[z_0][1] == 0:
                self.nu = 0
            screen.blit(self.imgs[self.nu+nums_z[z_0][0]],rect_1)
        return 0
c = Choose()
c.mainloop()
