import sys
import MbattleG #グラフィック
import MbattleC #計算
import 物理レベルMarge.Mparameter as Mparameter #マクロ

# ★全体を関数にする！
def run_battle(encount):
    
    #マクロからの初期化
    enemy_hp = Mparameter.ENEMY_MAX_HP
    player_hp = Mparameter.PLAYER_MAX_HP
    deck = Mparameter.DECK_LIST.copy()
    
    # バトル中に変わるパラメータ
    stock_attack = 0 
    stock_defence = 0 
    current_logs = ["----- バトル開始 -----"] # ★ログを入れる箱

    # === バトルループ ===
    while True:
        # --- 2. 表示 (View) ---
        MbattleG.encount_bar(encount)
        MbattleG.draw_battleStatus(enemy_hp, player_hp, stock_attack, stock_defence)
        # ★ここでログを表示する！
        MbattleG.draw_logs(current_logs)
        MbattleG.draw_battleCommand()

        # --- 3. 入力 (Input) ---
        # LbattleGのメッセージを使って入力を待つ
        command = input(MbattleG.draw_wait())
        print("") 


        # --- 4. 計算 (Logic) ---
        # A. ドロー処理
        if command == 'd':
            # ★ 計算結果を「全て」受け取る！
            deck, player_hp, stock_attack, stock_defence, force_end, new_logs = \
                MbattleC.calc_draw(deck, player_hp, stock_attack, stock_defence)
            
            # ★ ログを更新（これで次のループで表示される）
            current_logs = new_logs
            
            # ドクロ（強制終了）なら q (敵のターン) へ
            if force_end:
                command = 'q'

        # B. 攻撃処理
        elif command == 'c':
            enemy_hp, new_logs = \
                MbattleC.calc_player_attack(enemy_hp, stock_attack)
            
            current_logs = new_logs
            stock_attack = 0 # 攻撃したのでリセット
            command = 'q' # 攻撃後は敵のターンへ

        # C. 敵のターン
        if command == 'q':
            if enemy_hp > 0:
                # ステージ数は仮で「1」
                player_hp, enemy_logs = \
                    MbattleC.calc_enemy_turn(player_hp, stock_defence, 1)
                
                # ログを追記する
                current_logs.extend(enemy_logs)
                stock_defence = 0 # ガードを使ったのでリセット

        # --- 5. 勝敗判定 ---
        if enemy_hp <= 0:
            # 1. 勝利メッセージをログに追加
            current_logs.append("\n>> 勝利！おめでとう！") 
            
            # 2. 最後にログを描画して、メッセージを表示させる
            MbattleG.draw_logs(current_logs)
            
            return "win"
        
        if player_hp <= 0:
            # 1. 敗北メッセージをログに追加
            current_logs.append("\n>> 敗北... ゲームオーバー。")
            
            # 2. 最後にログを描画して、メッセージを表示させる
            MbattleG.draw_logs(current_logs)
            
            return "lose"
    

# このファイルを直接実行した時だけ動くテスト用コード
if __name__ == "__main__":
    run_battle()