# Ptitle.py
import pygame
import sys

# フォントの初期化
pygame.font.init()

# フォントの設定
FONT = pygame.font.Font(None, 60)
#追加可能


# 色の設定マクロ (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_map1(screen):
    pygame.draw.rect(screen, (255,0,0),(200,200,300,300), 0)
    text_map1 = FONT.render("stage_map1", True, WHITE)
    screen.blit(text_map1,(250,30))


def draw_map2(screen):
    text_map1 = FONT.render("stage_map2", True, WHITE)
    screen.blit(text_map1,(250,30))


def draw_map3(screen):
    text_map1 = FONT.render("stage_map3", True, WHITE)
    screen.blit(text_map1,(250,30))
    

def draw_wait_start():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "START?"