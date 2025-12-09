#バトルのグラフィックを描画

def encount_bar(encount):
    print(f"--------------------{encount}戦目--------------")

def draw_battleStatus(e_hp, p_hp, stockA, stockD): 
    print("---------最新情報-----------------")
    print(f"敵のHP:{e_hp}")
    print(f"プレイヤーのHP:{p_hp}")
    print(f"溜める攻撃力:{stockA}")
    print(f"溜める防御力:{stockD}")

def draw_battleCommand():
    print("-----コマンド-----")
    print("d: ドロー継続")
    print("c: 攻撃実行！")

def draw_wait():
    # 入力待ちのメッセージだけ返す
    return "コマンドを入力してください >>"

# ★ここ重要！ログのリストを受け取って表示する関数
def draw_logs(logs):
    print("[メッセージ]")
    for msg in logs:
        print(msg)