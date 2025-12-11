import pygame
import os

# --- 1. 準備：定数とフォント ---

pygame.font.init()

# フォント設定
FONT1 = pygame.font.Font(None, 40) 
FONT2 = pygame.font.Font(None, 80) 
FONT_LOG = pygame.font.Font(None, 24) 

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (70, 70, 70) 

# --- 2. 描画関数 ---

#何戦目かを表示
def draw_encountBar(screen, encount):
    text_title = FONT2.render(f"{encount}st Round", True, WHITE)
    screen.blit(text_title,(500, 30))

#HPなどを表示（元のまま）
def draw_battleStatus(screen, e_hp, p_hp, stockA, stockD): 
    text_bar = FONT1.render(f"----- Latest Imformation -----", True, WHITE)
    text_enemysta = FONT1.render(f"Enemy HP: {e_hp}", True, WHITE)
    text_playersta = FONT1.render(f"Player HP: {p_hp}", True, WHITE)
    text_stockA = FONT1.render(f"Stock Attack Card: {stockA}", True, WHITE)
    text_stockD = FONT1.render(f"Stock Defense Card: {stockD}", True, WHITE)
    
    screen.blit(text_bar, (50, 30))
    screen.blit(text_enemysta, (50, 70))
    screen.blit(text_playersta, (50, 110))
    screen.blit(text_stockA, (50, 150))
    screen.blit(text_stockD, (50, 190))

#コマンドを表示
def draw_battleCommand(screen):
    text_bar = FONT1.render(f"-----Command-----",True, WHITE)
    
    # Dキー
    draw_btn_rect = pygame.draw.rect(screen, GRAY, (470, 155, 230, 40), border_radius=5)
    text_drawing = FONT1.render("D key: draw Keeping!", True, WHITE)
    screen.blit(text_drawing, (480, 160))
    
    # Cキー
    text_carryOut = FONT1.render("C key: carry out owned card!", True, WHITE)
    screen.blit(text_carryOut, (480, 200))
    
    screen.blit(text_bar, (480, 120))

#カードを表示する
def draw_card(screen, card_list):
    
    card_num = len(card_list)
    one_set = 120
    start_x = 400 - ((one_set * card_num) // 2)

    for i, card_name in enumerate(card_list):
        x = start_x + (one_set * i)
        
        # 色決め (文字列でも数値でも対応)
        if card_name == "Attack" or card_name == 1:
            color = RED
        elif card_name == "Defense" or card_name == 2:
            color = BLUE   
        else:
            color = GREEN  

        pygame.draw.rect(screen, color, (x, 300, 100, 150), 0)


def draw_wait():
    return "COMMAND?"

#ログを表示する
def draw_logs(screen, logs):
    # ログ表示 (最新の3件を上から)
    start_y = 680
    display_logs = logs[-3:] 
    
    for msg in display_logs:
        text = FONT_LOG.render(msg, True, WHITE)
        screen.blit(text, (80, start_y))
        start_y += 25