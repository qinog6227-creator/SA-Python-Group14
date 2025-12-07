import random

# ==========================================
# 1. 設定・データエリア (Config)
#    C言語の #define や 構造体定義 みたいな場所
# ==========================================
MAX_HP = 30
DECK_INIT = [1, 1, 1, 2, 3, 4]  # 1:剣, 2:回復...

# ==========================================
# 2. ロジック関数エリア (Logic)
#    計算だけする。printは絶対しない！
#    C言語の int calc_damage(...) みたいな場所
# ==========================================

def init_game():
    # 最初のデータを作る
    return {
        "p_hp": MAX_HP,
        "e_hp": 50,
        "stock": 0,
        "deck": list(DECK_INIT) # コピーして使う
    }

def draw_card(state):
    # カードを引いて計算する
    if len(state["deck"]) == 0:
        state["deck"] = list(DECK_INIT) # 山札補充
    
    card = random.choice(state["deck"])
    state["deck"].remove(card) # 引いたカードを消す
    
    msg = ""
    # --- ここに効果のif文を書く ---
    if card == 1:
        state["stock"] += 1
        msg = "剣を引いた！攻撃力チャージ！"
    elif card == 2:
        state["p_hp"] += 5
        msg = "回復薬！HPが回復した"
        
    return state, msg

# ==========================================
# 3. 表示関数エリア (View)
#    画面を表示する。計算はしない！
#    明日は「ここだけ」をPygameに書き換える
# ==========================================

def show_screen(state, message):
    # 画面をクリア（改行をいっぱい入れてクリアっぽく見せる技）
    print("\n" * 50) 
    
    print("--------------------------------")
    print(f" 勇者HP: {state['p_hp']}   VS   魔王HP: {state['e_hp']}")
    print(f" 溜め攻撃力: {state['stock']}")
    print("--------------------------------")
    print(f"【状況】 {message}")
    print("--------------------------------")

# ==========================================
# 4. メイン実行エリア (Main Loop)
#    司令塔。whileループで回す
# ==========================================

# ゲーム開始の準備
current_state = init_game()
current_msg = "ゲームスタート！Enterを押してね"

while True:
    # (1) 画面を表示させる
    show_screen(current_state, current_msg)
    
    # (2) 入力を待つ
    key = input("コマンド (Enter:ドロー / q:終了) >> ")
    
    if key == "q":
        print("ゲーム終了")
        break
        
    # (3) ロジックを呼んで計算させる
    # 返ってきた新しいデータ(new_state)で情報を更新する
    current_state, current_msg = draw_card(current_state)
    
    # (4) 死亡判定など
    if current_state["e_hp"] <= 0:
        print("勝利！")
        break