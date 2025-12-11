import pygame
import sys
import Pparameter
import Ptitle
import Pmap
import Pbattle_main
import Presult

def main():
    pygame.init()
    screen = pygame.display.set_mode(Pparameter.SCREEN_SIZE)
    pygame.display.set_caption("SADAME DRAW - Heian Bozu Attack -")
    clock = pygame.time.Clock()

    # ゲーム全体の状態管理
    state = "title" # title, map, battle, result
    
    # プレイヤーデータ
    current_stage = 0 # 今クリアしているステージ (0=未クリア)
    player_hp = Pparameter.PLAYER_MAX_HP
    
    battle_result_flag = False # 勝ったかどうか

    while True:
        # イベント処理（共通の終了処理のみ）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # タイトル画面の入力
            if state == "title":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        # ゲーム開始初期化
                        current_stage = 0
                        player_hp = Pparameter.PLAYER_MAX_HP
                        state = "map"

            # リザルト画面の入力
            if state == "result":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if battle_result_flag: # 勝ち
                            if current_stage == 3: # 全クリ
                                state = "title"
                            else:
                                state = "map"
                        else: # 負け
                            state = "title"

        # --- 各シーンの描画・更新 ---
        
        if state == "title":
            Ptitle.draw_title(screen)

        elif state == "map":
            selected = Pmap.draw_map(screen, current_stage)
            if selected is not None:
                # バトル開始へ遷移
                # Pbattle_mainを呼び出して制御を渡す
                # メインループを一時的に抜けてバトルループに入るような挙動
                res, new_hp = Pbattle_main.battle_loop(screen, selected, player_hp)
                
                # バトル終了後
                player_hp = new_hp
                if res == "win":
                    current_stage = selected
                    battle_result_flag = True
                else:
                    battle_result_flag = False
                
                state = "result"

        elif state == "result":
            is_clear = (current_stage == 3 and battle_result_flag)
            Presult.draw_result(screen, battle_result_flag, is_clear)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()