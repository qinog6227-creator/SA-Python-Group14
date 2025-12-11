# Ptitle.py
import pygame
import sys

# フォントの初期化
pygame.font.init()

# フォントの設定
FONT = pygame.font.Font(None, 40)
#追加可能


# 色の設定マクロ (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_map1(screen):
    screen.fill(BLACK)
    text_map1 = FONT.render("stage_map1", True, WHITE)
    screen.blit(text_map1,(400,400))


def draw_map2(screen):
    screen.fill(BLACK)
    text_map1 = FONT.render("stage_map2", True, WHITE)
    screen.blit(text_map1,(400,400))


def draw_map3(screen):
    screen.fill(BLACK)
    text_map1 = FONT.render("stage_map3", True, WHITE)
    screen.blit(text_map1,(400,400))

    

def draw_wait_start():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "START?"