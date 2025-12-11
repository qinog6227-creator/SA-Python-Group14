import pygame
import os
import Pparameter #マクロと中央揃え関数

# --- 1. 準備：定数とフォント ---

# ここで初期化しておかないと、importしただけでエラーになる場合があるため残す
pygame.font.init()

#フォント設定
FONT = pygame.font.Font(None, 80) # 小さめ
#追加可能

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# --- 2. 描画関数 ---

#上のメニュー
def draw_encountBar(screen,encount):
    text_title = FONT.render(f"{encount}st Round", True, WHITE)
    screen.blit(text_title,Pparameter.centeringY(text_title, 60))


def draw_battleStatus(screen, e_hp, p_hp, stockA, stockD): 
    text_bar = FONT.render(f"----- Latest Imformation -----", True, WHITE)
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
    text_bar = FONT.render(f"-----Command-----",True, WHITE)
    text_drawing = FONT.render("draw Keeping!", True, WHITE)
    text_carryOut = FONT.render("carry out owned card!", True, WHITE)
    screen.blit(text_bar, (400, 150))
    screen.blit(text_drawing, (400, 190))
    screen.blit(text_carryOut, (400, 230))






def draw_hand(screen, hand_list):
    # --- 設定 ---
    start_x = 150       # 最初のカードの左端の位置
    start_y = 450       # カードの高さ（Y座標）
    gap = 80            # カードごとの隙間（ずらす幅）
    
    # --- ループ処理 ---
    # i には「0, 1, 2...」という番号が入る
    # card_name には「"Attack"」などのカード名が入る
    for i, card_name in enumerate(hand_list):
        
        # 1. ずらす計算
        # 最初の位置に (番号 × 隙間) を足す
        x_pos = start_x + (i * gap)
        
        # 2. 四角形（カード）を描く
        # カードサイズ: 幅60, 高さ90 と仮定
        card_rect = pygame.Rect(x_pos, start_y, 60, 90)
        
        # 白い枠線を描く
        pygame.draw.rect(screen, WHITE, card_rect, 2)
        
        # 3. 文字を書く (カード名)
        # 枠の中に書きたいので少し座標を調整 (+5, +35)
        text = FONT.render(card_name, True, WHITE)
        screen.blit(text, (x_pos + 5, start_y + 35))


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