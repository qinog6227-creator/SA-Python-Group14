# Ptitle.py
import pygame
import PARAMETER

pygame.font.init()

#フォントの設定
FONT = pygame.font.Font(None, 50)
#追加可能


# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Ptitle.py の draw_title_screen 関数の中身 (完成形)

def draw_title(screen):
    
    # A. ゲームタイトルの描画（画面上部中央）
    title_text = FONT.render("SADAME DRAW", True, RED)
    screen.blit(title_text, PARAMETER.centeringY(title_text, 100))
    
    # ----------------------------------------------------
    # B. サブタイトル枠の図形を描画 (画面中央より少し上)
    
    # 矩形情報: 左上隅(200, 200)から幅400, 高さ150の大きな枠
    sub_rect_info = (200, 200, 400, 150)
    sub_rect = pygame.Rect(sub_rect_info)
    
    # 枠線の描画 (太さ2)
    pygame.draw.rect(screen, WHITE, sub_rect, width=2, border_radius=5) 
    
    # 枠内の文字
    sub_text = FONT.render("Press START to change your Fate.", True, WHITE)
    screen.blit(sub_text, sub_text.get_rect(center=(400, 275))) # 枠の中央に配置
    # ----------------------------------------------------
    
    # C. スタートボタンの図形を描画（画面下部中央）
    
    # 矩形情報: 左上隅(300, 420)から幅200, 高さ60のボタン
    button_x = 300 
    button_y = 420 
    button_width = 200
    button_height = 60
    
    button_rect_info = (button_x, button_y, button_width, button_height)
    button_rect = pygame.Rect(button_rect_info)
    
    # 1. 背景と枠線を描画する
    pygame.draw.rect(screen, (70, 70, 70), button_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, button_rect, width=3, border_radius=10)
    
    # 2. スタートボタンの文字
    start_text = FONT.render("START", True, WHITE)
    screen.blit(start_text, start_text.get_rect(center=(400, 450)))


def draw_wait_start():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "START?"