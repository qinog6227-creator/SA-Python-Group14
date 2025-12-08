import random
import Lparameter

# ==========================================
# 1. 物理レベル (View / Display)
#    - print は「ここだけ」に許された特権！
#    - 明日はここを draw_text に変えるだけ！
# ==========================================

def show_battleStatus(e_hp, p_hp, stockA): 
    print("----------------------------------")
    print(f"敵のHP    : {e_hp}")
    print(f"プレイヤー: {p_hp}")
    print(f"溜め攻撃力: {stockA}")

def show_battleCommand():
    print("-----コマンド-----")
    print("d: ドロー継続")
    print("c: 攻撃実行！")
    print("q: ドロー終了 (敵のターンへ)")

# ★新機能：ログリストをまとめて表示する係
def show_logs(logs):
    for msg in logs:
        print(msg)

# ★新機能：システムメッセージを表示する係
def show_message(msg):
    print(msg)

# ==========================================
# 2. 論理レベル (Logic / Calculation)
#    - 計算だけする。print禁止。
# ==========================================

def logic_draw(deck, p_hp, stockA):
    logs = []
    force_end = False

    if len(deck) == 0:
        deck = Lparameter.DECK_LIST.copy()
        logs.append(">> 山札補充！")

    card = random.choice(deck)
    deck.remove(card)

    if card == 1:
        stockA += Lparameter.SWORD_POWER
        logs.append(">> 【剣】を引いた！ 攻撃力をチャージ！")
        
    elif card == 2:
        p_hp += Lparameter.HEAL_VALUE
        if p_hp > Lparameter.PLAYER_MAX_HP:
            p_hp = Lparameter.PLAYER_MAX_HP
        logs.append(f">> 【回復】を引いた！ HPが {Lparameter.HEAL_VALUE} 回復した！")
        
    elif card == 3:
        stockA = 0
        force_end = True
        logs.append(">> 【ドクロ】... 溜め攻撃没収 & 強制終了！")

    return deck, p_hp, stockA, force_end, logs

def logic_player_attack(e_hp, stockA):
    logs = []
    damage = int(stockA * 1.15) 
    e_hp -= damage
    logs.append(">> 攻撃実行！")
    logs.append(f">> 敵に {damage} ダメージを与えた！")
    return e_hp, logs

def logic_enemy_turn(p_hp):
    logs = []
    damage = Lparameter.ENEMY_POWER
    p_hp -= damage
    logs.append("\n>> 敵の攻撃！")
    logs.append(f">> {damage} ダメージを受けた！")
    return p_hp, logs

# ==========================================
# 3. メインループ (Main Controller)
#    - print禁止。「show_...」を呼ぶだけ！
# ==========================================

def battle():
    player_hp = Lparameter.PLAYER_MAX_HP
    enemy_hp = Lparameter.ENEMY_MAX_HP
    deck = Lparameter.DECK_LIST.copy()
    stock_attack = 0 
    
    # ★直接 print せず、表示係に頼む！
    show_message(">> 敵が現れた！")

    while True:
        # --- 表示 (Render) ---
        show_battleStatus(enemy_hp, player_hp, stock_attack)
        show_battleCommand()

        # --- 入力 (Input) ---
        command = input("コマンドを入力してください: ")
        show_message("") # 改行用

        # --- ロジック (Update) ---
        
        # A. ドロー
        if command == 'd':
            deck, player_hp, stock_attack, force_end, logs = logic_draw(deck, player_hp, stock_attack)
            
            # ★ログ表示も係に頼む！
            show_logs(logs)

            if force_end:
                command = 'q'

        # B. 攻撃
        if command == 'c':
            enemy_hp, logs = logic_player_attack(enemy_hp, stock_attack)
            stock_attack = 0
            
            show_logs(logs) # ★係に頼む
            command = 'q'

        # C. 敵ターン
        if command == 'q':
            if enemy_hp > 0:
                player_hp, logs = logic_enemy_turn(player_hp)
                show_logs(logs) # ★係に頼む
            
        # --- 勝敗判定 ---
        if enemy_hp <= 0:
            show_message("\n******* 勝ち！ *******") 
            return "win"  
        
        if player_hp <= 0:
            show_message("\n*** 負け... ***")
            return "lose"

if __name__ == "__main__":
    battle()