import pygame
import sys
import title
import map

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("ゲームタイトル")

    font1 = pygame.font.Font(
        r"C:\Users\user\Desktop\SA-Python-Group14\font\PixelMplus12R.ttf",
        40
    )

    state = "title"
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if state == "title" and event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                    state = "map"
                if state == "map" and event.key == pygame.K_ESCAPE:
                    state = "title"

        if state == "title":
            title.draw_title(screen, font1)
        elif state == "map":
            map.draw_map(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
