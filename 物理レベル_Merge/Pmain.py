import pygame
import sys
import Ptitle


# 1. 準備（画用紙を作る）
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 幅800, 高さ600
pygame.display.set_caption("サダメドロー")

# 文字を書くための「筆（フォント）」を用意
font = pygame.font.Font(None, 50) 
font2 = pygame.font.Font(None, 100)
#追加可能


# === 2. メインループ（ここが紙芝居） ===
while True:
    # (終了ボタンが押されたら終わる処理)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Ptitle.draw_title(screen)


    pygame.display.flip()