import random
import Lparameter

# ==========================================
# 1. 表示担当 (View)
#    - ステータス表示などはここに残す
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

# ==========================================
# 2. 計算担当 (Logic)
#    - print 禁止！ logs.append を使う！
# ==========================================

def logic_draw(deck, p_hp, stock):
    logs = [] # ★報告書を入れる箱を作る
    force_end = False # 強制終了フラグ

    # 山札補充
    if len(deck) == 0:
        deck = Lparameter.DECK_LIST.copy()
        logs.append(">> 山札補充！") # ★箱に入れる

    # ドロー
    card = random.choice(deck)
    deck.remove(card)

    # 計算 & ログ追加
    if card == 1:
        stock += Lparameter.SWORD_POWER
        logs.append(">> 【剣】を引いた！ 攻撃力をチャージ！")
        
    elif card == 2:
        p_hp += Lparameter.HEAL_VALUE
        if p_hp > Lparameter.PLAYER_MAX_HP:
            p_hp = Lparameter.PLAYER_MAX_HP
        logs.append(f">> 【回復】を引いた！ HPが {Lparameter.HEAL_VALUE} 回復した！")
        
    elif card == 3:
        stock = 0
        force_end = True
        logs.append(">> 【ドクロ】... 溜め攻撃没収 & 強制終了！")

    # ★計算結果と、ログの箱をまとめて返す
    return deck, p_hp, stock, force_end, logs

def logic_attack(e_hp, stock):
    logs = []
    
    # 計算
    damage = int(stock * 1) # 倍率は適宜調整
    e_hp -= damage
    
    # ログ追加
    logs.append(">> 攻撃実行！")
    logs.append(f">> 敵に {damage} ダメージを与えた！")
    
    return e_hp, logs

def logic_enemy_turn(p_hp):
    logs = []
    
    # 計算
    damage = Lparameter.ENEMY_POWER
    p_hp -= damage
    
    # ログ追加
    logs.append("\n>> 敵の攻撃！")
    logs.append(f">> {damage} ダメージを受けた！")
    
    return p_hp, logs

# ==========================================
# 3. メイン関数 (Controller)
#    - ここで logs を受け取って print する
# ==========================================
def battle():
    player_hp = Lparameter.PLAYER_MAX_HP
    enemy_hp = Lparameter.ENEMY_MAX_HP
    deck = Lparameter.DECK_LIST.copy()
    stock_attack = 0 
    
    print("敵が現れた！")

    while True:
        # 1. 表示
        show_battleStatus(enemy_hp, player_hp, stock_attack)
        show_battleCommand()

        # 2. 入力
        command = input("コマンドを入力してください: ")
        print("") # 改行

        # 3. 判定と計算
        
        # --- ドロー処理 ---
        if command == 'd':
            # ★ロジックを呼ぶ（logs も受け取る！）
            deck, player_hp, stock_attack, force_end, logs = logic_draw(deck, player_hp, stock_attack)
            
            # ★ここでまとめて表示！（CUIならprint, GUIなら描画）
            for msg in logs:
                print(msg)

            # 強制終了（ドクロ）なら q へ
            if force_end:
                command = 'q'

        # --- 攻撃処理 ---
        if command == 'c':
            # ★ロジックを呼ぶ
            enemy_hp, logs = logic_attack(enemy_hp, stock_attack)
            stock_attack = 0
            
            # ★表示
            for msg in logs:
                print(msg)
                
            command = 'q' # 敵のターンへ

        # --- 敵のターン ---
        if command == 'q':
            if enemy_hp > 0:
                # ★ロジックを呼ぶ
                player_hp, logs = logic_enemy_turn(player_hp)
                
                # ★表示
                for msg in logs:
                    print(msg)
            
        # 4. 勝敗判定
        if enemy_hp <= 0:
            print("\n******* 勝ち！ *******") 
            return "win"  
        
        if player_hp <= 0:
            print("\n*** 負け... ***")
            return "lose"

        # 安全策
        if player_hp <= 0: return "lose"
        if enemy_hp <= 0: return "win"

if __name__ == "__main__":
    battle()