import pygame
import os

# 1. 画像を入れる変数を先に作っておく
TITLE_IMG = None

# 2. 画像の読み込み（ここで1回だけやる！）
# ファイルがない時にエラーで落ちないように try を使う
try:
    # ファイル名が正しいか、もう一度確認してね！
    TITLE_IMG = pygame.image.load('title(ver1).png')
    print("画像読み込み成功！")
except Exception as e:
    print(f"【エラー】画像が見つかりません: {e}")
    # 画像がないときは None のまま

# --- 描画関数 ---
def draw_title(screen):
    # 画像が読み込めていたら表示する
    if TITLE_IMG is not None:
        screen.blit(TITLE_IMG, (100, 100))
    else:
        # 画像がない時は、代わりに赤い四角を表示（エラーだとわかるように）
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))



def draw_title1(screen,font):
    # A. 画用紙を黒で塗りつぶす（リセット）
    screen.fill((0, 0, 0)) 

    # B. 四角を描く（HPバーとか）
    # rect(画用紙, 色, (x, y, 幅, 高さ))
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 50))

    # C. 円を描く（プレイヤーの位置とか）
    # circle(画用紙, 色, (中心x, 中心y), 半径)
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)

    # D. 文字を書く（ログとか）
    # 手順①：文字の「シール」を作る
    text_img = font.render("Hello Pygame!", True, (255, 255, 255))
    # 手順②：画用紙に貼り付ける (blit)
    screen.blit(text_img, (100, 450))

