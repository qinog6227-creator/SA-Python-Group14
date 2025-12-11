# Pmain.py
import pygame
import sys
import Ptitle
import Pmap
import PbattleG
import Presult
import Pparameter
import Pbattle_main
import PbattleC

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("サダメドロー")

font = pygame.font.Font(None, 50)
battle_logs = []

def main(screen):
    game_state = Pparameter.STATE_TITLE
    battle_phase = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # ------------------------
                # タイトル画面での操作
                # ------------------------
                if game_state == Pparameter.STATE_TITLE:
                    game_state = Pparameter.STATE_MAP

                # ------------------------
                # マップ画面での操作
                # ------------------------
                elif game_state == Pparameter.STATE_MAP:
                    # ステージ1のマップからバトルへ
                    Pbattle_main.battle_init()
                    battle_phase = Pparameter.PHASE_PLAYER_DRAW
                    battle_logs.clear()
                    game_state = Pparameter.STATE_BATTLE

                # ------------------------
                # バトル画面での操作
                # ------------------------
                elif game_state == Pparameter.STATE_BATTLE:
                    # テストとして常に0番手札を使用
                    if Pparameter.PLAYER_HAND:
                        battle_phase = Pbattle_main.player_command_phase(0)
                        Pparameter.ENEMY_CURRENT_HP, logs = PbattleC.calc_player_attack(
                            Pparameter.ENEMY_CURRENT_HP,
                            Pparameter.PLAYER_ATTACK_POWER
                        )
                        battle_logs += logs
                        # 攻撃力リセット
                        Pparameter.PLAYER_ATTACK_POWER = 0

                # ------------------------
                # 結果画面での操作
                # ------------------------
                elif game_state == Pparameter.STATE_RESULT:
                    game_state = Pparameter.STATE_TITLE

        # 画面クリア
        screen.fill((0, 0, 0))

        # ------------------------
        # 描画処理
        # ------------------------
        if game_state == Pparameter.STATE_TITLE:
            Ptitle.draw_title(screen)

        elif game_state == Pparameter.STATE_MAP:
            # マップ描画（ステージ1固定）
            Pmap.draw_map1(screen)

        elif game_state == Pparameter.STATE_BATTLE:
            # バトルフェーズの処理
            if battle_phase == Pparameter.PHASE_PLAYER_DRAW:
                battle_phase = Pbattle_main.player_draw_phase()
            elif battle_phase == Pparameter.PHASE_ENEMY_TURN:
                battle_phase, logs = Pbattle_main.enemy_phase()
                battle_logs += logs
            elif battle_phase == Pparameter.PHASE_CHECK_END:
                result = Pbattle_main.check_end_phase()
                if result == "win" or result == "lose":
                    game_state = Pparameter.STATE_RESULT
                    battle_phase = None
                else:
                    battle_phase = result

            # バトル画面描画
            PbattleG.draw_battle_screen(
                screen,
                Pparameter.PLAYER_CURRENT_HP,
                Pparameter.ENEMY_CURRENT_HP,
                Pparameter.SWORD_POWER,
                Pparameter.GUARD_POWER
            )
            PbattleG.draw_card(screen, Pparameter.PLAYER_HAND)
            PbattleG.draw_logs(screen, battle_logs[-5:])

        elif game_state == Pparameter.STATE_RESULT:
            if Pparameter.PLAYER_CURRENT_HP > 0:
                Presult.draw_winning(screen)
            else:
                Presult.draw_losing(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main(screen)
