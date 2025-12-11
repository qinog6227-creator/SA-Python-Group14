import pygame
import sys
import PbattleC
import PbattleG
import Pparameter

# 1. 準備（画用紙を作る）
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 幅800, 高さ600
pygame.display.set_caption("サダメドロー")

# 文字を書くための「筆（フォント）」を用意
font = pygame.font.Font(None, 50) 
font2 = pygame.font.Font(None, 100)

# --- 関数定義 ---
def run_battle(encount):
    # ★変数はこの関数の中で初期化する（バトルのたびにリセット）
    enemy_hp = Pparameter.ENEMY_MAX_HP
    player_hp = Pparameter.PLAYER_MAX_HP
    deck = Pparameter.DECK_LIST.copy()
    
    # バトル中に変わるパラメータ
    stock_attack = 0 
    stock_defence = 0 
    current_logs = ["----- バトル開始 -----"] 

    # ★ボタンの場所（Rect）をここで定義しておく
    # (描画とクリック判定の両方で使うため)
    rect_draw = pygame.Rect(50, 500, 150, 50)
    rect_attack = pygame.Rect(250, 500, 150, 50)

    # === 2. メインループ（ここが紙芝居） ===
    while True:
        # (終了ボタンが押されたら終わる処理)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- 2. 表示 (View) ---
        # ★重要！ 全部最初の引数に 'screen' を渡す！
        
        PbattleG.encount_bar(screen, encount)
        
        PbattleG.draw_battleStatus(screen, enemy_hp, player_hp, stock_attack, stock_defence)
        
        PbattleG.draw_logs(screen, current_logs)
        
        # ボタンには screen と、さっき作ったRectを渡す
        PbattleG.draw_battleCommand(screen, rect_draw, rect_attack)

        pygame.display.flip()
        # ★これがないとPCが全力疾走して熱くなる
        pygame.time.Clock().tick(60) 

# --- テスト実行用 ---
if __name__ == '__main__':
    run_battle(1)