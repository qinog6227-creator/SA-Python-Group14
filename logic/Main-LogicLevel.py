import Ltitle
import Lmap
import Lbattle
import Lresult
import Lbattle

gameStart = 'a'
mapForward1 = 'a'
mapForward2 = 'a'
mapForward3 = 'a'
amout_win = 0
result_battle = "none"

Ltitle.title_draw() #Ltitleのtile_draw関数を実行
#do-while文と同じ働きをする
while True:
    gameStart = input("press [s + Enter] to START:")
    if gameStart == "s":
        break  # 正しい入力ならループを抜ける

gameStart = 'a'
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
    print("") 
    result_battle = Lbattle.battle()
    if result_battle == "lose":
        Lresult.losing()
        exit()

if mapForward1 == 'y':
    Lmap.map2_draw()
    while True:
        mapForward2 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward2 == "y":
            break  # 正しい入力ならループを抜ける
    print("") 
    result_battle = Lbattle.battle()
    if result_battle == "lose":
        Lresult.losing()
        exit()

if mapForward2 == 'y':
    Lmap.map3_draw()
    while True:
        mapForward3 = input("先へ進みますか？ [y + Enter]: ")
        if mapForward3 == "y":
            break  # 正しい入力ならループを抜ける
    print("") 
    result_battle = Lbattle.battle()
    if result_battle == "lose":
        Lresult.losing()
        exit()

print("王様：よくぞ魔王を倒してくれた！お前にこの国の宝をやろう！")