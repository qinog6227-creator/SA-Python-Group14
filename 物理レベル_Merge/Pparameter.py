# Pparameter.py (バトルロジック対応・完全版)

# --- 1. ゲームの状態定数 ---
STATE_TITLE = "title"
STATE_MAP = "map"
STATE_BATTLE = "battle"
STATE_RESULT = "result"
STATE_QUIT = "quit"

# ★追加：バトルのフェーズ管理（戦闘中の内部状態）
# Pbattle_main.py で処理を分けるために必須です
PHASE_PLAYER_DRAW = "p_draw"   # プレイヤーがドローする待ち時間
PHASE_PLAYER_COMMAND = "p_command" # プレイヤーがカードを選択・実行するフェーズ
PHASE_ENEMY_TURN = "e_turn"    # 敵が攻撃・行動するフェーズ
PHASE_CHECK_END = "check_end"  # 勝敗判定フェーズ


# --- パラメータ設定 ---
PLAYER_MAX_HP = 30
ENEMY_MAX_HP = 5

# ★追加：現在のゲームデータ（Pbattle_main.pyで操作される）
PLAYER_CURRENT_HP = 30  # ★修正：MAX HPと同じ初期値に直す
ENEMY_CURRENT_HP = 5

# ★追加：プレイヤーの攻撃力蓄積値と防御力蓄積値
PLAYER_ATTACK_POWER = 0 # 剣カードで溜まった攻撃力
PLAYER_DEFENSE_POWER = 0 # ガードカードで溜まった防御力

# ★追加：現在のステージ番号
CURRENT_STAGE = 1 # 敵の強さリストと連携させる


# ステージごとの敵の攻撃力
ENEMY_POWER_LIST = [2, 4, 6] # ステージ1, 2, 3... の敵の攻撃力


# --- カードの効果（Pbattle_main.pyのロジック用） ---
SWORD_POWER = 1  # 剣1枚で溜まる攻撃力
GUARD_POWER = 1  # ガードでのHP増強量

# ★追加：カードの種類定義（グラフィックとロジックを連携させる）
CARD_ATTACK = 1  # 剣
CARD_GUARD = 2   # ガード
CARD_SKULL = 3   # ドクロ

# --- デッキ (1:剣, 2:ガード, 3:ドクロ) ---
# ※ Pbattle_main.py で global 宣言して操作します
DECK_LIST = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
             1, 1, 1, 1, 1, 1, 1,
             2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] 

# ★追加：プレイヤーの現在の手札と山札（Pbattle_main.pyで操作）
PLAYER_HAND = [] # プレイヤーの手札（初期は空）
CURRENT_DECK = [] # シャッフルされた山札（初期は空）


# --- マクロ/ユーティリティ関数（描画のget_rectを使う） ---

# 画像を画面ど真ん中に揃える
def centering (name):
    # PygameのSurfaceやRectオブジェクトを受け取る
    rect = name.get_rect(center=(400, 300))
    return rect

# 画像を横半分（中央）に揃える
def centeringY (name, y):
    # PygameのSurfaceやRectオブジェクトを受け取る
    rect = name.get_rect(center=(400, y))
    return rect

# 画像を縦半分に揃える
def centeringX (name, x):
    # PygameのSurfaceやRectオブジェクトを受け取る
    rect = name.get_rect(center=(x, 300))
    return rect