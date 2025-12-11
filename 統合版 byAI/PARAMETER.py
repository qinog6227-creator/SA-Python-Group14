import pygame
import sys
import os

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
base_path = os.path.dirname(os.path.abspath(__file__))

def smart_load(name_candidates):
    """
    候補リスト(name_candidates)の中にあるファイルを探して読み込む
    拡張子(.jpg, .png)や区切り文字(_ありなし)を自動で探します
    """
    extensions = ["", ".png", ".jpg", ".jpeg", ".bmp"]
    
    for name in name_candidates:
        for ext in extensions:
            filename = name + ext
            path = os.path.join(base_path, filename)
            if os.path.exists(path):
                print(f"画像読み込み成功: {filename}")
                return pygame.image.load(path)
    
    # 見つからなかった場合
    return None

try:
    # 1. ゲームオーバー画像 (旧 gameover.jpg)
    # image0, image_0, imageover などを探します
    IMG_GAME_OVER = smart_load(["image0", "image_0", "gameover", "image_over"])

    # 2. 次のステージ画像 (旧 next_stage.jpg)
    # image1, image_1, next_stage などを探します
    IMG_NEXT_STAGE = smart_load(["image1", "image_1", "next_stage", "image_next"])

    # 3. ゲームクリア画像 (旧 gameclear.jpg)
    # image2, image_2, gameclear などを探します
    IMG_GAME_CLEAR = smart_load(["image2", "image_2", "gameclear", "image_clear"])

    # 4. 敵画像 (旧 enemy.png)
    # image3, image_3, enemy などを探します
    IMG_ENEMY_RAW = smart_load(["image3", "image_3", "enemy", "image_enemy"])

    # 読み込みチェック
    if None in [IMG_GAME_OVER, IMG_NEXT_STAGE, IMG_GAME_CLEAR, IMG_ENEMY_RAW]:
        print("\n" + "="*40)
        print("【画像が見つかりません】")
        print("ファイル名が以下のいずれかになっているか確認してください：")
        print("  負け画面: image0.jpg / image0.png / image_0.png")
        print("  次へ画面: image1.jpg / image1.png / image_1.png")
        print("  全クリ画面: image2.jpg / image2.png / image_2.png")
        print("  敵キャラ: image3.png / image3.jpg / image_3.png")
        print("="*40 + "\n")
        sys.exit()

    # リサイズ処理
    IMG_ENEMY_MAP = pygame.transform.scale(IMG_ENEMY_RAW, (80, 80))
    IMG_ENEMY_BATTLE = pygame.transform.scale(IMG_ENEMY_RAW, (200, 200))

except Exception as e:
    print(f"【予期せぬエラー】{e}")
    sys.exit()


# --- ユーティリティ関数 ---
def centering_rect(surface_w, surface_h, cx, cy):
    return pygame.Rect(cx - surface_w//2, cy - surface_h//2, surface_w, surface_h)