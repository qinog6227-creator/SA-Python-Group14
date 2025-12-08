import random
import Lparameter

#######物理レベル#######
def show_battleStatus(enemy_hp, player_hp, stockA, stockG): 
    print("----------------------------------")
    print(f"敵のHP    : {enemy_hp}")
    print(f"プレイヤー: {player_hp}")
    print(f"溜め攻撃力: {stockA}")
    print(f"溜めガード: {stockG}")

def show_battleCommand():
    print("-----コマンド-----")
    print("d: ドロー継続")
    print("c: 攻撃実行！")
    print("q: ドロー終了 (敵のターンへ)")



######論理レベル######
def logic_draw(deck, player_hp, stockA, stockG):
    logs = [] # 報告書（ログ）を入れる箱
    force_end = False # 強制終了フラグ

    # 山札補充処理
    if len(deck) == 0:
        deck = Lparameter.DECK_LIST.copy()
        logs.append("山札補充！")

    # ドロー処理
    card = random.choice(deck)
    deck.remove(card)

    # カードの効果計算
    if card == 1:
        stockA += Lparameter.SWORD_POWER
        logs.append("【剣】を引いた！ 攻撃力をチャージ！")
        
    elif card == 2:
        player_hp += Lparameter.HEAL_VALUE
        if player_hp > Lparameter.PLAYER_MAX_HP:
            player_hp = Lparameter.PLAYER_MAX_HP
        logs.append(f"【ガード】を引いた！ HPが {Lparameter.HEAL_VALUE} 回復した！")
        
    elif card == 3:
        stockA = 0
        force_end = True
        logs.append("ドクロ】... 溜め攻撃没収 & 強制終了！")

    # 計算結果とログをまとめて返す（多値返却）
    return deck, player_hp, stockA, force_end, logs

def logic_player_attack(enemy_hp, stockA):
    logs = []
    
    # ダメージ計算
    damage = int(stockA * 2) 
    enemy_hp -= damage
    
    logs.append("攻撃実行！")
    logs.append(f"敵に {damage} ダメージを与えた！")
    
    return enemy_hp, logs


def logic_enemy_turn(player_hp):
    logs = []
    
    # ダメージ計算
    damage = Lparameter.ENEMY_POWER
    player_hp -= damage
    
    logs.append("\n敵の攻撃！")
    logs.append(f"{damage} ダメージを受けた！")
    
    return player_hp, logs

# ==========================================
# 3. メインループ (Main Controller)
#    - 入力と出力を管理し、ロジックを呼び出す
# ==========================================

def battle():
    player_hp = Lparameter.PLAYER_MAX_HP
    enemy_hp = Lparameter.ENEMY_MAX_HP
    deck = Lparameter.DECK_LIST.copy()
    stock_attack = 0 
    
    print("敵が現れた！")

    while True:
        # --- 表示フェーズ (Render) ---
        show_battleStatus(enemy_hp, player_hp, stock_attack)
        show_battleCommand()

        # --- 入力フェーズ (Input) ---
        command = input("コマンドを入力してください: ")
        print("") # 改行

        # --- ロジックフェーズ (Update) ---
        
        # パターンA：ドロー
        if command == 'd':
            # ロジックを呼ぶ（計算丸投げ）
            deck, player_hp, stock_attack, force_end, logs = logic_draw(deck, player_hp, stock_attack)
            
            # 帰ってきたログを表示する（ここが物理レベルの仕事）
            for msg in logs:
                print(msg)

            # 強制終了フラグが立っていたら q へ
            if force_end:
                command = 'q'

        # パターンB：攻撃実行
        if command == 'c':
            # ロジックを呼ぶ
            enemy_hp, logs = logic_player_attack(enemy_hp, stock_attack)
            stock_attack = 0 # リセット
            
            # ログ表示
            for msg in logs:
                print(msg)
                
            command = 'q' # 敵のターンへ

        # パターンC：敵のターン
        if command == 'q':
            if enemy_hp > 0:
                # ロジックを呼ぶ
                player_hp, logs = logic_enemy_turn(player_hp)
                
                # ログ表示
                for msg in logs:
                    print(msg)
            
        # --- 勝敗判定 ---
        if enemy_hp <= 0:
            print("\n******* 勝ち！ *******") 
            return "win"  
        
        if player_hp <= 0:
            print("\n*** 負け... ***")
            return "lose"

if __name__ == "__main__":
    battle()