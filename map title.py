
import pygame
import os
import sys
import math

pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Title -> Map -> Next")

clock = pygame.time.Clock()

# ==== タイトル画像の読み込み ====
BASE = os.path.dirname(__file__)
TITLE_IMG_PATH = os.path.join(BASE, "pictures", "title", "title(ver1).png")

# タイトル画像読み込み（存在チェック＆フォールバック）
try:
    title_img = pygame.image.load(TITLE_IMG_PATH).convert_alpha()
    title_img = pygame.transform.scale(title_img, (WIDTH, HEIGHT))
except Exception as e:
    # 画像がない場合のフォールバック描画用
    title_img = None
    print(f"[WARN] タイトル画像を読み込めませんでした: {e}")

# ==== マップで使うデータ ====
enemies = [
    {"pos": (400, 150), "r": 50, "enabled": False},  # 大 (無効)
    {"pos": (400, 300), "r": 20, "enabled": False},  # 中 (無効)
    {"pos": (400, 450), "r": 20, "enabled": True},   # 中 (有効)
]

def is_hover(e, mouse_pos):
    ex, ey = e["pos"]
    mx, my = mouse_pos
    # Python 3.8+ の math.dist を使用（古い環境なら hypot を推奨）
    return math.dist((ex, ey), (mx, my)) <= e["r"]

# ==== 状態管理 ====
STATE_TITLE = 0
STATE_MAP   = 1
STATE_NEXT  = 2
state = STATE_TITLE

selected_enemy = None  # MAPで選択した敵を保持

# ==== メインループ ====
while True:
    mouse_pos = pygame.mouse.get_pos()

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- タイトルの操作 ---
        if state == STATE_TITLE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # クリックで MAP へ
                state = STATE_MAP

        # --- マップの操作 ---
        elif state == STATE_MAP:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 有効な敵にクリックヒットしたら次の画面へ
                for e in enemies:
                    if e["enabled"] and is_hover(e, mouse_pos):
                        selected_enemy = e
                        state = STATE_NEXT
                        break

        # --- 次の画面の操作（例：Escでタイトルへ戻るなど拡張可能） ---
        elif state == STATE_NEXT:
            # 今回は特に操作なし（必要ならキー操作など追加）
            pass

    # 描画
    if state == STATE_TITLE:
        if title_img:
            screen.blit(title_img, (0, 0))
        else:
            # フォールバック：画像なしでもタイトル風に描画
            screen.fill((20, 20, 30))
            font = pygame.font.SysFont(None, 64)
            text = font.render("Title Screen", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 40))
            font2 = pygame.font.SysFont(None, 32)
            tip = font2.render("クリックでスタート", True, (200, 200, 200))
            screen.blit(tip, (WIDTH // 2 - tip.get_width() // 2, HEIGHT // 2 + 20))

    elif state == STATE_MAP:
        # 背景
        screen.fill((0, 0, 0))

        # 敵同士を結ぶ線
        pygame.draw.lines(
            screen, (255, 255, 255), False,
            [e["pos"] for e in enemies],
            3
        )

        # 敵マーク描画
        for e in enemies:
            if e["enabled"] and is_hover(e, mouse_pos):
                # ホバー中の色
                color = (255, 120, 120)
            else:
                # 通常の色（赤かグレー）
                color = (255, 50, 50) if e["enabled"] else (120, 120, 120)

            pygame.draw.circle(screen, color, e["pos"], e["r"])
            pygame.draw.circle(screen, (255, 255, 255), e["pos"], e["r"], 2)
    
    elif state == STATE_NEXT:
        # 次の画面（例）
        screen.fill((0, 0, 0))
        

        # 戻る／遷移など拡張したい場合はここにボタンやキー処理を追加

    pygame.display.flip()
    clock.tick(60)
