import pygame
import Pparameter

# ステージの座標 (簡易的)
NODES = [
    {"id": 1, "pos": (200, 300), "radius": 40},
    {"id": 2, "pos": (500, 300), "radius": 40},
    {"id": 3, "pos": (800, 300), "radius": 60} # ボス
]

def draw_map(screen, cleared_stage):
    screen.fill(Pparameter.BLACK)
    
    # 線を描画
    pygame.draw.line(screen, Pparameter.WHITE, NODES[0]["pos"], NODES[1]["pos"], 5)
    pygame.draw.line(screen, Pparameter.WHITE, NODES[1]["pos"], NODES[2]["pos"], 5)

    font = pygame.font.Font(None, 40)
    msg = font.render("Select Next Battle", True, Pparameter.WHITE)
    screen.blit(msg, (50, 50))

    mouse_pos = pygame.mouse.get_pos()
    clicked_stage = None

    for node in NODES:
        stage_id = node["id"]
        pos = node["pos"]
        r = node["radius"]
        
        # 色の決定
        if stage_id <= cleared_stage:
            color = (100, 100, 100) # クリア済み(グレー)
        elif stage_id == cleared_stage + 1:
            color = Pparameter.RED # 挑戦可能(赤)
            # ホバー演出
            dist = ((mouse_pos[0]-pos[0])**2 + (mouse_pos[1]-pos[1])**2)**0.5
            if dist < r:
                color = (255, 100, 100)
                if pygame.mouse.get_pressed()[0]:
                    clicked_stage = stage_id
        else:
            color = (50, 50, 50) # まだ行けない(暗い)

        pygame.draw.circle(screen, color, pos, r)
        pygame.draw.circle(screen, Pparameter.WHITE, pos, r, 3)
        
        # 番号
        label = font.render(str(stage_id), True, Pparameter.WHITE)
        screen.blit(label, label.get_rect(center=pos))

    return clicked_stage