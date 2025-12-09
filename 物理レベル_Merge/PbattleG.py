import pygame

# --- 1. 準備 (画像とフォント) ---
# ※ ファイル名はチームメンバーからもらったものに合わせてね！
try:
    IMG_BG = pygame.image.load("background.png") 
    # IMG_ENEMY = pygame.image.load("enemy.png") # 敵画像があればコメント外す
except:
    # 画像がない場合のエラー回避（とりあえず黒塗りなどを代用）
    IMG_BG = None
    print("画像読み込みエラー: ファイル名を確認してください")

# フォントの準備 (Noneはデフォルトフォント)
pygame.font.init() 
FONT = pygame.font.Font(None, 40) 
WHITE = (255, 255, 255)
RED = (255, 100, 100)
YELLOW = (255, 255, 0)


def encount_bar(screen, encount):
    text_content = f"--- BATTLE {encount} ---"
    if encount == 3:
        text_content += " (BOSS: MAOU)"
    # render(文字, 滑らかにするか, 色)
    text = FONT.render(text_content, True, YELLOW)
    screen.blit(text, (20, 20)) # 左上に表示


def draw_battleStatus(screen, e_hp, p_hp, stockA, stockD): 
    # 1. 背景を貼り付ける (リセットも兼ねる)
    if IMG_BG:
        screen.blit(IMG_BG, (0, 0)) 
    else:
        screen.fill((0, 0, 0)) # 画像がなければ黒で塗りつぶし

    # 2. ステータス文字の描画
    # ★修正点: 引数の変数を正しく使うように直しました！    
    # 敵HP
    text_ehp = FONT.render(f"ENEMY HP: {e_hp}", True, RED)
    screen.blit(text_ehp, (300, 100)) # 画面中央上部

    # プレイヤーHP
    text_php = FONT.render(f"PLAYER HP: {p_hp}", True, WHITE)
    screen.blit(text_php, (50, 400)) # 左下

    # 攻撃ストック
    text_stA = FONT.render(f"STOCK ATK: {stockA}", True, WHITE)
    screen.blit(text_stA, (50, 450)) 

    # 防御ストック
    text_stD = FONT.render(f"STOCK DEF: {stockD}", True, WHITE)
    screen.blit(text_stD, (50, 500)) 


def draw_wait():
    # input用ではなく、画面下に表示するメッセージとして返す
    return "COMMAND >> CLICK BUTTON"


# ★ログのリストを受け取って表示する関数
def draw_logs(screen, logs):
    # ログを表示する開始位置（Y座標）
    y = 400 
    
    # ログが多すぎるとはみ出すので、後ろから5個だけ表示する
    display_logs = logs[-5:] 
    
    for msg in display_logs:
        text = FONT.render(msg, True, WHITE)
        # 右側のスペース（x=400以降）に表示
        screen.blit(text, (400, y))
        y -= 30 # 上に向かって積み上げる（または += 30 で下へ）