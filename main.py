from quiz_pkg import QuizGame

def main():
    game = QuizGame()

    while True:
        try:
            game.show_menu()
            choice = input("메뉴를 선택하세요 (1~5): ").strip()

            if choice == "":
                print("\n⚠️  번호를 입력해주세요.")
            elif choice == "1":
                game.run_quiz()
            elif choice == "2":
                game.add_quiz()
            elif choice == "3":
                game.show_quiz_list()
            elif choice == "4":
                game.show_score()
            elif choice == "5":
                print("\n👋 게임을 종료합니다. 수고하셨습니다!")
                game.save_state()
                break
            else:
                print("\n⚠️  1~5 사이의 번호를 입력해주세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  프로그램이 중단되었습니다. 데이터를 저장하고 종료합니다.")
            game.save_state()
            break

if __name__ == "__main__":
    main()
