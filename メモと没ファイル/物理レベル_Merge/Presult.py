# Ptitle.py
import pygame
import Pparameter

pygame.font.init()

#フォントの設定
FONT1 = pygame.font.Font(None, 80)
FONT2 = pygame.font.Font(None, 40)

#色の設定
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)


# Presult.py

import pygame

# 1. 準備
pygame.font.init()

# フォント定義
FONT_BIG = pygame.font.Font(None, 100) # デカ文字
FONT_SMALL = pygame.font.Font(None, 50) # 普通の文字

# 色定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255) # 水色（勝利用）

# ---------------------------------------------------------
# 勝利画面の描画
# ---------------------------------------------------------
def draw_winning(screen):
    # メインメッセージ
    text_win = FONT_BIG.render("YOU WIN!!", True, CYAN)
    screen.blit(text_win, Pparameter.centeringY(text_win, 200)) # だいたい真ん中
    
    # 次の指示
    text_next = FONT_SMALL.render("Press SPACE to NEXT STAGE", True, WHITE)
    screen.blit(text_next, Pparameter.centeringY(text_next, 300))


# ---------------------------------------------------------
# 敗北画面の描画
# ---------------------------------------------------------
def draw_losing(screen):
    # メインメッセージ
    text_lose = FONT_BIG.render("GAME OVER...", True, RED)
    screen.blit(text_lose, Pparameter.centeringY(text_lose, 200)) # だいたい真ん中
    
    # 次の指示
    text_retry = FONT_SMALL.render("Press SPACE to Title", True, WHITE)
    screen.blit(text_retry, Pparameter.centeringY(text_lose, 300))