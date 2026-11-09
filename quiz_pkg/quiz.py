class Quiz:
    """개별 퀴즈를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        """
        question : 질문 문자열
        choices  : 선택지 리스트 (4개)
        answer   : 정답 번호 (1~4 정수)
        """
        self.question = question
        self.choices  = choices
        self.answer   = answer

    # ── 변환 ──────────────────────────────────────────

    def to_dict(self):
        """JSON 저장용 딕셔너리 변환"""
        return {
            "question": self.question,
            "choices" : self.choices,
            "answer"  : self.answer
        }

    @staticmethod
    def from_dict(data):
        """딕셔너리 → Quiz 객체"""
        return Quiz(data["question"], data["choices"], data["answer"])

    # ── 출력 ──────────────────────────────────────────

    def display(self, index):
        """문제와 선택지 출력"""
        print(f"\n[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    # ── 정답 확인 ─────────────────────────────────────

    def check_answer(self, user_answer):
        """정답이면 True, 오답이면 False"""
        return user_answer == self.answer
