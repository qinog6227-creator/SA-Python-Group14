# Lparameter.py

# --- パラメータ設定 ---
PLAYER_MAX_HP = 30
ENEMY_MAX_HP = 50

# --- カードの効果 ---
SWORD_POWER = 3    # 剣1枚で溜まる攻撃力
HEAL_VALUE  = 5    # 回復薬での回復量
SKULL_DMG   = 5    # ドクロでの自傷ダメージ

# --- デッキ (1:剣, 2:回復, 3:実行, 4:ドクロ) ---
DECK_LIST = [
    1, 1, 1, 1, 1     # 剣（溜め）
    2, 2, 2, 2        # 回復（即時）
    3                 # ドクロ（没収）
]