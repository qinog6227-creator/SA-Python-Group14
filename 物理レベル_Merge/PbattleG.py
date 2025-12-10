import pygame
import os

# --- 1. 準備：定数とフォント ---

pygame.font.init()
FONT = pygame.font.Font(None, 30) # 小さめ
FONT_BIG = pygame.font.Font(None, 40) # 大きめ

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)



#2. 描画関数

def encount_bar(screen, encount):
    # バトル回数の表示 (画面上部)
    if encount == 1 or encount == 2:
        text_bar1 = FONT.render(f"Normal Enemy,{encount}戦目", True, RED)
        screen.bult(text_bar1, (50, 200))
    
    if encount == 3:
        text_bar1 = FONT.render(f"Boss,{encount}戦目", True, RED)
        screen.bult(text_bar1, (50, 200))



def draw_battleStatus(screen, e_hp, p_hp, stockA, stockD): 
    # 敵キャラの仮置き (四角)
    pygame.draw.rect(screen, GRAY, (300, 50, 200, 200)) # 敵キャラ枠

    # 1. 敵HP (上部に表示)
    text_ehp = FONT.render(f"ENEMY HP: {e_hp}", True, WHITE)
    screen.blit(text_ehp, (300, 260))

    # 2. プレイヤーHPバーの仮置き (左下)
    # HPの割合に合わせて幅を変える（最大幅: 200px）
    hp_width = int((p_hp / 30) * 200) # (30は仮のMAX_HP)
    pygame.draw.rect(screen, RED, (50, 400, hp_width, 20)) # HPバー本体
    pygame.draw.rect(screen, WHITE, (50, 400, 200, 20), 2) # HPバー枠

    # 3. プレイヤー情報
    text_php = FONT.render(f"HP: {p_hp}/30", True, WHITE)
    screen.blit(text_php, (50, 370))
    
    # 攻撃ストック
    text_stA = FONT.render(f"ATK: {stockA}", True, WHITE)
    screen.blit(text_stA, (50, 450)) 

    # 防御ストック
    text_stD = FONT.render(f"DEF: {stockD}", True, WHITE)
    screen.blit(text_stD, (50, 480)) 


def draw_battleCommand(screen, btn_draw_rect, btn_attack_rect):
    # ドローボタン
    pygame.draw.rect(screen, BLUE, btn_draw_rect)
    text_d = FONT_BIG.render("DRAW", True, WHITE)
    screen.blit(text_d, (btn_draw_rect.x + 20, btn_draw_rect.y + 10))

    # 攻撃ボタン
    pygame.draw.rect(screen, RED, btn_attack_rect)
    text_c = FONT_BIG.render("ATTACK", True, WHITE)
    screen.blit(text_c, (btn_attack_rect.x + 10, btn_attack_rect.y + 10))


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