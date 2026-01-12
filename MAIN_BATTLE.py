import pygame
import PARAMETER
import CALC
import BATTLE

def battle_loop(screen, stage_num, player_hp):
    clock = pygame.time.Clock()
    
    # 敵パラメータの読み込み
    enemy_data = PARAMETER.ENEMY_STATS[stage_num - 1]
    e_hp = enemy_data["hp"]
    e_max_hp = e_hp
    e_power = enemy_data["power"]

    # バトル初期状態
    stockA = 0
    deck = CALC.init_deck()
    logs = ["Battle Start!"]
    last_card = None
    player_hand = [] # 手札リストをここで初期化
    
    running = True
    result = "running" # win, lose, running

    while running:
        # イベント処理
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

        # ロジック反映
        if action == "draw":
            card, stockA, is_skull, deck = CALC.draw_card(deck, stockA)
            
            last_card = card
            player_hand.append(card)
            
            if is_skull:
                logs.append("SKULL! Stocks Lost & Enemy Turn!")
                dmg = CALC.calc_enemy_damage(e_power) 
                player_hp -= dmg
                logs.append(f"Enemy Attack! {dmg} dmg taken.")
            else:
                if card == PARAMETER.CARD_SWORD:
                    logs.append(f"Draw Sword! ATK UP!")
                
                # 盾のカードを引いたときの処理
                elif card == PARAMETER.CARD_GUARD:
                    heal_val = PARAMETER.GUARD_VAL # HPを1回復
                    player_hp += heal_val
                    logs.append(f"Draw Shield! HP +{heal_val}!")

        elif action == "exec":
            # プレイヤー攻撃
            dmg_to_enemy = CALC.calc_player_damage(stockA)
            e_hp -= dmg_to_enemy
            logs.append(f"Attack! {dmg_to_enemy} dmg to Enemy.")
            
            stockA = 0 
            player_hand = [] 
            last_card = None
            
            # 敵の反撃
            if e_hp > 0:
                dmg_to_player = CALC.calc_enemy_damage(e_power)
                player_hp -= dmg_to_player
                logs.append(f"Enemy Attack! {dmg_to_player} dmg taken.")


        # 勝敗の判定
        if e_hp <= 0:
            result = "win"
            running = False
        elif player_hp <= 0:
            result = "lose"
            running = False

        #描画
        BATTLE.draw_battle_screen(screen, stage_num, player_hp, e_hp, e_max_hp, stockA, 0, logs, last_card)

        # 関数を呼び出し、手札リストを渡す
        BATTLE.draw_player_hand(screen, player_hand)
        pygame.display.update()
        clock.tick(30)

    return result, player_hp