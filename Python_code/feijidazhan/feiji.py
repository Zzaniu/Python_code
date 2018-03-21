# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time
import threading


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 190
        self.y = 730
        self.screen = screen_temp
        self.image = pygame.image.load("./image/hero1.png")
        self.bullet_list = []
        self.fire_flg = False

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_lift(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./image/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5


def key_control(hero_temp):
    hero_temp.display()
    pygame.display.update()
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("exit")
                exit()
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_lift()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()


def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load("./image/background.png")

    #3. 创建一个背景对象
    hero = HeroPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
