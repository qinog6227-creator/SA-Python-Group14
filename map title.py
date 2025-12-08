
import pygame
import os
import sys
import math

pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Title -> Map -> Next (Hover Zoom)")
clock = pygame.time.Clock()

# ==== パス設定（実行ファイル基準で安全） ====
BASE = os.path.abspath(os.path.dirname(sys.argv[0]))
TITLE_IMG_PATH = os.path.join(BASE, "pictures", "title", "title(ver1).png")
ENEMY_IMG_PATH = os.path.join(BASE, "pictures", "enemy", "enemy.png")

# ==== 画像読み込み（失敗時は None） ====
def load_image(path, scale_to=None):
    if not os.path.exists(path):
        print(f"[ERROR] File not found: {path}")
        return None
    try:
        img = pygame.image.load(path).convert_alpha()
        if scale_to:
            img = pygame.transform.smoothscale(img, scale_to)
        return img
    except Exception as e:
        print(f"[ERROR] Failed to load image: {path} -> {e}")
        return None

title_img = load_image(TITLE_IMG_PATH, (WIDTH, HEIGHT))
enemy_base = load_image(ENEMY_IMG_PATH)

# ==== マップ用データ ====
enemies = [
    {"pos": (400, 150), "r": 70, "enabled": False},  # 上: 無効（ホバーしても変化なし）
    {"pos": (400, 300), "r": 30, "enabled": False},  # 中: 無効（ホバーしても変化なし）
    {"pos": (400, 450), "r": 30, "enabled": True},   # 下: 有効（ホバーで拡大）
]

def is_hover(e, mouse_pos):
    ex, ey = e["pos"]
    mx, my = mouse_pos
    return math.dist((ex, ey), (mx, my)) <= e["r"]

# 半径ごとの通常サイズスプライトをキャッシュ
sprite_cache = {}  # key: r -> Surface（直径にスケール済み）

def get_enemy_sprite(radius, zoom_factor=1.0):
    """
    半径に合わせて直径にスケール。
    zoom_factor > 1 のときは一時的に拡大（ホバー用）。
    """
    if enemy_base is None:
        return None

    # 通常サイズをキャッシュ
    if radius not in sprite_cache:
        diameter = radius * 2
        sprite_cache[radius] = pygame.transform.smoothscale(enemy_base, (diameter, diameter))

    base_sprite = sprite_cache[radius]
    if zoom_factor == 1.0:
        return base_sprite

    # ホバー拡大（都度スケール：敵数が少ないなら十分軽い）
    w, h = base_sprite.get_size()
    zw, zh = int(w * zoom_factor), int(h * zoom_factor)
    return pygame.transform.smoothscale(base_sprite, (zw, zh))

# ==== 状態管理 ====
STATE_TITLE = 0
STATE_MAP   = 1
STATE_NEXT  = 2
state = STATE_TITLE
selected_enemy = None

# ホバー拡大率（好みで調整）
HOVER_ZOOM = 1.25

# ==== メインループ ====
while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == STATE_TITLE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = STATE_MAP

        elif state == STATE_MAP:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for e in enemies:
                    if e["enabled"] and is_hover(e, mouse_pos):
                        selected_enemy = e
                        state = STATE_NEXT
                        break

    # ==== 描画 ====
    if state == STATE_TITLE:
        if title_img:
            screen.blit(title_img, (0, 0))
        else:
            screen.fill((20, 20, 30))
            font = pygame.font.SysFont(None, 64)
            text = font.render("Title Screen", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 40))
            font2 = pygame.font.SysFont(None, 32)
            tip = font2.render("クリックでスタート", True, (200, 200, 200))
            screen.blit(tip, (WIDTH // 2 - tip.get_width() // 2, HEIGHT // 2 + 20))

    elif state == STATE_MAP:
        screen.fill((0, 0, 0))

        # 敵同士を結ぶ線
        pygame.draw.lines(
            screen, (255, 255, 255), False,
            [e["pos"] for e in enemies],
            3
        )

        # 敵スプライト描画（有効な敵のみホバーで拡大）
        for e in enemies:
            r = e["r"]
            pos = e["pos"]
            hovered = is_hover(e, mouse_pos)
            zoom = HOVER_ZOOM if (e["enabled"] and hovered) else 1.0

            sprite = get_enemy_sprite(r, zoom_factor=zoom)

            if sprite:
                rect = sprite.get_rect(center=pos)
                screen.blit(sprite, rect)
            else:
                # 画像が無い場合は円でフォールバック（色は固定）
                color = (255, 50, 50) if e["enabled"] else (120, 120, 120)
                radius_to_draw = int(r * zoom)
                pygame.draw.circle(screen, color, pos, radius_to_draw)
                pygame.draw.circle(screen, (255, 255, 255), pos, radius_to_draw, 2)

    elif state == STATE_NEXT:
        screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(60)
