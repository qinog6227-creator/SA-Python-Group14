#バトルのグラフィックを描画
import pygame

IMG_BG = pygame.image.load("background.png") 
FONT = pygame.font.Font(None, 40) # 文字を書く筆


def encount_bar(encount):
    print(f"--------------------{encount}戦目--------------")
    if encount == 1 or 2:
        print("--------------------vs雑魚敵-------------------")
    if encount == 3:
        print("--------------------vs魔王---------------------")


def draw_battleStatus(screen, e_hp, p_hp, stockA, stockD): 
    # 1. 画像を貼り付ける
    screen.blit(IMG_BG, (0, 0)) 

    # 2. 文字を描く (少し面倒だけど定型文)
    # 「文字の画像」を作ってから、それを貼り付ける
    text = FONT.render(f"HP: {e_hp}", True, (255, 255, 255))
    screen.blit(text, (50, 500)) # (x, y)座標
    text = FONT.render(f"HP: {p_hp}", True, (255, 255, 255))
    screen.blit(text, (50, 450)) # (x, y)座標
    text = FONT.render(f"溜める攻撃力: {p_hp}", True, (255, 255, 255))
    screen.blit(text, (50, 400)) # (x, y)座標
    text = FONT.render(f"溜める防御力: {p_hp}", True, (255, 255, 255))
    screen.blit(text, (50, 350)) # (x, y)座標

def draw_battleCommand():
    print("-----コマンド-----")
    print("d: ドロー継続")
    print("c: 攻撃実行！")

def draw_wait():
    # 入力待ちのメッセージだけ返す
    return "コマンドを入力してください >>"

# ★ここ重要！ログのリストを受け取って表示する関数
# ログも print じゃなくて画面に出す
def draw_logs(screen, logs):
    y = 100
    for msg in logs:
        text = FONT.render(msg, True, (255, 255, 255))
        screen.blit(text, (50, y))
        y += 30