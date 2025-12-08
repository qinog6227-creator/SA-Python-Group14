import pygame
import random
import sys

# ------------------ 設定 ------------------
SCREEN_W, SCREEN_H = 800, 600
FPS = 60
HAND_LIMIT = 10

# 日本語フォント（環境に応じて変更可）
UI_FONT_NAME = "meiryo"  # 例: "Noto Sans CJK JP", "Yu Gothic", "Hiragino Kaku Gothic Pro"

# 山札ビューのパネル設定（描画と一致させる）
DECK_PANEL_W, DECK_PANEL_H = 520, 420
DECK_ROW_H = 28

# ------------------ ユーティリティ ------------------
def jp_font(size):
    """日本語フォントがない環境でも落ちないようにフォールバック"""
    try:
        return pygame.font.SysFont(UI_FONT_NAME, size)
    except Exception:
        return pygame.font.SysFont(None, size)

# ------------------ カード定義 ------------------
class Card:
    def __init__(self, name, color=(230, 230, 255), is_skull=False, ctype="Generic"):
        self.name = name
        self.color = color
        self.size = (100, 150)
        self.pos = (0, 0)  # 手札描画位置
        self.is_skull = is_skull
        self.ctype = ctype  # "Attack", "Skill", "Power", "Curse" 等

    def draw(self, surface, font):
        """通常（手札）描画"""
        x, y = self.pos
        w, h = self.size
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(surface, self.color, rect, border_radius=8)
        pygame.draw.rect(surface, (40, 40, 80), rect, width=2, border_radius=8)
        name_surf = font.render(f"{self.name}", True, (20, 20, 20))
        surface.blit(name_surf, (x + 8, y + 8))

    def render_surface(self, font):
        """ズーム用にカードをSurfaceとして生成"""
        w, h = self.size
        surf = pygame.Surface((w, h), pygame.SRCALPHA)
        rect = pygame.Rect(0, 0, w, h)
        pygame.draw.rect(surf, self.color, rect, border_radius=8)
        pygame.draw.rect(surf, (40, 40, 80), rect, width=2, border_radius=8)
        name_surf = font.render(f"{self.name}", True, (20, 20, 20))
        surf.blit(name_surf, (8, 8))
        return surf

# ------------------ 山札・手札・墓地管理 ------------------
def make_starting_deck():
    """初期デッキ＋ドクロカード1枚（コストなし）"""
    deck = []
    for i in range(5):
        deck.append(Card(name=f"Strike {i+1}", color=(240, 220, 220), ctype="Attack"))
    for i in range(5):
        deck.append(Card(name=f"Defend {i+1}", color=(220, 240, 220), ctype="Skill"))
    deck.append(Card(name="Bash", color=(240, 230, 200), ctype="Attack"))
    skull = Card(name="💀 Skull", color=(80, 80, 80), is_skull=True, ctype="Curse")
    deck.append(skull)
    random.shuffle(deck)
    return deck

def reshuffle_from_grave_if_needed(deck, grave):
    """山札が空なら墓地をシャッフルして山札へ戻す"""
    if not deck and grave:
        deck.extend(grave)
        grave.clear()
        random.shuffle(deck)

def draw_one(deck, hand, grave):
    """山札から1枚引く。ドクロはズーム演出→ターン終了を別処理で行う"""
    if len(hand) >= HAND_LIMIT:
        return None
    if not deck:
        reshuffle_from_grave_if_needed(deck, grave)
        if not deck:
            return None
    card = deck.pop()   # リスト末尾を「山札の上」とする
    hand.append(card)
    if card.is_skull:
        return "SKULL_DRAWN"
    return None

def execute_all(hand, grave):
    """手札を一括実行して墓地へ"""
    if not hand:
        return []
    executed_cards = hand[:]
    grave.extend(executed_cards)
    hand.clear()
    return executed_cards

def layout_hand(hand):
    """手札を画面下に整列"""
    if not hand:
        return
    spacing = 20
    card_w, card_h = hand[0].size
    total_w = len(hand) * card_w + (len(hand) - 1) * spacing
    start_x = (SCREEN_W - total_w) // 2
    y = SCREEN_H - card_h - 60  # 下UIと重なりにくく
    for i, c in enumerate(hand):
        c.pos = (start_x + i * (card_w + spacing), y)

# ------------------ ボタンクラス ------------------
class Button:
    def __init__(self, rect, text, font=None,
                 bg=(70, 90, 140), hover_bg=(90, 120, 180), fg=(255, 255, 255),
                 border=(230, 230, 255), disabled_bg=(80, 80, 80), disabled_fg=(200, 200, 200)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font or jp_font(28)
        self.bg = bg
        self.hover_bg = hover_bg
        self.fg = fg
        self.border = border
        self.disabled_bg = disabled_bg
        self.disabled_fg = disabled_fg
        self._is_hover = False
        self.enabled = True

    def set_enabled(self, enabled: bool):
        self.enabled = enabled

    def update(self, mouse_pos):
        self._is_hover = self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        if self.enabled:
            color = self.hover_bg if self._is_hover else self.bg
            fg = self.fg
        else:
            color = self.disabled_bg
            fg = self.disabled_fg
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, self.border, self.rect, width=2, border_radius=8)
        label = self.font.render(self.text, True, fg)
        lx = self.rect.x + (self.rect.w - label.get_width()) // 2
        ly = self.rect.y + (self.rect.h - label.get_height()) // 2
        surface.blit(label, (lx, ly))

    def handle_event(self, event):
        """左クリックされたら True。disabled の場合は無効。"""
        if not self.enabled:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# ------------------ 山札アイコン ------------------
def make_deck_icon_rect(draw_button_rect, icon_size=(80, 104), gap=8, extra_up=24):
    """ドローボタンの上に置く山札アイコンRect（上に少し余分にずらす）"""
    iw, ih = icon_size
    ix = draw_button_rect.x + (draw_button_rect.w - iw) // 2
    iy = draw_button_rect.y - ih - gap - extra_up
    return pygame.Rect(ix, iy, iw, ih)

def draw_deck_icon(surface, rect, count, hover=False):
    """重なったカード裏のイラスト＋枚数ラベル（ラベルは上側）"""
    back_colors = [(40, 60, 100), (50, 70, 120), (60, 80, 140)]
    offsets = [(8, 10), (4, 5), (0, 0)]
    for (dx, dy), col in zip(offsets, back_colors):
        r = pygame.Rect(rect.x + dx, rect.y + dy, rect.w - dx, rect.h - dy)
        pygame.draw.rect(surface, col, r, border_radius=10)
        pygame.draw.rect(surface, (200, 210, 240), r, width=2, border_radius=10)
    if hover:
        pygame.draw.rect(surface, (250, 240, 120), rect.inflate(8, 8), width=2, border_radius=12)

    font = jp_font(18)
    label = font.render(f"山札: {count}", True, (240, 240, 240))
    shadow = font.render(f"山札: {count}", True, (20, 20, 20))
    lx = rect.centerx - label.get_width() // 2
    ly = rect.top - label.get_height() - 6  # 上に表示
    surface.blit(shadow, (lx + 1, ly + 1))
    surface.blit(label, (lx, ly))

# ------------------ 山札ビューの並べ替え ------------------
TYPE_ORDER = ["Attack", "Skill", "Power", "Other", "Curse"]

def deck_to_grouped_view_list(deck):
    """
    山札をタイプ別に並べ替えた表示用リストを返す。
    ドクロ（is_skull=True）は必ず最後にまとめる。
    ※ deck の内部順序は変更しない（表示専用）
    """
    non_skull = [c for c in deck if not getattr(c, "is_skull", False)]
    skulls = [c for c in deck if getattr(c, "is_skull", False)]

    def normalize_type(c):
        t = getattr(c, "ctype", "Other")
        return t if t in TYPE_ORDER else "Other"

    groups = {t: [] for t in TYPE_ORDER}
    for c in non_skull:
        groups[normalize_type(c)].append(c)

    ordered = []
    for t in TYPE_ORDER:
        ordered.extend(groups[t])
    ordered.extend(skulls)  # 最後にドクロを追加
    return ordered

# ------------------ 山札ビュー（モーダル） ------------------
def draw_deck_view(screen, deck, ui_font, item_font, scroll_offset=0):
    """半透明オーバーレイ＋中央パネルに山札内容を表示（タイプ別／ドクロ最後）"""
    overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    panel_rect = pygame.Rect(0, 0, DECK_PANEL_W, DECK_PANEL_H)
    panel_rect.center = (SCREEN_W // 2, SCREEN_H // 2)
    pygame.draw.rect(screen, (30, 40, 70), panel_rect, border_radius=12)
    pygame.draw.rect(screen, (230, 230, 255), panel_rect, width=2, border_radius=12)

    # タイトルをシンプルに
    title = ui_font.render("山札", True, (240, 240, 240))
    screen.blit(title, (panel_rect.centerx - title.get_width() // 2, panel_rect.top + 10))

    close_font = jp_font(20)
    # 閉じるボタンもシンプルに
    close_text = close_font.render("閉じる", True, (240, 220, 220))
    close_rect = close_text.get_rect()
    close_rect.topright = (panel_rect.right - 12, panel_rect.top + 12)
    screen.blit(close_text, close_rect.topleft)

    # 内側領域（inflate(-24, -80) と一致）
    inner = panel_rect.inflate(-24, -80)
    pygame.draw.rect(screen, (25, 32, 60), inner, border_radius=8)

    items = deck_to_grouped_view_list(deck)
    row_h = DECK_ROW_H
    visible_rows = inner.h // row_h

    start_idx = max(0, min(len(items) - visible_rows, scroll_offset))
    end_idx = min(len(items), start_idx + visible_rows)

    for i, card in enumerate(items[start_idx:end_idx], start=0):
        y = inner.y + i * row_h
        if i % 2 == 0:
            pygame.draw.rect(screen, (32, 42, 75), (inner.x, y, inner.w, row_h))
        # シンプルな表示（タイプ＋名前のみ）
        label_text = f"{card.ctype}: {card.name}"
        color = (255, 230, 160) if getattr(card, "is_skull", False) else (220, 230, 240)
        label = item_font.render(label_text, True, color)
        screen.blit(label, (inner.x + 8, y + 5))

    hint = close_font.render("↑↓キー / マウスホイールでスクロール", True, (220, 220, 220))
    screen.blit(hint, (panel_rect.centerx - hint.get_width() // 2, panel_rect.bottom - 28))

    return {"panel_rect": panel_rect, "close_rect": close_rect, "inner_rect": inner, "visible_rows": visible_rows}

# ------------------ ドクロのズーム演出 ------------------
def draw_skull_zoom_overlay(screen, skull_card, card_font, scale=1.5, title_font=None):
    """画面を薄暗くして、ドクロカードを中央にズーム表示"""
    overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    base_surf = skull_card.render_surface(card_font)
    w, h = skull_card.size
    scaled_w, scaled_h = int(w * scale), int(h * scale)
    scaled = pygame.transform.smoothscale(base_surf, (scaled_w, scaled_h))

    cx = SCREEN_W // 2
    cy = SCREEN_H // 2
    rect = scaled.get_rect(center=(cx, cy))
    screen.blit(scaled, rect.topleft)

    if title_font:
        title = title_font.render("💀 ドクロ発動", True, (240, 220, 100))
        screen.blit(title, (cx - title.get_width() // 2, rect.top - title.get_height() - 12))

# ------------------ メインループ ------------------
def main():
    pygame.init()
    pygame.display.set_caption("山札ビュー＋ドクロズーム（シンプルラベル）")
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()

    # フォント
    ui_font = jp_font(26)
    card_font = jp_font(24)
    log_font = jp_font(22)
    title_font = jp_font(30)

    # 山札・手札・墓地
    deck = make_starting_deck()
    hand = []
    grave = []

    # ターン状態
    turn_active = True  # True: 進行中 / False: 終了中

    # ボタン配置（左下：ドロー、右下：実行）
    btn_w, btn_h = 160, 44
    margin = 20
    draw_button = Button(rect=(margin, SCREEN_H - btn_h - margin, btn_w, btn_h), text="ドロー", font=ui_font)
    exec_button = Button(rect=(SCREEN_W - btn_w - margin, SCREEN_H - btn_h - margin, btn_w, btn_h), text="実行", font=ui_font)

    # 山札アイコンRect（ドローボタンの上／上方向余白あり）
    deck_icon_rect = make_deck_icon_rect(draw_button.rect, icon_size=(80, 104), gap=8, extra_up=24)
    deck_icon_hover = False

    # 山札ビューの状態（描画前でも安全に扱えるよう visible_rows を事前計算）
    deck_view_open = False
    deck_view_scroll = 0
    deck_view_ui = None
    deck_view_visible_rows = (DECK_PANEL_H - 80) // DECK_ROW_H  # inner.h = panel_h - 80 と一致

    # ドクロズーム演出の状態
    skull_anim_active = False
    skull_anim_card = None
    skull_anim_start_ms = 0
    skull_anim_duration_ms = 2000  # 0.9秒表示

    last_log = ""

    running = True
    while running:
        dt = clock.tick(FPS)
        now = pygame.time.get_ticks()

        # 入力処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ドクロ演出中は入力無効
            if skull_anim_active:
                continue

            # 山札ビューが開いている時の入力（deck_view_ui に依存しない安全版）
            if deck_view_open:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        deck_view_open = False
                    elif event.key == pygame.K_UP:
                        deck_view_scroll = max(0, deck_view_scroll - 1)
                    elif event.key == pygame.K_DOWN:
                        max_start = max(0, len(deck) - deck_view_visible_rows)
                        deck_view_scroll = min(max_start, deck_view_scroll + 1)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # 閉じるボタンは描画後（deck_view_ui がある時）だけ判定
                        if deck_view_ui and deck_view_ui["close_rect"].collidepoint(event.pos):
                            deck_view_open = False
                    elif event.button == 4:  # wheel up
                        deck_view_scroll = max(0, deck_view_scroll - 1)
                    elif event.button == 5:  # wheel down
                        max_start = max(0, len(deck) - deck_view_visible_rows)
                        deck_view_scroll = min(max_start, deck_view_scroll + 1)
                elif event.type == pygame.MOUSEWHEEL:
                    delta = -event.y  # 上に回すと y=1 → スクロールアップ
                    max_start = max(0, len(deck) - deck_view_visible_rows)
                    deck_view_scroll = min(max_start, max(0, deck_view_scroll + delta))
                # ビュー中は他の入力をブロック
                continue

            # 左下：ドローボタン
            if draw_button.handle_event(event):
                if not turn_active:
                    turn_active = True
                    last_log = "次のターン開始"
                trigger = draw_one(deck, hand, grave)
                if trigger == "SKULL_DRAWN":
                    skull_anim_active = True
                    skull_anim_card = hand[-1]
                    skull_anim_start_ms = now

            # 右下：実行ボタン（ターン中のみ）
            if exec_button.handle_event(event):
                if turn_active:
                    executed = execute_all(hand, grave)
                    if executed:
                        names = ", ".join([c.name for c in executed])
                        last_log = f"実行: {names}"
                    else:
                        last_log = "実行できるカードがありません（手札が空）"

            # 山札アイコンクリックで山札ビューを開く
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if deck_icon_rect.collidepoint(event.pos):
                    deck_view_open = True
                    deck_view_scroll = 0  # 先頭から

            # デバッグ：スペース=ドロー / Enter=実行 / D=山札ビュー
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not turn_active:
                        turn_active = True
                        last_log = "次のターン開始"
                    trigger = draw_one(deck, hand, grave)
                    if trigger == "SKULL_DRAWN":
                        skull_anim_active = True
                        skull_anim_card = hand[-1]
                        skull_anim_start_ms = now
                if event.key == pygame.K_RETURN:
                    if turn_active:
                        executed = execute_all(hand, grave)
                        if executed:
                            names = ", ".join([c.name for c in executed])
                            last_log = f"実行: {names}"
                        else:
                            last_log = "実行できるカードがありません（手札が空）"
                if event.key == pygame.K_d:
                    deck_view_open = True
                    deck_view_scroll = 0

        # ドクロ演出の終了処理
        if skull_anim_active and (now - skull_anim_start_ms >= skull_anim_duration_ms):
            grave.extend(hand)
            hand.clear()
            turn_active = False
            last_log = "💀 ドクロ発動：手札をすべて墓地へ送り、ターン終了"
            skull_anim_active = False
            skull_anim_card = None

        # ボタン有効/無効
        if skull_anim_active or deck_view_open:
            draw_button.set_enabled(False)
            exec_button.set_enabled(False)
        else:
            draw_button.set_enabled(True)
            exec_button.set_enabled(turn_active)

        # ホバー更新
        mouse_pos = pygame.mouse.get_pos()
        draw_button.update(mouse_pos)
        exec_button.update(mouse_pos)
        deck_icon_hover = deck_icon_rect.collidepoint(mouse_pos)

        # レイアウト更新
        layout_hand(hand)

        # ------------------ 描画 ------------------
        screen.fill((15, 20, 35))

        info = ui_font.render(
            f"Deck: {len(deck)}  Hand: {len(hand)}  Grave(墓地): {len(grave)}  / ターン: {'進行中' if turn_active else '終了'}",
            True, (230, 230, 230)
        )
        screen.blit(info, (20, 20))

        log_surf = log_font.render(last_log, True, (220, 220, 180))
        screen.blit(log_surf, (20, 50))

        for c in hand:
            c.draw(screen, card_font)

        draw_button.draw(screen)
        exec_button.draw(screen)

        # 山札アイコン（ラベルは上、アイコンは上にずらして配置）
        draw_deck_icon(screen, deck_icon_rect, count=len(deck), hover=deck_icon_hover)

        # ドクロズーム演出
        if skull_anim_active and skull_anim_card:
            draw_skull_zoom_overlay(screen, skull_anim_card, card_font, scale=1.5, title_font=title_font)

        # 山札ビュー（オーバーレイ）
        deck_view_ui = None
        if deck_view_open:
            deck_view_ui = draw_deck_view(screen, deck, ui_font, item_font=jp_font(20), scroll_offset=deck_view_scroll)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
