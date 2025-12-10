# Ptitle.py
import pygame

pygame.font.init()

#フォントの設定
FONT_TITLE = pygame.font.Font(None, 80)
FONT_SUB = pygame.font.Font(None, 40)

#色をタプルの形で設定
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)


def draw_title(screen):
    screen.fill(BLACK)
    
    # タイトル枠
    pygame.draw.rect(screen, RED, (100, 100, 600, 300), 0)
    
    # タイトル文字
    text_title = FONT_TITLE.render("Unmei Draw (Pre)", True, WHITE)
    screen.blit(text_title, (180, 200))
    
    # スタート案内
    text_start = FONT_SUB.render("Press [S] to START", True, WHITE)
    screen.blit(text_start, (260, 450))





def draw_wait_start():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "START?"