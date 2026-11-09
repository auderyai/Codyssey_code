# 🐍 Python Quiz Game

파이썬 기초 개념을 퀴즈로 학습할 수 있는 CLI 기반 퀴즈 게임입니다.

## 📁 프로젝트 구조

python-quiz-project/
├── main.py              # 프로그램 진입점
├── quiz_pkg/
│   ├── __init__.py      # 패키지 초기화
│   ├── quiz.py          # Quiz 클래스 정의
│   └── game.py          # QuizGame 클래스 (게임 로직)
├── state.json           # 퀴즈 및 점수 저장 파일
├── .gitignore
└── README.md

## ⚙️ 실행 방법

```bash
python main.py
```
🕹️ 주요 기능
기능	설명
퀴즈 풀기	파이썬 관련 객관식 문제 풀이
퀴즈 추가	새로운 문제 직접 추가
퀴즈 목록	전체 문제 목록 확인
점수 확인	최고 점수 기록 확인
저장/불러오기	state.json으로 데이터 유지
🛠️ 기술 스택
Python 3
JSON (데이터 저장)
Git / GitHub (버전 관리)
👤 개발자
auderyai
