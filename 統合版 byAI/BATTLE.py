import pygame
import Pparameter

pygame.font.init()
FONT_L = pygame.font.Font(None, 60)
FONT_M = pygame.font.Font(None, 40)
FONT_S = pygame.font.Font(None, 30)

def draw_battle_screen(screen, stage_num, p_hp, e_hp, e_max_hp, stockA, stockD, logs, last_card):
    screen.fill((30, 30, 40)) # 背景色

    # --- ヘッダー情報の描画 ---
    info_str = f"STAGE: {stage_num}   Enemy HP: {e_hp}/{e_max_hp}   Player HP: {p_hp}/{Pparameter.PLAYER_MAX_HP}"
    info_text = FONT_M.render(info_str, True, Pparameter.WHITE)
    screen.blit(info_text, (50, 30))

    # --- ステータス（溜め量） ---
    # 攻撃溜め
    atk_text = FONT_L.render(f"ATK Stock: {stockA}", True, Pparameter.RED)
    screen.blit(atk_text, (100, 150))
    # 防御溜め
    def_text = FONT_L.render(f"DEF Stock: {stockD}", True, Pparameter.BLUE)
    screen.blit(def_text, (100, 220))

    # --- 最後に引いたカードの表示 ---
    card_rect = pygame.Rect(450, 150, 120, 180)
    color = Pparameter.GRAY
    label = "Ready"
    
    if last_card == Pparameter.CARD_SWORD:
        color = Pparameter.RED
        label = "SWORD"
    elif last_card == Pparameter.CARD_GUARD:
        color = Pparameter.BLUE
        label = "GUARD"
    elif last_card == Pparameter.CARD_SKULL:
        color = (50, 50, 50)
        label = "SKULL!!"

    pygame.draw.rect(screen, color, card_rect, border_radius=10)
    pygame.draw.rect(screen, Pparameter.WHITE, card_rect, 3, border_radius=10)
    
    label_surf = FONT_M.render(label, True, Pparameter.WHITE)
    screen.blit(label_surf, (card_rect.centerx - label_surf.get_width()//2, card_rect.centery - label_surf.get_height()//2))

    # --- ログ表示 ---
    y = 400
    for log in logs[-5:]: # 最新5件
        t = FONT_S.render(log, True, (200, 200, 200))
        screen.blit(t, (50, y))
        y += 25

    # --- ボタン描画 ---
    # ボタン位置定義 (rectを返す)
    btn_draw_rect = pygame.Rect(700, 400, 200, 60)
    btn_exec_rect = pygame.Rect(700, 480, 200, 60)

    # ドローボタン
    pygame.draw.rect(screen, (200, 150, 50), btn_draw_rect, border_radius=5)
    t_draw = FONT_M.render("DRAW (Space)", True, Pparameter.BLACK)
    screen.blit(t_draw, (btn_draw_rect.centerx - t_draw.get_width()//2, btn_draw_rect.centery - t_draw.get_height()//2))

    # 実行ボタン
    pygame.draw.rect(screen, (50, 200, 50), btn_exec_rect, border_radius=5)
    t_exec = FONT_M.render("ATTACK (Enter)", True, Pparameter.BLACK)
    screen.blit(t_exec, (btn_exec_rect.centerx - t_exec.get_width()//2, btn_exec_rect.centery - t_exec.get_height()//2))

    return btn_draw_rect, btn_exec_rect