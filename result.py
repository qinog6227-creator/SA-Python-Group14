import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Result Screen")

# 画像読み込み
game_over_img = pygame.image.load("gameover.png")
game_clear_img = pygame.image.load("gameclear.png")

# 画面サイズに合わせて調整したい場合は以下を使用
# game_over_img = pygame.transform.scale(game_over_img, (800, 600))
# game_clear_img = pygame.transform.scale(game_clear_img, (800, 600))

# ----------- 勝敗をセット -----------
# "win" または "lose"
result = "win"     # ←勝利
# result = "lose"  # ←敗北
# ------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 背景を黒で塗る
    screen.fill((0, 0, 0))

    # 結果によって表示画像を切り替え
    if result == "win":
        screen.blit(game_clear_img, (0, 0))
    else:
        screen.blit(game_over_img, (0, 0))

    pygame.display.update()
