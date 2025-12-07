import random
import Lparameter

# --- 表示担当の関数たち ---
def show_battleStatus(e_hp, p_hp, stockA): # ★ここも引数で受け取るように変更
    print("\n--------------------------------") # ★見やすく改行追加
    print("敵のHP    :", e_hp)
    print("プレイヤーのHP:", p_hp)
    print("溜め攻撃力:", stockA)
    print("--------------------------------")

def show_battleCommand():
    print("-----コマンド-----")
    print("ドロー継続：d + Enter")
    print("攻撃実行！：c + Enter")
    print("ドロー終了：q + Enter")
    
def show_attack(card, heal): 
    # ★引いたカードの番号(card)によって分岐
    if card == 1:
        print(">> 【剣】を引いた！ 攻撃力を溜めます！")
    elif card == 2:
        print(">> 【回復】を引いた！ HPが", heal ,"回復した！")
    elif card == 3:
        print(">> 【ドクロ】を引いた... 札を失ってしまった…")

# --- メイン関数 ---
def main():
    # ★変数は main の中で作るのが Python のお作法
    player_hp = Lparameter.PLAYER_MAX_HP #プレイヤーのHP
    enemy_hp = Lparameter.ENEMY_MAX_HP #敵のHP
    deck = Lparameter.DECK_LIST.copy() #デッキ
    stock_attack = 0 #攻撃を溜めた量
    
    print("敵が現れた！")

    # ★ゲームはずっと続くので while True で囲む
    while True:
        # 1. 現状表示
        show_battleStatus(enemy_hp, player_hp, stock_attack)
        show_battleCommand()

        # 2. 入力（★ここで変数 command に入れる！）
        command = input("コマンドを入力してください: ")

        # 3. 判定と計算
        if command == 'd':
            # ★ここで初めてカードを引く（ロジック）
            if len(deck) == 0:
                deck = Lparameter.DECK_LIST.copy() # 山札補充
                print(">> 山札補充！")

            card = random.choice(deck)
            deck.remove(card) # 引いたら消す

            # ★引いたカードを「表示関数」に渡す
            show_attack(card, 1)

            # ★計算（パラメータの更新）
            if card == 1:
                stock_attack += 1
            elif card == 2:
                player_hp += 1 # 仮の回復量
            elif card == 3:
                stock_attack = 0 #攻撃を溜めた量を失う
                command = 'q'
        
        if command == 'c':
           print("攻撃実行！")
           print("敵に", stock_attack*1, "ダメージを与えた！")
           enemy_hp -= (stock_attack*1)
           stock_attack = 0
           command == 'q'

        if command == 'q':
            print("敵の攻撃！")
            print("2ダメージを受けた！")
            player_hp -= 2
           









        # ★勝敗判定
        if enemy_hp <= 0:
            print("勝ち！")
            break
        if player_hp <= 0:
            print("負け...")
            break

# 実行
if __name__ == "__main__":
    main()