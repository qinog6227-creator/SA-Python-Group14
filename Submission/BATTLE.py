import pygame
import PARAMETER

pygame.font.init()
FONT_L = pygame.font.Font(None, 60)
FONT_M = pygame.font.Font(None, 40)
FONT_S = pygame.font.Font(None, 30)

FONT50 = pygame.font.Font(None, 50)

def draw_battle_screen(screen, stage_num, p_hp, e_hp, e_max_hp, stockA, stockD, logs, last_card):
    screen.fill((30, 30, 40)) # 背景色

    # --- ヘッダー情報のテキスト描画 ---
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


    # --- 3枚ごとのbonus攻撃力ステータス（溜め量）のテキスト描画 ---
    
    # 1. まずいつもの攻撃ストックを表示
    atk_text = FONT_L.render(f"ATK Stock: {stockA}", True, PARAMETER.RED)
    screen.blit(atk_text, (700, 30))
    
    # ★追加: ボーナス表示のロジック
    # 「3枚ごとにボーナス」の計算をして、0より大きければ表示する
    bonus_val = 2 * (stockA // 3)

    if bonus_val > 0:
        # ボーナスがある時だけ表示
        # 色は目立つようにゴールド (255, 215, 0) にする
        bonus_str = f"Bonus! +{bonus_val}"
        bonus_text = FONT_M.render(bonus_str, True, (255, 215, 0)) 
        
        # ATK Stock のすぐ下 (Y=80) に表示
        screen.blit(bonus_text, (700, 80))


# --- 敵の描画 (図形) ---
    
    # 敵の基本位置 (画面中央より少し上)
    enemy_center_x = PARAMETER.SCREEN_WIDTH // 2
    enemy_center_y = 200
    
    # ステージによって敵の見た目を変える
    if stage_num == 3: # ボス (大きく、赤い)
        enemy_w, enemy_h = 190, 190
        enemy_color = (200, 50, 50) # 赤
        eye_color = (255, 255, 0)   # 黄色い目
    else: # ザコ敵 (小さく、緑っぽい)
        enemy_w, enemy_h = 120, 120
        enemy_color = (50, 150, 50) # 緑
        eye_color = PARAMETER.WHITE # 白い目

    # 敵の体 (四角形) を描画
    # 中心座標から左上座標を計算してRectを作る
    enemy_rect = pygame.Rect(
        enemy_center_x - enemy_w // 2, 
        enemy_center_y - enemy_h // 2, 
        enemy_w, 
        enemy_h
    )
    
    # 体を描く
    pygame.draw.rect(screen, enemy_color, enemy_rect, border_radius=20)
    # 白い枠線をつける
    pygame.draw.rect(screen, PARAMETER.WHITE, enemy_rect, 5, border_radius=20)

    # 目を描く (ちょっとキャラっぽく)
    eye_size = enemy_w // 5
    # 左目
    pygame.draw.circle(screen, eye_color, (enemy_center_x - eye_size, enemy_center_y - eye_size), eye_size // 2)
    # 右目
    pygame.draw.circle(screen, eye_color, (enemy_center_x + eye_size, enemy_center_y - eye_size), eye_size // 2)



    # --- ステータス（溜め量）のテキスト描画 ---
    # 攻撃溜め
    atk_text = FONT_L.render(f"ATK Stock: {stockA}", True, PARAMETER.RED)
    screen.blit(atk_text, (700, 30))
    
    # ★変更: DEF Stock の表示を削除 (もう存在しないため)
    # def_text = FONT_L.render(f"DEF Stock: {stockD}", True, PARAMETER.BLUE)
    # screen.blit(def_text, (700, 80))

    # --- 最後に引いたカードの表示 ---
    card_rect = pygame.Rect(850, 190, 120, 180)
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


    # ログ全体を囲むエリアを定義
    # 左上の座標 (20, 390) から、幅 620、高さ 100 のエリア
    log_area_rect = pygame.Rect(10, 480, 620, 120)
    
    # ログエリアの背景と枠線を描画
    pygame.draw.rect(screen, (50, 50, 60), log_area_rect, border_radius=5) # 背景（少し暗い色）
    pygame.draw.rect(screen, PARAMETER.WHITE, log_area_rect, 2, border_radius=5) # 枠線 (太さ2)

    # --- ログ表示 ---
    y = 500
    for log in logs[-2:]: # 最新3件
        t = FONT50.render(log, True, (200, 200, 200))
        screen.blit(t, (20, y))
        y += 45

    # --- ボタン描画 ---
    # ボタン位置と大きさの定義 (rectを返す)　(x,y,w,h)を含んだタプル
    btn_draw_rect = pygame.Rect(650, 400, 300, 60)
    btn_exec_rect = pygame.Rect(650, 480, 300, 60)

    # ドローボタン
    pygame.draw.rect(screen, (200, 150, 50), btn_draw_rect, border_radius=5)
    t_draw = FONT_M.render("DRAW (Space)", True, PARAMETER.BLACK)
    screen.blit(t_draw, (btn_draw_rect.centerx - t_draw.get_width()//2, btn_draw_rect.centery - t_draw.get_height()//2))

    # 実行ボタン
    pygame.draw.rect(screen, (50, 200, 50), btn_exec_rect, border_radius=5)
    t_exec = FONT_M.render("ATTACK (Enter)", True, PARAMETER.BLACK)
    screen.blit(t_exec, (btn_exec_rect.centerx - t_exec.get_width()//2, btn_exec_rect.centery - t_exec.get_height()//2))

    return btn_draw_rect, btn_exec_rect

#カードを並べて表示する
CARD_WIDTH = 100
CARD_HEIGHT = 150
CARD_MARGIN = 20 # カード間のマージン

def draw_player_hand(screen, player_hand):
    # 1. ここで「最新の5枚」だけの新しいリストを作る
    display_hand = player_hand[-5:] 

    # 2. 幅の計算も「display_hand (5枚)」で行う
    total_width = len(display_hand) * CARD_WIDTH + (len(display_hand) - 1) * CARD_MARGIN
    start_x = 30
    
    current_x = start_x
    
    # ログウィンドウ(Y=480)の上に配置 (480 - 150 - 10 = 320)
    card_y = 320 

    # 一番重要
    # 「player_hand」ではなく、「display_hand」を使ってループする
    for card_type in display_hand: 
        card_rect = pygame.Rect(current_x, card_y, CARD_WIDTH, CARD_HEIGHT)
        color = PARAMETER.GRAY
        label = "?"
        
        if card_type == PARAMETER.CARD_SWORD:
            color = PARAMETER.RED
            label = "SWO"
        elif card_type == PARAMETER.CARD_GUARD:
            color = PARAMETER.BLUE
            label = "SHI"
        elif card_type == PARAMETER.CARD_SKULL:
            color = (50, 50, 50)
            label = "SKL"
            
        pygame.draw.rect(screen, color, card_rect, border_radius=5)
        pygame.draw.rect(screen, PARAMETER.WHITE, card_rect, 2, border_radius=5)
        
        label_surf = FONT_S.render(label, True, PARAMETER.WHITE)
        screen.blit(label_surf, label_surf.get_rect(center=card_rect.center))
        
        current_x += CARD_WIDTH + CARD_MARGIN
    
    # --- 案内テキスト (任意) ---
    # info_text = FONT_S.render("Cards (Max 5 shown)", True, PARAMETER.WHITE)
    # screen.blit(info_text, (start_x, card_y - 30))