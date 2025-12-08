import pygame
import sys
import math

#window size
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Map Test")
clock = pygame.time.Clock()

#敵の座標
enemies = [
    {"pos": (400, 150), "r": 20, "enabled": False},  # 大
    {"pos": (400, 300), "r": 14, "enabled": False},  # 中
    {"pos": (400, 450), "r": 14, "enabled": True},   # 中 
]

def is_hover(e, mouse_pos):
    ex, ey = e["pos"]
    mx, my = mouse_pos
    return math.dist((ex, ey), (mx, my)) <= e["r"]

#   マップ画面ループ
in_map = True
while in_map:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for e in enemies:
                if e["enabled"] and is_hover(e, mouse_pos):
                    in_map = False 
                    break

    #背景
    screen.fill((128, 128, 128))

    #線
    pygame.draw.lines(
        screen, (0, 0, 0), False,
        [e["pos"] for e in enemies],
        3
    )

    #敵マーク描画
    for e in enemies:
        if is_hover(e, mouse_pos):
            # ホバー中の色
            color = (255, 120, 120)
        else:
            # 通常の色（赤かグレー）
            color = (255, 50, 50) if e["enabled"] else (120, 120, 120)

        pygame.draw.circle(screen, color, e["pos"], e["r"])
        pygame.draw.circle(screen, (255, 255, 255), e["pos"], e["r"], 2)

    pygame.display.flip()
    clock.tick(60)

#   次の描画
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)