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
pygame.display.set_caption("植物大战僵尸")#设置窗口标题
screen = pygame.display.set_mode((800, 600))#创建了一个窗口

card = {}
card['a_0'] = pygame.image.load('jianguo_1_card.gif').convert_alpha()
card['a_1'] = pygame.image.load('wandou_1_card.gif').convert_alpha()
card['a_2'] = pygame.image.load('xiangrikui_1_card.gif').convert_alpha()

imageDict = {}
imageDict['a_0'] = pygame.image.load('jianguo_1.gif').convert_alpha()
imageDict['a_1'] = pygame.image.load('wandou_1.gif').convert_alpha()
imageDict['a_2'] = pygame.image.load('xiangrikui_1.gif').convert_alpha()

imageDict_z = {}
imageDict_z['z_0'] = pygame.image.load('jiangshi1.gif').convert_alpha()
imageDict_z['z_1'] = pygame.image.load('jiangshi_2.gif').convert_alpha()

background_1 = pygame.image.load('background_1.gif').convert()
background_2 = pygame.image.load('background_2.jpg').convert()
SeedBank = pygame.image.load('SeedBank.png').convert()

pygame.mouse.set_cursor(*pygame.cursors.tri_left)

nums = {}
nums['a_0'] = [10,2,100,100,12]
nums['a_1'] = [5,2,120,120,7]
nums['a_2'] = [3,2,85,100,12]

nums_z = {}
nums_z['z_0'] = [9,4,86.15,150,13]
nums_z['z_1'] = [9,2,100,150,11]

image = {}
image['a_0'] = [imageDict['a_0'].subsurface(Rect((i*nums['a_0'][2],0),(nums['a_0'][2],nums['a_0'][3])))
                        for i in xrange(nums['a_0'][4])]
image['a_1'] = [imageDict['a_1'].subsurface(Rect((i*nums['a_1'][2],0),(nums['a_1'][2],nums['a_1'][3])))
                        for i in xrange(nums['a_1'][4])]
image['a_2'] = [imageDict['a_2'].subsurface(Rect((i*nums['a_2'][2],0),(nums['a_2'][2],nums['a_2'][3])))
                        for i in xrange(nums['a_2'][4])]

image_z = {}
image_z['z_0'] = [imageDict_z['z_0'].subsurface(Rect((i*nums_z['z_0'][2],0),(nums_z['z_0'][2],nums_z['z_0'][3])))
                        for i in xrange(nums_z['z_0'][4])]
image_z['z_1'] = [imageDict_z['z_1'].subsurface(Rect((i*nums_z['z_1'][2],0),(nums_z['z_1'][2],nums_z['z_1'][3])))
                        for i in xrange(nums_z['z_1'][4])]

rect_1 = (0,0,0,0,)
b = True
pl = {}
u = 0
a = 0
x1 = 0
y1 = 0
class Choose:
    def __init__(self):
        pass
    def choose(self):
        global 'a_0','a_1','a_2',a_3,'z_0'
        for event in pygame.event.get():
            pass
    def mainloop(self):
        global a,b,'a_0','a_1','a_2',a_3,'z_0',pl
        i = 0
        while b:
            a = 0
            screen.blit(background_2, (0,0))#将背景图画上去
            screen.blit(pygame.transform.scale(SeedBank, (670, 87)),(60,0))
            screen.blit(card['a_0'], (25,90))
            screen.blit(card['a_1'], (78,90))
            screen.blit(card['a_2'], (131,90))
            for event in pygame.event.get():
                if event.type == QUIT:#接收到退出事件后退出程序
                    sys.exit(0)
                if event.type == KEYDOWN:
                    b = False 
                x,y = pygame.mouse.get_pos()   
                if event.type == pygame.MOUSEBUTTONDOWN and 25<x<78 and 90<y<165:
                    card[i] = card['a_0']
                    pl[i] = 'a_0'
                    i = i + 1
                    break
                x,y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and 78<x<131 and 90<y<165:
                    card[i] = card['a_1']
                    pl[i] = 'a_1'
                    i = i + 1
                    break
                x,y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and 131<x<184 and 90<y<165:
                    card[i] = card['a_2']
                    pl[i] = 'a_2'
                    i = i + 1
                    break
            while a < i:
                screen.blit(card[a], (175+a*55,5))
                a = a + 1
            pygame.display.update()#刷新一下画面
            pygame.time.Clock().tick(0)
        g = Game()
        g.mainloop()
class Game:
    def __init__(self):
        pass
    def update(self):
        pass
    def mainloop(self):
        global b,rect_1
        i_0 = 0
        r_Zom = Rect(805,200,86.15,150)    
        Zomb = Zombie(image_z['z_0'],r_Zom,[-5,0])
        Plan = {}
        pla = {}
        while True:#游戏主循环
            tru = False
            screen.blit(background_1, (0,0))#将背景图画上去
            i = 0
            while i < a:
                screen.blit(card[i], (75+i*53,5))
                i = i + 1 
            for event in pygame.event.get():
                if event.type == QUIT:#接收到退出事件后退出程序
                    sys.exit(0)
                i = 0
                while i < a: 
                    x,y = pygame.mouse.get_pos()    
                    if event.type == pygame.MOUSEBUTTONDOWN and 75+i*53<x<75+53*(i+1) and 5<y<80:
                        screen.blit(image[pl[i]][0], (x-nums[pl[i]][2]/2, y-nums[pl[i]][3]/2))
                        j = 0
                        while j < i_0: 
                            Plan[j].update(screen)
                            j = j + 1
                        Zomb.update(screen)
                        pygame.display.update()#刷新一下画面
                        tru = True
                    while tru:
                        x,y = pygame.mouse.get_pos()
                        screen.blit(background_1, (0,0))#将背景图画上去
                        j = 0
                        while j < a:
                            screen.blit(card[j], (75+j*53,5))
                            j = j + 1
                        j = 0
                        while j < i_0:
                            screen.blit(pla[j][0],(pla[j][1],pla[j][2]))
                            j = j + 1
                        r_Zom = rect_1
                        Zomb1 = Zombie(image_z['z_0'],r_Zom,[-0.5,0])
                        Zomb1.update(screen)
                        screen.blit(image[pl[i]][0], (x-nums[pl[i]][2]/2, y-nums[pl[i]][3]/2))
                        pygame.display.update()#刷新一下画面 
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x,y = pygame.mouse.get_pos()
                                r_Pla = Rect(x-nums[pl[i]][2]/2,y-nums[pl[i]][3]/2,nums[pl[i]][2],nums[pl[i]][3])
                                Plan[i_0] = Plants(image[pl[i]],r_Pla,i,x-nums[pl[i]][2]/2,y-nums[pl[i]][3]/2)
                                pla[i_0] = [image[pl[i]][0], x-nums[pl[i]][2]/2, y-nums[pl[i]][3]/2]
                                i_0 = i_0 + 1
                                tru = False
                    i = i + 1                               
            screen.blit(background_1, (0,0))#将背景图画上去
            j = 0
            while j < a:
                screen.blit(card[j], (75+j*53,5))
                j = j + 1
            i = 0
            while i < i_0: 
                Plan[i].update(screen)
                i = i + 1
            Zomb.update(screen)
            pygame.display.update()#刷新一下画面
            pygame.time.Clock().tick(3)
class Plants:
    def __init__(self,imgs,rect,i,x,y):
        self.imgs = imgs
        self.rect = rect
        self.num = 0
        self.n = -1
        self.i = i
        self.x = x
        self.y = y
    def update(self,screen):
        global rect_1,u,x1,y1
        x1 = self.x+nums[pl[self.i]][2]-20
        y1 = self.y
        if rect_1 != (self.x+nums[pl[self.i]][2]-20,self.y,86.15,150) and u == 0:
            self.num += 1
            if self.num%nums[pl[self.i]][0] == 0:
                self.num = 0
            screen.blit(self.imgs[self.num],self.rect)
        if rect_1 == (self.x+nums[pl[self.i]][2]-20,self.y,86.15,150):
            u += 1
            if u <20:
                screen.blit(self.imgs[nums[pl[self.i]][0]],self.rect)
            if u >= 20 and u <30:
                screen.blit(self.imgs[nums[pl[self.i]][0]+1],self.rect)            
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
        if rect_1 != (x1,y1,86.15,150) or u >= 30:
            self.num += 1
            rect_1=rect_1.move(self.speed)
            if self.num%nums_z['z_0'][0] == 0:
                self.num = 0
            screen.blit(self.imgs[self.num],rect_1)
        else:
            self.nu += 1
            if self.nu%nums_z['z_0'][1] == 0:
                self.nu = 0
            screen.blit(self.imgs[self.nu+nums_z['z_0'][0]],rect_1)
        return 0
c = Choose()
c.mainloop()
