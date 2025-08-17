import pygame
import sys
import random

pygame.init()

# 画面設定
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ブロック崩し")


# 色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


# パドル
paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 30, 100, 10)


# ボール
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 10, 10)
ball_dx, ball_dy = 3, -3


# ブロック生成
blocks = []
for i in range(5):  # 5行
    for j in range(10):  # 10列
        block = pygame.Rect(60 * j + 5, 20 * i + 5, 55, 15)
        blocks.append(block)


clock = pygame.time.Clock()