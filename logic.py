import battle_parameter

gameStart = 'a'
mapForward1 = 'a'
mapForward2 = 'a'
mapForward3 = 'a'

def tile_draw():
    print("")
    print("-----Store/Trash-----")
    print("press [s + Enter] to START")
    print("")

def map_draw1():
    print("")
    print("-----Map--------------")
    print("★：クリア地点    ☆：NEXT")
    print("★-----☆-----？-----？")
    print("")

def map_draw2():
    print("")
    print("-----Map--------------")
    print("★：クリア地点    ☆：NEXT")   
    print("★----★-----☆-----？")
    print("")

def map_draw3():
    print
    print("-----Map--------------")
    print("★：クリア地点    ☆：NEXT")   
    print("★----★-----★-----☆")
    print("")
    

tile_draw()
while True:
    gameStart= input("王様：魔王を倒してくれるかのう？ [y + Enter]: ")
    if gameStart == "y":
        break  # 正しい入力ならループを抜ける
    print("王様：魔王を倒してくれるかのう？ [y+ Enter]: ")
    # ここでループの先頭に戻って、もう一度 input させる

# ここに来た時点で select には必ず "y" が入ってる
if gameStart == 'y':
    print("ゲームスタート！")
    map_draw1()

    while True:
        gameStart= input("先へ進みますか？ [y + Enter]: ")
        if gameStart1 == "y":
            break  # 正しい入力ならループを抜ける
    map_draw1()
    print("先へ進みますか？ [y+ Enter]: ")
    # ここでループの先頭に戻って、もう一度 input させる


if mapForward == 'y':
    map_draw2()

    while True:
        gameStart= input("先へ進みますか？ [y + Enter]: ")
        if gameStart == "y":
            break  # 正しい入力ならループを抜ける
    map_draw2()
    print("先へ進みますか？ [y+ Enter]: ")
    # ここでループの先頭に戻って、もう一度 input させる