import pygame
import PARAMETER
import PbattleC
import PbattleG

def battle_loop(screen, stage_num, player_hp):
    clock = pygame.time.Clock()
    
    # 敵パラメータの読み込み
    enemy_data = PARAMETER.ENEMY_STATS[stage_num - 1]
    e_hp = enemy_data["hp"]
    e_max_hp = e_hp
    e_power = enemy_data["power"]

    # バトル初期状態
    stockA = 0
    stockD = 0
    deck = PbattleC.init_deck()
    logs = ["Battle Start!"]
    last_card = None
    
    running = True
    result = "running" # win, lose, running

    while running:
        # --- イベント処理 ---
        action = None # "draw", "exec"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    action = "draw"
                if event.key == pygame.K_RETURN:
                    action = "exec"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 描画関数からボタンの座標を取得して判定は少し複雑になるので
                # 簡易的にマウス座標と決め打ち座標で判定
                mx, my = pygame.mouse.get_pos()
                if 700 <= mx <= 900:
                    if 400 <= my <= 460:
                        action = "draw"
                    elif 480 <= my <= 540:
                        action = "exec"

        # --- ロジック反映 ---
        if action == "draw":
            card, stockA, stockD, is_skull, deck = PbattleC.draw_card(deck, stockA, stockD)
            last_card = card
            if is_skull:
                logs.append("SKULL! Stocks Lost & Enemy Turn!")
                # ドクロ強制ターンエンド処理
                dmg = PbattleC.calc_enemy_damage(e_power, 0) # ガード0で受ける
                player_hp -= dmg
                logs.append(f"Enemy Attack! {dmg} dmg taken.")
            else:
                c_name = "Sword" if card == PARAMETER.CARD_SWORD else "Guard"
                logs.append(f"Draw {c_name}!")

        elif action == "exec":
            # プレイヤー攻撃
            dmg_to_enemy = PbattleC.calc_player_damage(stockA)
            e_hp -= dmg_to_enemy
            logs.append(f"Attack! {dmg_to_enemy} dmg to Enemy.")
            
            # リセット
            stockA = 0 
            
            # 敵が生きていれば反撃
            if e_hp > 0:
                dmg_to_player = PbattleC.calc_enemy_damage(e_power, stockD)
                player_hp -= dmg_to_player
                stockD = 0 # ガードは使い捨て
                if dmg_to_player > 0:
                    logs.append(f"Enemy Attack! {dmg_to_player} dmg taken.")
                else:
                    logs.append("Perfect Guard!")

        # --- 判定 ---
        if e_hp <= 0:
            result = "win"
            running = False
        elif player_hp <= 0:
            result = "lose"
            running = False

        # --- 描画 ---
        PbattleG.draw_battle_screen(screen, stage_num, player_hp, e_hp, e_max_hp, stockA, stockD, logs, last_card)
        pygame.display.update()
        clock.tick(30)

    return result, player_hp