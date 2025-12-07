import Ltitle
import Lmap
import Lbattle
import Lresult

gameStart = 'a'
mapForward1 = 'a'
mapForward2 = 'a'
mapForward3 = 'a'


Ltitle.tile_draw()

while True:
    gameStart = input("王様：魔王を倒してくれるかのう？ [y + Enter]: ")
    if gameStart == "y":
        break  # 正しい入力ならループを抜ける

# ここに来た時点で select には必ず "y" が入ってる
if gameStart == 'y':
    print("ゲームスタート！")
    Lmap.map_draw1()
    while True:
        mapForward1 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward1 == "y":
            break  # 正しい入力ならループを抜ける


if mapForward1 == 'y':
    map_draw2()
    while True:
        mapForward2 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward2 == "y":
            break  # 正しい入力ならループを抜ける


if mapForward2 == 'y':
    map_draw3()
    while True:
        mapForward3 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward3 == "y":
            break  # 正しい入力ならループを抜ける

print("") 
print("王様：よくぞ魔王を倒してくれた！お前にこの国の宝をやろう！")