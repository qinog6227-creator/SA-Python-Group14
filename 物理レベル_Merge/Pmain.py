import pygame
import sys
import Ptitle
import os # ★重要：ファイル操作用

# --- 1. 魔法の3行（場所ズレ防止）---
# これを入れると「画像が見つからない」エラーが消えます
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 1. 準備（画用紙を作る）
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 幅800, 高さ600
pygame.display.set_caption("サダメドロー.exe")

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

    # --- お絵かきタイム ---

    Ptitle.draw_title(screen)

    # --- 3. 提出（これをしないと画面に出ない！） ---
    pygame.display.flip()