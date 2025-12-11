import pygame
import PARAMETER

# ステージの座標
NODES = [
    {"id": 1, "pos": (200, 300), "radius": 40},
    {"id": 2, "pos": (500, 300), "radius": 40},
    {"id": 3, "pos": (800, 300), "radius": 60}
]

def draw_map(screen, cleared_stage):
    screen.fill(PARAMETER.BLACK)
    
    # 線を描画
    pygame.draw.line(screen, PARAMETER.WHITE, NODES[0]["pos"], NODES[1]["pos"], 5)
    pygame.draw.line(screen, PARAMETER.WHITE, NODES[1]["pos"], NODES[2]["pos"], 5)

    font = pygame.font.Font(None, 40)
    msg = font.render("Select Next Battle", True, PARAMETER.WHITE)
    screen.blit(msg, (50, 50))

    mouse_pos = pygame.mouse.get_pos()
    clicked_stage = None

    for node in NODES:
        stage_id = node["id"]
        pos = node["pos"]
        r = node["radius"] # 今回は画像の配置基準に使います
        
        # 画像の準備
        img = PARAMETER.IMG_ENEMY_MAP
        # 画像の中心をノードの座標に合わせる
        img_rect = img.get_rect(center=pos)

        # 状態判定と描画
        if stage_id <= cleared_stage:
            # クリア済み：少し暗く表示する演出
            dark_img = img.copy()
            # 黒を乗算して暗くする
            dark_img.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_MULT)
            screen.blit(dark_img, img_rect)
            
        elif stage_id == cleared_stage + 1:
            # 挑戦可能：そのまま表示
            screen.blit(img, img_rect)
            # ホバー判定（マウスが画像の範囲内にあるか）
            if img_rect.collidepoint(mouse_pos):
                # ホバー時に赤い枠を表示
                pygame.draw.rect(screen, PARAMETER.RED, img_rect, 3)
                if pygame.mouse.get_pressed()[0]:
                    clicked_stage = stage_id
        else:
            # まだ行けない：さらに暗く表示
            very_dark_img = img.copy()
            very_dark_img.fill((50, 50, 50), special_flags=pygame.BLEND_RGB_MULT)
            screen.blit(very_dark_img, img_rect)

        # 番号を画像の上に重ねて表示
        label = font.render(str(stage_id), True, PARAMETER.WHITE)
        screen.blit(label, label.get_rect(center=pos))

    return clicked_stage