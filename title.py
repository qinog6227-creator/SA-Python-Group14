import pygame
import map  # map.py をインポート

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("タイトル画面")

w = screen.get_width() // 2
h = screen.get_height() // 2

font1 = pygame.font.SysFont("meiryo", 35)   
font2 = pygame.font.SysFont("meiryo", 50)

show_map = False  # マップ画面を表示するかどうか

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                show_map = True  # フラグを立てる
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                show_map = False  # 離したら戻す

    if show_map:
        map.show_map(screen)  # フラグが True の時だけ関数を呼ぶ
        continue  # map が終了したら次のループへ

    # タイトル画面描画
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (w - 250, h - 150,500,300))

    text = font1.render("坊主めくり × カードバトル", True, (255, 255, 255))
    text_rect = text.get_rect(center=(w, h-50))
    screen.blit(text, text_rect)

    text = font2.render("Heian Bozu Attak", True, (255, 255, 255))
    text_rect = text.get_rect(center=(w, h+50))
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
