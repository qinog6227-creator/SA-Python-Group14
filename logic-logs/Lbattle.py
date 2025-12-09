import random
import Lparameter

#ステータスを表示する
def show_battleStatus(e_hp, p_hp, stockA): 
    print("----------------------------------")
    print(f"敵のHP    : {e_hp}")
    print(f"プレイヤー: {p_hp}")
    print(f"溜め攻撃力: {stockA}")

#コマンド一覧を表示
def show_battleCommand():
    print("-----コマンド-----")
    print("d: ドロー継続")
    print("c: 攻撃実行！")
    print("q: ドロー終了 (敵のターンへ)")
    
# コマンド入力&実行結果を表示
def show_attack(card, heal): 
    if card == 1:
        print(">> 【剣】を引いた！ 攻撃力をチャージ！")
    elif card == 2:
        print(f">> 【回復】を引いた！ HPが {heal} 回復した！")
    elif card == 3:
        print(">> 【ドクロ】... 溜め攻撃没収 & 強制終了！")


# メッセージ一覧
#　普通の敵、魔王遭遇


# --- メイン関数 ---
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
        print("")

        # 3. 判定と計算
        if command == 'd':
            # 山札補充
            if len(deck) == 0: #配列の要素数(len関数で計測)が0ならば
                deck = Lparameter.DECK_LIST.copy()
                print(">> 山札補充！")

            # 札をランダムに取り出す
            card = random.choice(deck)
            deck.remove(card)

            # 結果表示
            show_attack(card, Lparameter.HEAL_VALUE)

            # 計算
            if card == 1:
                stock_attack += Lparameter.SWORD_POWER
            elif card == 2:
                player_hp += Lparameter.HEAL_VALUE
                # 最大HPを超えないようにする
                if player_hp > Lparameter.PLAYER_MAX_HP:
                    player_hp = Lparameter.PLAYER_MAX_HP
            elif card == 3:
                stock_attack = 0
                command = 'q' #敵の攻撃へ移行
        
        if command == 'c':
            print(">> 攻撃実行！")
            print(f">> 敵に {stock_attack} ダメージを与えた！")
            
            enemy_hp -= stock_attack
            stock_attack = 0
            command = 'q' #敵の攻撃へ移行

        #自分のターンが終了して、敵の攻撃へ移行
        if command == 'q':
            # 敵が生きているなら攻撃してくる
            if enemy_hp > 0:
                print("\n>> 敵の攻撃！")
                print(f">> {Lparameter.ENEMY_POWER} ダメージを受けた！")
                player_hp -= Lparameter.ENEMY_POWER
            
        # 勝敗判定
        if enemy_hp <= 0:
            print("\n******* 勝ち！ *******") 
            return  "win"  
        
        if player_hp <= 0:
            print("\n*** 負け... ***")
            return "lose"