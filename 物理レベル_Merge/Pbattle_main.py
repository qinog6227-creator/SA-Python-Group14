import pygame
import sys
import TITLE
import MAP
import MAIN_BATTLE
import BATTLE
import CALCURATE
import PARAMETER

# 文字を書くための「筆（フォント）」を用意
font = pygame.font.Font(None, 50) 
font2 = pygame.font.Font(None, 100)


# ★全体を関数にする！
def run_battle(encount):
    
    #マクロからの初期化
    enemy_hp = PARAMETER.ENEMY_MAX_HP
    player_hp = PARAMETER.PLAYER_MAX_HP
    deck = PARAMETER.DECK_LIST.copy()
    
    # バトル中に変わるパラメータ
    stock_attack = 0 
    stock_defence = 0 
    #current_logs = ["----- バトル開始 -----"] # ★ログを入れる箱

    # === バトルループ ===
    while True:
        # --- 2. 表示 (View) ---
        BATTLE.encountBar(encount)
        BATTLE.draw_battleStatus(enemy_hp, player_hp, stock_attack, stock_defence)
        # ★ここでログを表示する！
        BATTLE.draw_logs(current_logs)
        BATTLE.draw_battleCommand()

        # --- 3. 入力 (Input) ---
        # LbattleGのメッセージを使って入力を待つ
        command = input(BATTLE.draw_wait())
        print("") 