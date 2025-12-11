import pygame
import PARAMETER

def draw_result(screen, is_win, is_clear):
    screen.fill(PARAMETER.BLACK)
    font_s = pygame.font.Font(None, 40)

    target_image = None
    sub_text_str = ""

    # 状況に応じて表示する画像とサブテキストを決定
    if not is_win:
        # 負け (GAME OVER)
        target_image = PARAMETER.IMG_GAME_OVER
        sub_text_str = "Press SPACE to Return Title"
    elif is_clear:
        # 全クリ (GAME CLEAR)
        target_image = PARAMETER.IMG_GAME_CLEAR
        sub_text_str = "Thank you for playing!"
    else:
        # 勝ち (GO TO NEXT STAGE)
        target_image = PARAMETER.IMG_NEXT_STAGE
        sub_text_str = "Press SPACE for Next Stage"

    # 画像の描画（画面中央より少し上）
    if target_image:
        # 画像の中心を指定してRectを取得
        rect = target_image.get_rect(center=(PARAMETER.SCREEN_WIDTH//2, 250))
        screen.blit(target_image, rect)

    # サブテキスト（案内表示）の描画（画像の下）
    sub = font_s.render(sub_text_str, True, PARAMETER.WHITE)
    screen.blit(sub, sub.get_rect(center=(PARAMETER.SCREEN_WIDTH//2, 450)))