import pygame
import PARAMETER

pygame.font.init()
FONT_L = pygame.font.Font(None, 60)
FONT_M = pygame.font.Font(None, 40)
FONT_S = pygame.font.Font(None, 30)
FONT50 = pygame.font.Font(None, 50)


# カードの画像
IMG_SWORD = pygame.transform.scale(pygame.image.load("assets/SwordCard.png"), (100, 150))
IMG_SHIELD = pygame.transform.scale(pygame.image.load("assets/ShieldCard.png"), (100, 150))
IMG_SKULL = pygame.transform.scale(pygame.image.load("assets/Skull.png"), (100, 150))

# 敵の画像
IMG_ENEMY_RAW = pygame.image.load("assets/Enemy.png")
IMG_BOSS_RAW = pygame.image.load("assets/Boss.png")


def draw_battle_screen(screen, stage_num, p_hp, e_hp, e_max_hp, stockA, stockD, logs, last_card):
    screen.fill((30, 30, 40)) # 背景色

    #ヘッダー情報のテキスト描画
    if stage_num == 1 or stage_num == 2:
        type_enemy = 'Normal Enemy'
    if stage_num == 3:
        type_enemy = 'Boss'

    info_str2 = f"STAGE: {stage_num}          vs {type_enemy}"
    info_text = FONT50.render(info_str2, True, PARAMETER.WHITE)
    screen.blit(info_text, (90, 20))

    info_str2 = f"Enemy HP: {e_hp} / {e_max_hp}   Player HP: {p_hp} / {PARAMETER.PLAYER_MAX_HP}"
    info_text2 = FONT50.render(info_str2, True, PARAMETER.WHITE)
    screen.blit(info_text2, (30, 70))

    #剣のカードを3枚ごとのボーナスダメージを表示
    atk_text = FONT_L.render(f"ATK Stock: {stockA}", True, PARAMETER.RED)
    screen.blit(atk_text, (700, 30))
    
    bonus_val = 2 * (stockA // 3)
    if bonus_val > 0:
        bonus_str = f"Bonus! +{bonus_val}"
        bonus_text = FONT_M.render(bonus_str, True, (255, 215, 0)) 
        screen.blit(bonus_text, (700, 80))

    # 敵の描画
    enemy_center_x = PARAMETER.SCREEN_WIDTH // 2
    enemy_center_y = 200
    
    if stage_num == 3: # ボスの敵
        enemy_w, enemy_h = 200, 200 # 少し大きく
        use_img = IMG_BOSS_RAW
    else: # 普通の敵
        enemy_w, enemy_h = 150, 150
        use_img = IMG_ENEMY_RAW

    # 画像を指定サイズにリサイズ
    current_enemy_img = pygame.transform.scale(use_img, (enemy_w, enemy_h))
    
    # 画像の中心を計算して配置
    img_rect = current_enemy_img.get_rect(center=(enemy_center_x, enemy_center_y))
    screen.blit(current_enemy_img, img_rect)


    # 最後に引いたカードの表示
    # 表示位置
    center_x = 910
    center_y = 280
    
    # 枠線だけ描くためのRect
    card_rect = pygame.Rect(0, 0, 100, 150)
    card_rect.center = (center_x, center_y)

    target_img = None
    
    if last_card == PARAMETER.CARD_SWORD:
        target_img = IMG_SWORD
    elif last_card == PARAMETER.CARD_GUARD:
        target_img = IMG_SHIELD
    elif last_card == PARAMETER.CARD_SKULL:
        target_img = IMG_SKULL

    if target_img is not None:
        # 画像の中心を合わせて表示
        img_rect = target_img.get_rect(center=(center_x, center_y))
        screen.blit(target_img, img_rect)
    else:
        # カードがない時(Ready)は枠だけ
        pygame.draw.rect(screen, PARAMETER.GRAY, card_rect, border_radius=5)
        text = FONT_M.render("Ready", True, PARAMETER.WHITE)
        screen.blit(text, text.get_rect(center=card_rect.center))


    # ログの表示
    log_area_rect = pygame.Rect(10, 480, 620, 120)
    pygame.draw.rect(screen, (50, 50, 60), log_area_rect, border_radius=5)
    pygame.draw.rect(screen, PARAMETER.WHITE, log_area_rect, 2, border_radius=5)
    
    y = 500
    for log in logs[-2:]:
        t = FONT50.render(log, True, (200, 200, 200))
        screen.blit(t, (20, y))
        y += 45

    # ボタンの描画
    btn_draw_rect = pygame.Rect(650, 400, 300, 60)
    btn_exec_rect = pygame.Rect(650, 480, 300, 60)

    pygame.draw.rect(screen, (200, 150, 50), btn_draw_rect, border_radius=5)
    t_draw = FONT_M.render("DRAW (Space)", True, PARAMETER.BLACK)
    screen.blit(t_draw, (btn_draw_rect.centerx - t_draw.get_width()//2, btn_draw_rect.centery - t_draw.get_height()//2))

    pygame.draw.rect(screen, (50, 200, 50), btn_exec_rect, border_radius=5)
    t_exec = FONT_M.render("ATTACK (Enter)", True, PARAMETER.BLACK)
    screen.blit(t_exec, (btn_exec_rect.centerx - t_exec.get_width()//2, btn_exec_rect.centery - t_exec.get_height()//2))

    return btn_draw_rect, btn_exec_rect


# 手札を描画する関数
CARD_WIDTH = 100
CARD_HEIGHT = 150
CARD_MARGIN = 20

def draw_player_hand(screen, player_hand):
    display_hand = player_hand[-5:] 

    total_width = len(display_hand) * CARD_WIDTH + (len(display_hand) - 1) * CARD_MARGIN
    start_x = 30
    current_x = start_x
    card_y = 320 

    for card_type in display_hand: 
        # 表示位置の中心を計算
        center_x = current_x + CARD_WIDTH // 2
        center_y = card_y + CARD_HEIGHT // 2
        
        target_img = None
        
        if card_type == PARAMETER.CARD_SWORD:
            target_img = IMG_SWORD
        elif card_type == PARAMETER.CARD_GUARD:
            target_img = IMG_SHIELD
        elif card_type == PARAMETER.CARD_SKULL:
            target_img = IMG_SKULL
            
        if target_img is not None:
            img_rect = target_img.get_rect(center=(center_x, center_y))
            screen.blit(target_img, img_rect)
        
        current_x += CARD_WIDTH + CARD_MARGIN