import random
import Mparameter

# --- 1. ドロー処理 ---
# ★引数と戻り値に stockD を追加！★
def calc_draw(deck, p_hp, stockA, stockD):
    logs = []
    force_end = False #強制終了の判定

    if len(deck) == 0: #len関数は配列の要素数を計測
        deck = Mparameter.DECK_LIST.copy() #マクロからコピー
        logs.append(">> 山札を補充しました！")

    card = random.choice(deck) #ランダムに引く
    deck.remove(card) #

    # --- 効果判定 ---
    if card == 1:
        stockA += Mparameter.SWORD_POWER
        logs.append(">> 【剣】を引いた！ 攻撃力をチャージ！")
        
    elif card == 2:
        # ★ガードを「加算」して溜めるロジックに変更
        stockD += Mparameter.GUARD_POWER
        logs.append(f">> 【ガード】を引いた！ 防御力が {Mparameter.GUARD_POWER} 増強！")
        
    elif card == 3:
        # ドクロは全てを失う
        stockA = 0
        stockD = 0
        force_end = True
        logs.append(">> 【ドクロ】... 溜め攻撃・防御を全て没収 & 強制終了！")

    # ★戻り値に stockD を追加！
    return deck, p_hp, stockA, stockD, force_end, logs


# ==========================================
# 2. プレイヤーの攻撃処理
#    (stockD は攻撃には影響しないため変更なし)
# ==========================================
def calc_player_attack(e_hp, stockA):
    logs = []
    damage = int(stockA * 1.0) 
    e_hp -= damage
    logs.append(">> 攻撃実行！")
    logs.append(f">> 敵に {damage} のダメージを与えた！")
    
    return e_hp, logs


# ==========================================
# 3. 敵の攻撃処理
#    ★ stockD を使ってダメージを減らすロジックを追加！
# ==========================================
def calc_enemy_turn(p_hp, stockD, current_stage):
    logs = []
    
    # 敵の基本攻撃力を取得
    base_power = Mparameter.ENEMY_POWER_LIST[current_stage - 1]
    
    # ★ガードによるダメージ軽減計算
    actual_damage = base_power - stockD
    if actual_damage < 0:
        actual_damage = 0 # ダメージは0未満にならない
        
    p_hp -= actual_damage
    
    logs.append("\n>> 敵の攻撃！")
    
    if actual_damage > 0:
        logs.append(f">> {base_power} ダメージ（ガードで {stockD} 軽減）を受けた！")
    else:
        logs.append(">> 攻撃は完璧にガードされた！ダメージなし！")
        
    # ガードは使い切りなので、メイン関数側でリセット処理が必要です。
    # (ここでは計算のみ行う)
    return p_hp, logs

