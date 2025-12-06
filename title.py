import pygame
import os
import sys

pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Title Screen")

# タイトル画像のパス
BASE = os.path.dirname(__file__)
TITLE_IMG_PATH = os.path.join(BASE, "pictures", "title", "title(ver1).png")

# タイトル画像読み込み
title_img = pygame.image.load(TITLE_IMG_PATH).convert_alpha()
title_img = pygame.transform.scale(title_img, (WIDTH, HEIGHT))

clock = pygame.time.Clock()

# 状態
STATE_TITLE = 0
STATE_GAME = 1
state = STATE_TITLE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # クリックで開始
        if state == STATE_TITLE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = STATE_GAME

    # ----------- 描画 -----------
    if state == STATE_TITLE:
        screen.blit(title_img, (0, 0))

    elif state == STATE_GAME:
        screen.fill((0, 0, 0))

    pygame.display.update()
    clock.tick(60)