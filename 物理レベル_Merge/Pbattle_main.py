import pygame
import sys
import Ptitle
import Pmap
import Pbattle_main
import PbattleG
import PbattleC
import Pparameter

# 文字を書くための「筆（フォント）」を用意
font = pygame.font.Font(None, 50) 
font2 = pygame.font.Font(None, 100)


# ★全体を関数にする！
def run_battle(encount):
    
    #マクロからの初期化
    enemy_hp = Pparameter.ENEMY_MAX_HP
    player_hp = Pparameter.PLAYER_MAX_HP
    deck = Pparameter.DECK_LIST.copy()
    
    # バトル中に変わるパラメータ
    stock_attack = 0 
    stock_defence = 0 
    #current_logs = ["----- バトル開始 -----"] # ★ログを入れる箱

    # === バトルループ ===
    while True:
        # --- 2. 表示 (View) ---
        PbattleG.encountBar(encount)
        PbattleG.draw_battleStatus(enemy_hp, player_hp, stock_attack, stock_defence)
        # ★ここでログを表示する！
        #PbattleG.draw_logs(current_logs)
        PbattleG.draw_battleCommand()

        # --- 3. 入力 (Input) ---
        # LbattleGのメッセージを使って入力を待つ
        command = input(PbattleG.draw_wait())
        print("") 