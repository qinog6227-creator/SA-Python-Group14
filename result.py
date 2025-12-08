import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Result Screen")

# 画像読み込み
game_over_img = pygame.image.load("pictures/result/gameover.png")
game_clear_img = pygame.image.load("pictures/result/gameclear.png")
next_stage_img = pygame.image.load("pictures/result/next_stage.png")  # ← 追加

game_over_img = pygame.transform.scale(game_over_img, (800, 600))
game_clear_img = pygame.transform.scale(game_clear_img, (800, 600))
next_stage_img = pygame.transform.scale(next_stage_img, (800, 600))

# ----------- 勝敗とステージをセット -----------
# "win" または "lose"
result = "win"     # ← 勝ち
# result = "lose"  # ← 負け

stage = 2          # ← 現在のステージ（1 / 2 / 3）
# ----------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    # ◆ 表示ロジック ◆
    # ・負け（lose） → どのステージでも gameover
    # ・勝ち（win）かつ stage == 3 → gameclear
    # ・勝ち（win）かつ stage が 1 or 2 → next_stage

    if result == "lose":
        screen.blit(game_over_img, (0, 0))

    elif result == "win":
        if stage == 3:
            screen.blit(game_clear_img, (0, 0))      # 最終ステージ勝利
        else:
            screen.blit(next_stage_img, (0, 0))      # ステージ1、2クリア → 次へ

    pygame.display.update()
