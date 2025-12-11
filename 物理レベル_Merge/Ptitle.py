# Ptitle.py
import pygame

pygame.font.init()

#フォントの設定
FONT = pygame.font.Font(None, 80)
#追加可能

#色をタプルの形で設定
BLACK = (0,0,0)
WHITE = (255,255,255)

def draw_title(screen):
    text_title = FONT.render("Titile", True, WHITE)
    screen.blit(text_title,(400,400))

def draw_wait_start():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "START?"