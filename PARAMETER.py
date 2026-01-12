import pygame


# 画面の設定
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# プレイヤーの最大HP
PLAYER_MAX_HP = 30

# 敵のHPと攻撃力のリスト
ENEMY_STATS = [
    {"hp": 15, "power": 2},
    {"hp": 20, "power": 3},
    {"hp": 35, "power": 4} 
]

# カードの識別子
CARD_SWORD = 1
CARD_GUARD = 2
CARD_SKULL = 3

SWORD_DMG = 1
GUARD_VAL = 1

# デッキ構成 (ドローし放題の山札の比率)
# ここでは比率として定義し、枯渇したらリシャッフルする形にする
# 小倉百人一首の殿66枚、姫21枚、坊主13枚と同じ数にしている
DECK_COMPOSITION = [CARD_SWORD]*66 + [CARD_GUARD]*21 + [CARD_SKULL]*13

# 色をタプルで定義しておく
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (200, 50, 50)
BLUE  = (50, 50, 200)
GRAY  = (100, 100, 100)
PURPLE = (150, 50, 150)



# ユーティリティ関数
# 中央揃えで表示するための関数
def centering_rect(surface_w, surface_h, cx, cy):
    """指定した中心座標に配置するためのRectを返す"""
    return pygame.Rect(cx - surface_w//2, cy - surface_h//2, surface_w, surface_h)