import random
import PARAMETER

def init_deck():
    """山札を初期化してシャッフルして返す"""
    deck = PARAMETER.DECK_COMPOSITION.copy()
    random.shuffle(deck)
    return deck

def draw_card(deck, stockA, stockD):
    """
    カードを1枚引く処理
    Return: (card_type, stockA, stockD, is_skull, deck)
    """
    if not deck:
        deck = init_deck() # 山札切れなら補充
    
    card = deck.pop()
    is_skull = False
    
    if card == PARAMETER.CARD_SWORD:
        stockA += PARAMETER.SWORD_DMG
    elif card == PARAMETER.CARD_GUARD:
        stockD += PARAMETER.GUARD_VAL
    elif card == PARAMETER.CARD_SKULL:
        # ドクロ：全没収
        stockA = 0
        stockD = 0
        is_skull = True

    return card, stockA, stockD, is_skull, deck

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