import json
import os
from quiz_pkg.quiz import Quiz

STATE_FILE = "state.json"

# ── 기본 퀴즈 데이터 (파이썬 주제, 7개) ──────────────────
DEFAULT_QUIZZES = [
    Quiz("파이썬에서 주석을 작성할 때 사용하는 기호는?",
         ["//", "/* */", "#", "--"], 3),
    Quiz("파이썬 리스트에서 마지막 요소를 제거하고 반환하는 메서드는?",
         ["remove()", "pop()", "delete()", "clear()"], 2),
    Quiz("파이썬에서 정수형 타입을 나타내는 키워드는?",
         ["integer", "int", "num", "digit"], 2),
    Quiz("파이썬에서 아무것도 반환하지 않는 함수의 반환값은?",
         ["0", "False", "None", "Null"], 3),
    Quiz("파이썬 딕셔너리에서 키 목록을 가져오는 메서드는?",
         ["values()", "items()", "keys()", "get()"], 3),
    Quiz("파이썬에서 클래스를 정의할 때 사용하는 키워드는?",
         ["def", "class", "struct", "object"], 2),
    Quiz("파이썬 for 루프에서 1부터 5까지 반복할 때 올바른 range는?",
         ["range(1,5)", "range(1,6)", "range(0,5)", "range(5)"], 2),
]


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.quizzes    = []
        self.best_score = 0
        self.load_state()

    # ════════════════════════════════════════════════
    # 파일 저장 / 불러오기
    # ════════════════════════════════════════════════

    def load_state(self):
        """state.json에서 퀴즈와 최고 점수 불러오기"""
        if not os.path.exists(STATE_FILE):
            # 첫 실행: 기본 퀴즈 사용 후 저장
            self.quizzes    = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.save_state()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes    = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = data.get("best_score", 0)
        except (json.JSONDecodeError, KeyError, TypeError):
            print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
            self.quizzes    = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.save_state()

    def save_state(self):
        """퀴즈와 최고 점수를 state.json에 저장"""
        try:
            data = {
                "quizzes"   : [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"⚠️  파일 저장 중 오류가 발생했습니다: {e}")

    # ════════════════════════════════════════════════
    # 메뉴 출력
    # ════════════════════════════════════════════════

    def show_menu(self):
        print("\n========================================")
        print("         🐍 파이썬 퀴즈 게임")
        print("========================================")
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("========================================")

    # ════════════════════════════════════════════════
    # 1. 퀴즈 풀기
    # ════════════════════════════════════════════════

    def run_quiz(self):
        if not self.quizzes:
            print("\n⚠️  등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print("\n========== 퀴즈 시작! ==========")
        score = 0
        total = len(self.quizzes)

        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            user_ans = self._get_valid_number("정답 번호 입력 (1~4): ", 1, 4)
            if user_ans is None:
                return          # KeyboardInterrupt / EOFError 발생 시 복귀
            if quiz.check_answer(user_ans):
                print("  ✅ 정답입니다!")
                score += 1
            else:
                print(f"  ❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n🏁 최종 점수: {score} / {total}")

        if score > self.best_score:
            self.best_score = score
            print("🏆 새로운 최고 점수입니다!")
            self.save_state()

    # ════════════════════════════════════════════════
    # 2. 퀴즈 추가
    # ════════════════════════════════════════════════

    def add_quiz(self):
        print("\n========== 퀴즈 추가 ==========")

        question = self._get_valid_text("질문을 입력하세요: ")
        if question is None:
            return

        choices = []
        for i in range(1, 5):
            choice = self._get_valid_text(f"  보기 {i}: ")
            if choice is None:
                return
            choices.append(choice)

        answer = self._get_valid_number("정답 번호 (1~4): ", 1, 4)
        if answer is None:
            return

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("✅ 퀴즈가 추가되었습니다!")

    # ════════════════════════════════════════════════
    # 3. 퀴즈 목록
    # ════════════════════════════════════════════════

    def show_quiz_list(self):
        print("\n========== 퀴즈 목록 ==========")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n[{i}] {quiz.question}")
            for j, choice in enumerate(quiz.choices, 1):
                mark = "★" if j == quiz.answer else " "
                print(f"  {mark} {j}. {choice}")

    # ════════════════════════════════════════════════
    # 4. 점수 확인
    # ════════════════════════════════════════════════

    def show_score(self):
        print("\n========== 점수 확인 ==========")
        if self.best_score == 0:
            print("아직 퀴즈를 풀지 않았습니다. 도전해보세요! 🎯")
        else:
            total = len(self.quizzes)
            print(f"🏆 현재 최고 점수: {self.best_score} / {total}")

    # ════════════════════════════════════════════════
    # 내부 유틸 메서드
    # ════════════════════════════════════════════════

    def _get_valid_number(self, prompt, min_val, max_val):
        """유효한 숫자 입력을 받을 때까지 반복.
        KeyboardInterrupt / EOFError 발생 시 None 반환."""
        while True:
            try:
                raw = input(prompt).strip()
                if raw == "":
                    print(f"  ⚠️  값을 입력해주세요.")
                    continue
                val = int(raw)
                if min_val <= val <= max_val:
                    return val
                print(f"  ⚠️  {min_val}~{max_val} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("  ⚠️  숫자를 입력하세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️  입력이 중단되었습니다. 데이터를 저장하고 메뉴로 돌아갑니다.")
                self.save_state()
                return None

    def _get_valid_text(self, prompt):
        """빈 문자열이 아닌 텍스트 입력을 받을 때까지 반복.
        KeyboardInterrupt / EOFError 발생 시 None 반환."""
        while True:
            try:
                raw = input(prompt).strip()
                if raw == "":
                    print("  ⚠️  내용을 입력해주세요.")
                    continue
                return raw
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️  입력이 중단되었습니다. 데이터를 저장하고 메뉴로 돌아갑니다.")
                self.save_state()
                return None
