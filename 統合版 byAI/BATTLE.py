import pygame
import PARAMETER

pygame.font.init()
FONT_L = pygame.font.Font(None, 60)
FONT_M = pygame.font.Font(None, 40)
FONT_S = pygame.font.Font(None, 30)

def draw_battle_screen(screen, stage_num, p_hp, e_hp, e_max_hp, stockA, stockD, logs, last_card):
    screen.fill((30, 30, 40)) # 背景色

    # --- 敵画像の描画 (追加) ---
    enemy_img = PARAMETER.IMG_ENEMY_BATTLE
    # 画面上部中央に配置 (Y座標を120くらいに設定)
    enemy_rect = enemy_img.get_rect(center=(PARAMETER.SCREEN_WIDTH//2, 120))
    screen.blit(enemy_img, enemy_rect)

    # --- ヘッダー情報の描画 ---
    # 画像と被らないように位置を調整 (Y=30 から Y=230 へ変更)
    info_str = f"STAGE: {stage_num}   Enemy HP: {e_hp}/{e_max_hp}   Player HP: {p_hp}/{PARAMETER.PLAYER_MAX_HP}"
    info_text = FONT_M.render(info_str, True, PARAMETER.WHITE)
    screen.blit(info_text, (50, 230))

    # --- ステータス（溜め量） ---
    # 位置を少し調整 Y=150, 220 -> Y=280, 350
    atk_text = FONT_L.render(f"ATK Stock: {stockA}", True, PARAMETER.RED)
    screen.blit(atk_text, (100, 280))
    def_text = FONT_L.render(f"DEF Stock: {stockD}", True, PARAMETER.BLUE)
    screen.blit(def_text, (100, 350))

    # --- 最後に引いたカードの表示 ---
    # 位置を少し調整 Y=150 -> Y=280
    card_rect = pygame.Rect(450, 280, 120, 180)
    color = PARAMETER.GRAY
    label = "Ready"
    
    if last_card == PARAMETER.CARD_SWORD:
        color = PARAMETER.RED
        label = "SWORD"
    elif last_card == PARAMETER.CARD_GUARD:
        color = PARAMETER.BLUE
        label = "GUARD"
    elif last_card == PARAMETER.CARD_SKULL:
        color = (50, 50, 50)
        label = "SKULL!!"

    pygame.draw.rect(screen, color, card_rect, border_radius=10)
    pygame.draw.rect(screen, PARAMETER.WHITE, card_rect, 3, border_radius=10)
    
    label_surf = FONT_M.render(label, True, PARAMETER.WHITE)
    screen.blit(label_surf, (card_rect.centerx - label_surf.get_width()//2, card_rect.centery - label_surf.get_height()//2))

    # --- ログ表示 ---
    # 位置を少し調整 Y=400 -> Y=480
    y = 480
    for log in logs[-4:]: # 表示数を5から4に減らして調整
        t = FONT_S.render(log, True, (200, 200, 200))
        screen.blit(t, (50, y))
        y += 25

    # --- ボタン描画 ---
    # 位置を少し調整 Y=400, 480 -> Y=480, 550
    btn_draw_rect = pygame.Rect(700, 480, 200, 50)
    btn_exec_rect = pygame.Rect(700, 540, 200, 50)

    # ドローボタン
    pygame.draw.rect(screen, (200, 150, 50), btn_draw_rect, border_radius=5)
    t_draw = FONT_M.render("DRAW (Space)", True, PARAMETER.BLACK)
    screen.blit(t_draw, (btn_draw_rect.centerx - t_draw.get_width()//2, btn_draw_rect.centery - t_draw.get_height()//2))

    # 実行ボタン
    pygame.draw.rect(screen, (50, 200, 50), btn_exec_rect, border_radius=5)
    t_exec = FONT_M.render("ATTACK (Enter)", True, PARAMETER.BLACK)
    screen.blit(t_exec, (btn_exec_rect.centerx - t_exec.get_width()//2, btn_exec_rect.centery - t_exec.get_height()//2))

    return btn_draw_rect, btn_exec_rect