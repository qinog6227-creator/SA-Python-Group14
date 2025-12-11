import pygame
import os

# --- 1. 準備：定数とフォント ---

# ここで初期化しておかないと、importしただけでエラーになる場合があるため残す
pygame.font.init()

#フォント設定
FONT = pygame.font.Font(None, 30) # 小さめ
#追加可能

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- 2. 描画関数 ---

def encount_bar(screen,encount):
    screen.fill(BLACK)
    text_title = FONT.render(f"{encount}st Round", True, WHITE)
    screen.blit(text_title,(400,400))


def draw_battleStatus(screen, e_hp, p_hp, stockA, stockD): 
    screen.fill(BLACK)
    text_bar = FONT.render(f"----- Latest Imformation -----")
    text_enemysta = FONT.render(f"Enemy HP: {e_hp}", True, WHITE)
    text_playersta = FONT.render(f"Player HP: {p_hp}", True, WHITE)
    text_stockA = FONT.render(f"Stock Attack Card: {stockA}", True, WHITE)
    text_stockD = FONT.render(f"Stock Defense Card: {stockD}", True, WHITE)
    screen.blit(text_bar, (50, 150))
    screen.blit(text_enemysta, (50, 190))
    screen.blit(text_playersta, (50, 230))
    screen.blit(text_stockA, (50, 270))
    screen.blit(text_stockD, (50, 310))



def draw_battleCommand(screen):
    screen.fill(BLACK)
    text_bar = FONT.render(f"-----Command-----")
    text_drawing = FONT.render("draw Keeping!", True, WHITE)
    text_carryOut = FONT.render("carry out owned card!", True, WHITE)
    screen.blit(text_bar, (200, 150))
    screen.blit(text_drawing, (200, 190))
    screen.blit(text_carryOut, (200, 230))


def draw_wait():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "COMMAND?"

def draw_logs(screen, logs):
    # ログウィンドウの仮置き
    log_area_rect = (550, 50, 220, 500)
    pygame.draw.rect(screen, (30, 30, 30), log_area_rect) # 黒背景
    pygame.draw.rect(screen, WHITE, log_area_rect, 2) # 白枠

    # ログ表示 (最新の数件を上から)
    start_y = 60
    display_logs = logs[-15:] 
    
    for msg in display_logs:
        text = FONT.render(msg, True, WHITE)
        screen.blit(text, (560, start_y))
        start_y += 25