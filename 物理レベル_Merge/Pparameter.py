#バトルに関するパラメータのマクロ

# --- パラメータ設定 ---
PLAYER_MAX_HP = 30
ENEMY_MAX_HP = 5

# ステージごとの敵の攻撃力
ENEMY_POWER_LIST = [2, 4, 6] 

# --- カードの効果 ---
SWORD_POWER = 1   # 剣1枚で溜まる攻撃力
GUARD_POWER = 1   #ガードでのHP増強量
ENEMY_POWER = 2   # 敵のターンでの攻撃力

# --- デッキ (1:剣, 2:ガード, 3:ドクロ) ---
DECK_LIST = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
             1, 1, 1, 1, 1, 1, 1,
             2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] 


#図形をど真ん中に揃える関数
def centering (name):
    rect = name.get_rect(center=(400,300))
    return rect

#画像を横半分に揃える
def centeringY (name, y):
    rect = name.get_rect(center=(400,y))
    return rect

#画像を縦半分に揃える
def centeringX (name, x):
    rect = name.get_rect(center=(x,300))
    return rect

