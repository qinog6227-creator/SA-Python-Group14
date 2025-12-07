import Ltitle
import Lmap
import Lbattle
import Lresult

gameStart = 'a'
mapForward1 = 'a'
mapForward2 = 'a'
mapForward3 = 'a'


Ltitle.title_draw() #Ltitleのtile_draw関数を実行
while True:
    gameStart = input("王様：魔王を倒してくれるかのう？ [y + Enter]: ")
    if gameStart == "y":
        break  # 正しい入力ならループを抜ける


# ここに来た時点で select には必ず "y" が入ってる
if gameStart == 'y':
    print("ゲームスタート！")
    Lmap.map1_draw()
    while True:
        mapForward1 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward1 == "y":
            break  # 正しい入力ならループを抜ける


if mapForward1 == 'y':
    Lmap.map2_draw()
    while True:
        mapForward2 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward2 == "y":
            break  # 正しい入力ならループを抜ける


if mapForward2 == 'y':
    Lmap.map3_draw()
    while True:
        mapForward3 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward3 == "y":
            break  # 正しい入力ならループを抜ける

print("") 
print("王様：よくぞ魔王を倒してくれた！お前にこの国の宝をやろう！")