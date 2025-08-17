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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # キー入力
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(5, 0)


    # ボール移動
    ball.move_ip(ball_dx, ball_dy)


    # 壁で反射
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy


    # パドルで反射
    if ball.colliderect(paddle):
        ball_dy = -ball_dy


    # ブロックに当たったら消す
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        hit_block = blocks.pop(hit_index)
        ball_dy = -ball_dy


    # 下に落ちたらゲームオーバー
    if ball.bottom >= HEIGHT:
        print("ゲームオーバー！")
        pygame.quit()
        sys.exit()


    # 描画
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    pygame.display.flip()
    clock.tick(60)