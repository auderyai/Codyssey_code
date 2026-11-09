# quiz_pkg/game.py

from quiz_pkg.quiz import get_quiz_data

def run_quiz():
    """
    퀴즈 게임을 실행하는 메인 함수입니다.
    문제를 출력하고, 정답을 확인하여 최종 점수를 반환합니다.
    """
    questions = get_quiz_data()
    score = 0
    total = len(questions)

    print("=" * 40)
    print("     🐍 파이썬 퀴즈 게임을 시작합니다!")
    print("=" * 40)

    for i, q in enumerate(questions):
        print(f"\nQ{i + 1}. {q['question']}")
        for option in q['options']:
            print(f"   {option}")

        # 사용자 입력 받기 (1~4 숫자만 허용)
        while True:
            try:
                user_input = int(input("\n정답 번호를 입력하세요 (1~4): "))
                if 1 <= user_input <= 4:
                    break
                else:
                    print("⚠️  1부터 4 사이의 숫자를 입력해 주세요.")
            except ValueError:
                print("⚠️  숫자만 입력해 주세요.")

        # 정답 확인
        if user_input == q['answer']:
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 오답입니다. 정답은 {q['answer']}번이었습니다.")
    # 최종 결과 출력
    print("\n" + "=" * 40)
    print(f"🏆 최종 점수: {score} / {total}")
    print("=" * 40)
