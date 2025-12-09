import pygame #パイゲーム実行
import sys
import LbattleG #グラフィック
import LbattleC #計算
import Lparameter #マクロ

# ★全体を関数にする！
def run_battle(screen, encount):
    
    #マクロからの初期化
    enemy_hp = Lparameter.ENEMY_MAX_HP
    player_hp = Lparameter.PLAYER_MAX_HP
    deck = Lparameter.DECK_LIST.copy()
        
    # バトル中に変わるパラメータ
    stock_attack = 0 
    stock_defence = 0 
    current_logs = ["----- バトル開始 -----"] # ★ログを入れる箱
    # ボタンの場所を決めておく（透明な四角形）
    BTN_DRAW = pygame.Rect(100, 400, 150, 50)   # ドローボタン
    BTN_ATTACK = pygame.Rect(300, 400, 150, 50) # 攻撃ボタン


    # === バトルループ ===
    while True:
    # 1. 画面を一度真っ黒にリセット（塗りつぶし）
        screen.fill((0, 0, 0))

        # 2. グラフィック担当に描いてもらう (screenを渡す)
        LbattleG.draw_battleStatus(screen, enemy_hp, ...)
        LbattleG.draw_logs(screen, current_logs)
        
        # (仮) ボタンの場所がわかるように四角を描く
        pygame.draw.rect(screen, (0, 255, 0), BTN_DRAW)
        pygame.draw.rect(screen, (255, 0, 0), BTN_ATTACK)

        # ★重要：描いたものをモニターに反映！
        pygame.display.update()

        # 3. 入力処理 (input ではなく event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # クリックされたら？
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # ドローボタンの上なら？ (input('d') の代わり)
                if BTN_DRAW.collidepoint(event.pos):
                    # ★計算ロジック(LbattleC)はそのまま使える！！！
                    # ★ 計算結果を「全て」受け取る！
                    deck, player_hp, stock_attack, stock_defence, force_end, new_logs = \
                    LbattleC.calc_draw(deck, player_hp, stock_attack, stock_defence)
            
                    # ★ ログを更新（これで次のループで表示される）
                    current_logs = new_logs
                    #ドクロ（強制終了）なら q (敵のターン) へ
                    if force_end:
                        command = 'q'


                # 攻撃ボタンの上なら？ (input('c') の代わり)
                elif BTN_ATTACK.collidepoint(event.pos):
                    # ★ここもそのまま！
                    enemy_hp, ... = LbattleC.calc_player_attack(...)
                    # ...











        

        # B. 攻撃処理
        elif command == 'c':
            enemy_hp, new_logs = \
                LbattleC.calc_player_attack(enemy_hp, stock_attack)
            
            current_logs = new_logs
            stock_attack = 0 # 攻撃したのでリセット
            command = 'q' # 攻撃後は敵のターンへ

        # C. 敵のターン
        if command == 'q':
            if enemy_hp > 0:
                # ステージ数は仮で「1」
                player_hp, enemy_logs = \
                    LbattleC.calc_enemy_turn(player_hp, stock_defence, 1)
                
                # ログを追記する
                current_logs.extend(enemy_logs)
                stock_defence = 0 # ガードを使ったのでリセット

        # --- 5. 勝敗判定 ---
        if enemy_hp <= 0:
            # 1. 勝利メッセージをログに追加
            current_logs.append("\n>> 勝利！おめでとう！") 
            
            # 2. 最後にログを描画して、メッセージを表示させる
            LbattleG.draw_logs(current_logs)
            
            return "win"
        
        if player_hp <= 0:
            # 1. 敗北メッセージをログに追加
            current_logs.append("\n>> 敗北... ゲームオーバー。")
            
            # 2. 最後にログを描画して、メッセージを表示させる
            LbattleG.draw_logs(current_logs)
            
            return "lose"
    

# このファイルを直接実行した時だけ動くテスト用コード
if __name__ == "__main__":
    run_battle()