import random
import Lparameter

# --- 1. 変数の準備（C言語の int hp = 10; と同じ） ---
player_hp = Lparameter.PLAYER_MAX_HP
enemy_hp = Lparameter.ENEMY_MAX_HP
deck = Lparameter.DECK_LIST.copy()  # 山札（デッキ）

stock_damage = 0 # 溜めている攻撃力
stock_carryOut = 0 # 溜めている攻撃力を実際に使うときの変数

print("--- バトルスタート ---")

# --- 2. バトルのメイン(無限)ループ ---
def battle_status():
    print("")
    print("\n--------------------------------")
    print("敵のHP    :", enemy_hp)
    print("")
    print("プレイヤーのHP:", player_hp)
    print("溜め攻撃力:", stock_damage)
    print("--------------------------------")
    print("")

def battle_command():
    print("")
    print("-----コマンド-----")
    print("ドロー：d + Enter")
    print("ドロー終了：q + Enter")
    print("カード実行：c + Enter")
    input("コマンドを入力してください: ")

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
        # 敵のHPを減らす
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
