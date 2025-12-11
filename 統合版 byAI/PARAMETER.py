import pygame
import sys

# --- 画面設定 ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# --- ゲームバランス設定 ---
PLAYER_MAX_HP = 30
ENEMY_STATS = [
    {"hp": 20, "power": 2},
    {"hp": 20, "power": 2},
    {"hp": 50, "power": 4} 
]

# カード設定
CARD_SWORD = 1
CARD_GUARD = 2
CARD_SKULL = 3
SWORD_DMG = 1
GUARD_VAL = 1
DECK_COMPOSITION = [CARD_SWORD]*20 + [CARD_GUARD]*15 + [CARD_SKULL]*5

# --- 色定義 ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (200, 50, 50)
BLUE  = (50, 50, 200)
GRAY  = (100, 100, 100)
PURPLE = (150, 50, 150)

# --- 画像読み込み ---
# ※pygame.init()が呼ばれる前に読み込むため、try-exceptで安全策を取ります
try:
    # リザルト画面用画像
    IMG_GAME_OVER = pygame.image.load("image_0.png")
    IMG_NEXT_STAGE = pygame.image.load("image_1.png")
    IMG_GAME_CLEAR = pygame.image.load("image_2.png")
    
    # 敵アイコン画像 (image_3.png)
    IMG_ENEMY_RAW = pygame.image.load("image_3.png")
    # マップ表示用に小さくリサイズ (80x80)
    IMG_ENEMY_MAP = pygame.transform.scale(IMG_ENEMY_RAW, (80, 80))
    # バトル表示用に大きくリサイズ (200x200)
    IMG_ENEMY_BATTLE = pygame.transform.scale(IMG_ENEMY_RAW, (200, 200))

except FileNotFoundError as e:
    print("【エラー】画像ファイルが見つかりません。")
    print("image_0.png から image_3.png をプログラムと同じ場所に置いてください。")
    sys.exit() # 画像がないと続行できないため終了

except Exception as e:
    # その他のエラー（pygameが初期化されていない環境など）
    print(f"【警告】画像の読み込みに失敗しました: {e}")
    # とりあえずNoneを入れておく（実行時にエラーになる可能性あり）
    IMG_GAME_OVER = None
    IMG_NEXT_STAGE = None
    IMG_GAME_CLEAR = None
    IMG_ENEMY_MAP = None
    IMG_ENEMY_BATTLE = None


# --- ユーティリティ関数 ---
def centering_rect(surface_w, surface_h, cx, cy):
    return pygame.Rect(cx - surface_w//2, cy - surface_h//2, surface_w, surface_h)