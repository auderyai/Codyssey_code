# quiz_pkg/quiz.py

def get_quiz_data():
    """
    퀴즈 문제와 정답 데이터를 반환합니다.
    리스트 내에 딕셔너리 형태로 저장하여 확장성을 고려했습니다.
    """
    questions = [
        {
            "question": "파이썬에서 리스트에 요소를 추가하는 메서드는?",
            "options": ["1. append()", "2. add()", "3. insert_end()", "4. push()"],
            "answer": 1
        },
        {
            "question": "파이썬의 창시자는 누구일까요?",
            "options": ["1. 제임스 고슬링", "2. 귀도 반 로섬", "3. 데니스 리치", "4. 빌 게이츠"],
            "answer": 2
        },
        {
            "question": "다음 중 파이썬의 기본 자료형이 아닌 것은?",
            "options": ["1. int", "2. str", "3. float", "4. array"],
            "answer": 4
        }
    ]
    return questions
