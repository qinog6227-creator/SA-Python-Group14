import pygame

# --- 画面設定 ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# --- ゲームバランス設定 ---
# プレイヤー
PLAYER_MAX_HP = 30

# 敵 (ステージごとの設定: [HP, 攻撃力])
# 1戦目, 2戦目, 3戦目(ボス)
ENEMY_STATS = [
    {"hp": 20, "power": 2},
    {"hp": 20, "power": 2},
    {"hp": 50, "power": 4} 
]

# カードID
CARD_SWORD = 1
CARD_GUARD = 2
CARD_SKULL = 3

# カード効果
SWORD_DMG = 1
GUARD_VAL = 1

# デッキ構成 (仕様書通り: ドローし放題の山札の比率)
# ここでは比率として定義し、枯渇したらリシャッフルする形にします
DECK_COMPOSITION = [CARD_SWORD]*20 + [CARD_GUARD]*15 + [CARD_SKULL]*5

# --- 色定義 ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (200, 50, 50)
BLUE  = (50, 50, 200)
GRAY  = (100, 100, 100)
PURPLE = (150, 50, 150)

# --- ユーティリティ関数 ---
def centering_rect(surface_w, surface_h, cx, cy):
    """指定した中心座標に配置するためのRectを返す"""
    return pygame.Rect(cx - surface_w//2, cy - surface_h//2, surface_w, surface_h)