import random  # 乱数を使うためのおまじない（Cの #include <stdlib.h> みたいなもの）

# --- 1. 変数の準備（C言語の int hp = 10; と同じ） ---
player_hp = 10
enemy_hp = 10

# 山札（C言語の配列みたいなもの。 [] の中にデータを入れる）
# 1="剣", 2="回復", 3="姫(攻撃実行)", 4="ドクロ" とします
deck = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4] 

# 溜めている攻撃力
stock_damage = 0

print("--- ゲームスタート ---")

# --- 2. ゲームのループ（C言語の while(1) { ... } と同じ） ---
while True:
    print("\n--------------------------------")
    print("あなたのHP:", player_hp)
    print("敵のHP    :", enemy_hp)
    print("溜め攻撃力:", stock_damage)
    print("--------------------------------")

    # ユーザーに入力させる（Enterキーを押すまで待つ）
    input("Enterキーを押してカードを引く！")

    # --- 3. 山札からカードを引く処理 ---
    if len(deck) == 0:
        print("山札がなくなった！リシャッフルします！")
        deck = [1, 1, 1, 2, 2, 3, 3, 4, 4] # 山札を元に戻す

    # random.choice は「配列からランダムに1個選ぶ」命令
    card = random.choice(deck)

    # --- 4. 引いたカードごとの動き（C言語の if ~ else if と同じ） ---
    if card == 1:
        print("【剣】を引いた！ 攻撃力を溜めます！")
        stock_damage = stock_damage + 1

    elif card == 2:
        print("【回復】を引いた！ HPが1回復！")
        player_hp = player_hp + 1

    elif card == 3:
        print("【姫】を引いた！ 溜めた攻撃を放て！！")
        carryOut = input("攻撃を実行しますか？ はい:y いいえ:n")

        if carryOut.lower() != "n":
            print("攻撃をキャンセルしました。")
            continue  # 攻撃しないので次のループへ
        else:
            #敵のHPを減らす
            print("敵に", stock_damage, "のダメージ！")
            enemy_hp = enemy_hp - stock_damage
            
            stock_damage = 0  # 攻撃したのでストックは0に戻る

    elif card == 4:
        print("【ドクロ】を引いた... 攻撃失敗＆ダメージを受ける！")
        stock_damage = 0  # 溜めた攻撃がパァになる
        player_hp = player_hp - 2
        print("あなたは2ダメージ受けた...")

    # --- 5. 勝敗判定 ---
    if enemy_hp <= 0:
        print("\nやった！ 敵を倒した！ あなたの勝ち！")
        break  # ループを抜けて終了

    if player_hp <= 0:
        print("\n残念... あなたは負けてしまった...")
        break  # ループを抜けて終了

print("--- ゲーム終了 ---")