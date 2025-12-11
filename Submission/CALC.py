import random
import PARAMETER

def init_deck():
    """山札を初期化してシャッフルして返す"""
    deck = PARAMETER.DECK_COMPOSITION.copy()
    random.shuffle(deck)
    return deck

# CALC.py

# 引数から stockD を削除
def draw_card(deck, stockA): 
    """
    カードを1枚引く処理
    Return: (card_type, stockA, is_skull, deck)
    """
    if not deck:
        deck = init_deck()
    
    card = deck.pop()
    is_skull = False
    
    if card == PARAMETER.CARD_SWORD:
        stockA += PARAMETER.SWORD_DMG
    # ★変更: GUARDカードのときは何もしない（MAIN_BATTLEでHP回復するため）
    elif card == PARAMETER.CARD_GUARD:
        pass 
    elif card == PARAMETER.CARD_SKULL:
        stockA = 0
        # stockD = 0 ← 削除
        is_skull = True

    # 戻り値から stockD を削除
    return card, stockA, is_skull, deck

# ★変更: 引数 stockD を削除し、防御計算なしでダメージをそのまま返す
def calc_enemy_damage(enemy_power):
    """敵の攻撃ダメージ計算（素通り）"""
    return enemy_power

def calc_player_damage(stockA):
    """プレイヤーの攻撃ダメージ計算（溜めた分すべて）"""
    damage = stockA
    return damage

def calc_enemy_damage(enemy_power, stockD):
    """
    敵の攻撃ダメージ計算
    ガード値を引いたダメージを返す（最低0）
    """
    damage = enemy_power - stockD
    if damage < 0:
        damage = 0
    return damage