# 🐍 파이썬 퀴즈 게임

Python으로 만든 터미널 기반 퀴즈 게임입니다.  
퀴즈를 풀고, 추가하고, 점수를 관리할 수 있습니다.

---

## 📁 프로젝트 구조

```
python-quiz-project/
├── main.py              # 프로그램 진입점
├── state.json           # 퀴즈 및 점수 저장 파일 (자동 생성)
└── quiz_pkg/
    ├── __init__.py
    ├── quiz.py          # Quiz 클래스
    └── game.py          # QuizGame 클래스
```

---

## 🏗️ 클래스 구조

### `Quiz` (quiz_pkg/quiz.py)

| 속성 / 메서드 | 라인 | 설명 |
|---|---|---|
| `question` | L11 | 질문 문자열 |
| `choices` | L12 | 선택지 리스트 (4개) |
| `answer` | L13 | 정답 번호 (1~4 정수) |
| `to_dict()` | L17 | JSON 저장용 딕셔너리 변환 |
| `from_dict(data)` | L25 | 딕셔너리 → Quiz 객체 (정적 메서드) |
| `display(index)` | L30 | 문제와 선택지 출력 |
| `check_answer(user_answer)` | L36 | 정답이면 `True`, 오답이면 `False` |

### `QuizGame` (quiz_pkg/game.py)

| 속성 / 메서드 | 라인 | 설명 |
|---|---|---|
| `quizzes` | L37 | 퀴즈 목록 (Quiz 객체 리스트) |
| `best_score` | L38 | 현재까지의 최고 점수 |
| `load_state()` | L44 | `state.json`에서 퀴즈와 점수 불러오기 |
| `save_state()` | L62 | 퀴즈와 점수를 `state.json`에 저장 |
| `show_menu()` | L76 | 메인 메뉴 출력 |
| `run_quiz()` | L90 | 퀴즈 풀기 진행 |
| `add_quiz()` | L114 | 새 퀴즈 추가 |
| `show_quiz_list()` | L134 | 등록된 퀴즈 목록 출력 |
| `show_score()` | L147 | 최고 점수 출력 |
| `_get_valid_number()` | L157 | 유효한 숫자 입력 받기 |
| `_get_valid_text()` | L174 | 유효한 텍스트 입력 받기 |

---

## ⚙️ 주요 기능

### 1. 퀴즈 풀기
- 등록된 퀴즈를 순서대로 출력합니다.
- 1~4번 중 정답 번호를 입력합니다.
- 최종 점수가 최고 점수를 넘으면 자동 저장됩니다.

### 2. 퀴즈 추가
- 질문, 보기 4개, 정답 번호를 입력해 새 퀴즈를 등록합니다.
- 추가 즉시 `state.json`에 저장됩니다.

### 3. 퀴즈 목록
- 등록된 모든 퀴즈와 선택지를 출력합니다.
- 정답 보기에는 `★` 표시가 붙습니다.

### 4. 점수 확인
- 지금까지의 최고 점수를 확인합니다.

### 5. 종료
- 데이터를 저장하고 프로그램을 종료합니다.

---

## 🔄 실행 흐름

```
main.py
└── main()
    ├── QuizGame 객체 생성 → load_state() 자동 실행
    └── while True 메인 루프
        ├── 1 → run_quiz()
        ├── 2 → add_quiz()
        ├── 3 → show_quiz_list()
        ├── 4 → show_score()
        ├── 5 → save_state() → 종료
        └── Ctrl+C / EOFError → save_state() → 안전 종료
```

---

## 🛡️ 예외 처리

## 예외 처리 목록

### 1. 공백 제거 (`strip()`)
- 📄 `quiz_pkg/game.py` L161, L177
```python
raw = input(prompt).strip()  # ✅ 있음
```
`_get_valid_number` (L161), `_get_valid_text` (L177) 둘 다 적용됩니다.

---

### 2. 숫자 변환 실패 안내 + 재입력
- 📄 `quiz_pkg/game.py` L168
```python
except ValueError:
    print("  ⚠️  숫자를 입력하세요.")
# while True 루프로 재입력 흐름 복귀
```

---

### 3. 범위 밖 숫자 안내 + 재입력
- 📄 `quiz_pkg/game.py` L164
```python
if min_val <= val <= max_val:
    return val
print(f"  ⚠️  {min_val}~{max_val} 사이의 숫자를 입력하세요.")
# while True 루프 계속
```

---

### 4. 빈 입력 안내 + 재입력
- 📄 `quiz_pkg/game.py` L162, L178
```python
if raw == "":
    print(f"  ⚠️  값을 입력해주세요.")
    continue
```
`_get_valid_number` (L162), `_get_valid_text` (L178) 둘 다 처리됩니다.

---

### 5. KeyboardInterrupt / EOFError 처리
- 📄 `quiz_pkg/game.py` L170 — QuizGame 내부 메서드
```python
except (KeyboardInterrupt, EOFError):
    print("\n\n⚠️  입력이 중단되었습니다. 데이터를 저장하고 메뉴로 돌아갑니다.")
    self.save_state()
    return None
```
- 📄 `main.py` — 메인 루프
```python
except (KeyboardInterrupt, EOFError):
    print("\n\n⚠️  프로그램이 중단되었습니다. 데이터를 저장하고 종료합니다.")
    game.save_state()
    break
```

---

### 6. 파일 없을 때 기본 데이터 사용
- 📄 `quiz_pkg/game.py` L46
```python
if not os.path.exists(STATE_FILE):
    self.quizzes    = list(DEFAULT_QUIZZES)
    self.best_score = 0
    self.save_state()
    return
```

---

### 7. 파일 손상 시 안내 + 기본 데이터 복구
- 📄 `quiz_pkg/game.py` L57
```python
except (json.JSONDecodeError, KeyError, TypeError):
    print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
    self.quizzes    = list(DEFAULT_QUIZZES)
    self.best_score = 0
    self.save_state()
```

---

### ✅ 예외 처리 체크 결과

| # | 항목 | 결과 |
|---|------|------|
| 1 | 공백 제거 후 처리 | ✅ |
| 2 | 숫자 변환 실패 처리 | ✅ |
| 3 | 범위 밖 숫자 처리 | ✅ |
| 4 | 빈 입력 처리 | ✅ |
| 5 | KeyboardInterrupt / EOFError | ✅ |
| 6 | 파일 없을 때 기본 데이터 | ✅ |
| 7 | 파일 손상 시 복구 | ✅ |

---

## 💾 데이터 저장 방식

- 저장 파일: `state.json`
- 인코딩: `UTF-8`
- 저장 시점: 퀴즈 추가, 최고 점수 갱신, 비정상 종료 시

```json
{
  "quizzes": [
    {
      "question": "파이썬에서 주석을 작성할 때 사용하는 기호는?",
      "choices": ["//", "/* */", "#", "--"],
      "answer": 3
    }
  ],
  "best_score": 5
}
```

---

## 🚀 실행 방법

```bash
# 저장소 클론
git clone https://github.com/auderyai/python-quiz-project.git
cd python-quiz-project

# 실행 (Python 3.x 필요)
python main.py
```

---

# 🐍 파이썬 퀴즈 게임

Python으로 구현한 터미널 기반 퀴즈 게임입니다.

---

## 📁 프로젝트 구조

```
quiz_project/
├── main.py              # 프로그램 진입점
├── state.json           # 퀴즈·점수 저장 파일 (자동 생성)
└── quiz_pkg/
    ├── __init__.py
    ├── quiz.py          # Quiz 클래스
    └── game.py          # QuizGame 클래스
```

---

## ▶️ 실행 방법

```bash
python main.py
```

---

## 📋 메뉴 기능

| 번호 | 기능 |
|------|------|
| 1 | 퀴즈 풀기 |
| 2 | 퀴즈 추가 |
| 3 | 퀴즈 목록 |
| 4 | 점수 확인 |
| 5 | 종료 |

---

## ✅ 요구사항 구현 목록

### 📦 Quiz 클래스 (`quiz_pkg/quiz.py`)

| # | 요구사항 | 구현 여부 | 파일·라인 |
|---|----------|-----------|-----------|
| 1 | `question`, `choices`, `answer` 속성 | ✅ | `quiz.py` L8~L10 |
| 2 | 선택지 4개 기본 | ✅ | `quiz.py` L8 `choices` 리스트 |
| 3 | 정답은 1~4 번호로 관리 | ✅ | `quiz.py` L10 `answer` 정수 |
| 4 | 퀴즈 출력 메서드 | ✅ | `quiz.py` L33 `display(index)` |
| 5 | 정답 확인 메서드 | ✅ | `quiz.py` L40 `check_answer()` |

---

### 📝 퀴즈 데이터 (`quiz_pkg/game.py`)

| # | 요구사항 | 구현 여부 | 파일·라인 |
|---|----------|-----------|-----------|
| 6 | 주제 퀴즈 5개 이상 직접 작성 | ✅ 7개 | `game.py` L9~L26 |
| 7 | 문제 + 선택지 4개 + 정답 포함 | ✅ | `game.py` L9~L26 |
| 8 | `Quiz` 클래스 인스턴스로 생성 | ✅ | `game.py` L9 `Quiz(...)` |

---

### 🎮 퀴즈 풀기 (`quiz_pkg/game.py`)

| # | 요구사항 | 구현 여부 | 파일·라인 |
|---|----------|-----------|-----------|
| 9 | 저장된 퀴즈 출제 | ✅ | `game.py` L88 `run_quiz()` |
| 10 | 사용자 정답 입력 | ✅ | `game.py` L97 `_get_valid_number()` |
| 11 | 정답/오답 여부 안내 | ✅ | `game.py` L99~L102 |
| 12 | 모든 문제 풀면 결과 표시 | ✅ | `game.py` L104 점수 출력 |
| 13 | 퀴즈 없는 경우 처리 | ✅ | `game.py` L89~L91 |

---

### ➕ 퀴즈 추가 (`quiz_pkg/game.py`)

| # | 요구사항 | 구현 여부 | 파일·라인 |
|---|----------|-----------|-----------|
| 14 | 새 퀴즈 등록 기능 | ✅ | `game.py` L114 `add_quiz()` |
| 15 | 문제 + 선택지 4개 + 정답 번호 입력 | ✅ | `game.py` L117~L128 |
| 16 | 잘못된 입력 예외 처리 | ✅ | `game.py` L155~L181 |
| 17 | 추가한 퀴즈 파일 저장 | ✅ | `game.py` L130 `save_state()` |

---

### 📋 퀴즈 목록 (`quiz_pkg/game.py`)

| # | 요구사항 | 구현 여부 | 파일·라인 |
|---|----------|-----------|-----------|
| 18 | 퀴즈 목록 확인 기능 | ✅ | `game.py` L137 `show_quiz_list()` |
| 19 | 퀴즈 없는 경우 처리 | ✅ | `game.py` L139~L141 |

---

### 🏆 최고 점수 (`quiz_pkg/game.py`)

| # | 요구사항 | 구현 여부 | 파일·라인 |
|---|----------|-----------|-----------|
| 20 | 최고 점수 확인 기능 | ✅ | `game.py` L150 `show_score()` |
| 21 | 퀴즈 풀 때마다 비교·갱신 | ✅ | `game.py` L106~L109 |
| 22 | 최고 점수 파일 저장 | ✅ | `game.py` L62 `save_state()` |
| 23 | 아직 풀지 않은 경우 처리 | ✅ | `game.py` L152~L153 |

---

## 🛡️ 예외 처리 목록

### 1. 공백 제거 (`strip()`)
- 📄 `quiz_pkg/game.py` L161, L177
```python
raw = input(prompt).strip()
```
`_get_valid_number` (L161), `_get_valid_text` (L177) 둘 다 적용됩니다.

---

### 2. 숫자 변환 실패 안내 + 재입력
- 📄 `quiz_pkg/game.py` L168
```python
except ValueError:
    print("  ⚠️  숫자를 입력하세요.")
# while True 루프로 재입력 흐름 복귀
```

---

### 3. 범위 밖 숫자 안내 + 재입력
- 📄 `quiz_pkg/game.py` L164~L165
```python
if min_val <= val <= max_val:
    return val
print(f"  ⚠️  {min_val}~{max_val} 사이의 숫자를 입력하세요.")
# while True 루프 계속
```

---

### 4. 빈 입력 안내 + 재입력
- 📄 `quiz_pkg/game.py` L162~L163, L178~L179
```python
if raw == "":
    print("  ⚠️  값을 입력해주세요.")
    continue
```
`_get_valid_number` (L162), `_get_valid_text` (L178) 둘 다 처리됩니다.

---

### 5. KeyboardInterrupt / EOFError — 내부 메서드
- 📄 `quiz_pkg/game.py` L170~L173
```python
except (KeyboardInterrupt, EOFError):
    print("\n\n⚠️  입력이 중단되었습니다. 데이터를 저장하고 메뉴로 돌아갑니다.")
    self.save_state()
    return None
```

### 5-2. KeyboardInterrupt / EOFError — 메인 루프
- 📄 `main.py` L21~L24
```python
except (KeyboardInterrupt, EOFError):
    print("\n\n⚠️  프로그램이 중단되었습니다. 데이터를 저장하고 종료합니다.")
    game.save_state()
    break
```

---

### 6. 파일 없을 때 기본 데이터 사용
- 📄 `quiz_pkg/game.py` L44~L48
```python
if not os.path.exists(STATE_FILE):
    self.quizzes    = list(DEFAULT_QUIZZES)
    self.best_score = 0
    self.save_state()
    return
```

---

### 7. 파일 손상 시 안내 + 기본 데이터 복구
- 📄 `quiz_pkg/game.py` L55~L59
```python
except (json.JSONDecodeError, KeyError, TypeError):
    print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
    self.quizzes    = list(DEFAULT_QUIZZES)
    self.best_score = 0
    self.save_state()
```

---

## 🎯 구현 달성률

```
요구사항  23개 중 23개 ✅
예외처리   8개 중  8개 ✅
전체 달성률: 100% 🎉
```

---

## 🎮 QuizGame 클래스 (`quiz_pkg/game.py`)

### 속성·메서드 목록

| # | 요구사항 | 구현 여부 | 파일·라인 | 코드 근거 |
|---|----------|-----------|-----------|-----------|
| 1 | `QuizGame` 클래스 정의 | ✅ | `game.py` L29 | `class QuizGame:` |
| 2 | 속성: 퀴즈 목록 | ✅ | `game.py` L33 | `self.quizzes = []` |
| 3 | 속성: 최고 점수 | ✅ | `game.py` L34 | `self.best_score = 0` |
| 4 | 메서드: 메뉴 표시 | ✅ | `game.py` L70 | `show_menu()` |
| 5 | 메서드: 퀴즈 풀기 | ✅ | `game.py` L88 | `run_quiz()` |
| 6 | 메서드: 퀴즈 추가 | ✅ | `game.py` L114 | `add_quiz()` |
| 7 | 메서드: 목록 보기 | ✅ | `game.py` L137 | `show_quiz_list()` |
| 8 | 메서드: 점수 확인 | ✅ | `game.py` L150 | `show_score()` |
| 9 | 메서드: 파일 저장 | ✅ | `game.py` L55 | `save_state()` |
| 10 | 메서드: 파일 불러오기 | ✅ | `game.py` L39 | `load_state()` |

---

### 💾 파일 저장/불러오기 (`state.json`)

| # | 요구사항 | 구현 여부 | 파일·라인 | 코드 근거 |
|---|----------|-----------|-----------|-----------|
| 11 | 프로젝트 루트에 `state.json` 저장 | ✅ | `game.py` L5 | `STATE_FILE = "state.json"` |
| 12 | UTF-8 인코딩 | ✅ | `game.py` L50, L62 | `encoding="utf-8"` |
| 13 | JSON 파일에서 데이터 불러오기 | ✅ | `game.py` L50~L53 | `json.load(f)` |
| 14 | 파일 없을 때 기본 퀴즈 사용 | ✅ | `game.py` L44~L48 | `os.path.exists()` 체크 후 `DEFAULT_QUIZZES` |
| 15 | 파일 손상 `try/except` 처리 | ✅ | `game.py` L55~L59 | `json.JSONDecodeError, KeyError, TypeError` |
| 16 | 읽기/쓰기 오류 `try/except` 처리 | ✅ | `game.py` L63~L68 | `OSError` |
| 17 | 스키마 키: `quizzes` | ✅ | `game.py` L59 | `data.get("quizzes", [])` |
| 18 | 스키마 키: `best_score` | ✅ | `game.py` L60 | `data.get("best_score", 0)` |

---

### 🔍 핵심 코드

**① 클래스 속성 초기화**
```python
# game.py L29~L35
class QuizGame:
    def __init__(self):
        self.quizzes    = []   # 퀴즈 목록
        self.best_score = 0    # 최고 점수
        self.load_state()      # 시작 시 자동 불러오기
```

**② state.json 저장 (UTF-8 + OSError 처리)**
```python
# game.py L55~L68
def save_state(self):
    try:
        data = {
            "quizzes"   : [q.to_dict() for q in self.quizzes],  # quizzes 키
            "best_score": self.best_score                         # best_score 키
        }
        with open(STATE_FILE, "w", encoding="utf-8") as f:       # UTF-8
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as e:                                          # 쓰기 오류 처리
        print(f"⚠️  파일 저장 중 오류가 발생했습니다: {e}")
```

**③ state.json 불러오기 (파일 없음 + 손상 처리)**
```python
# game.py L39~L59
def load_state(self):
    if not os.path.exists(STATE_FILE):           # 파일 없음 → 기본 퀴즈
        self.quizzes    = list(DEFAULT_QUIZZES)
        self.best_score = 0
        self.save_state()
        return
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:  # UTF-8
            data = json.load(f)
        self.quizzes    = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
        self.best_score = data.get("best_score", 0)
    except (json.JSONDecodeError, KeyError, TypeError):      # 손상 처리
        print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
        self.quizzes    = list(DEFAULT_QUIZZES)
        self.best_score = 0
        self.save_state()
```

## 📝 Git 커밋 이력

> `git log --oneline --graph` 실행 결과

```
* 806989c (HEAD -> main, origin/main) Docs: README.md 작성
* 70fc7c2 Chore: state.json 추가 및 임시 파일 정리
* 8ae0b53 Test: pull 실습용 파일 추가
* 80e7942 Docs: README.md 작성 (프로젝트 설명, 구조, 기능)
* f89e1bc (origin/feature/full-implementation, feature/full-implementation) Feat: 입력 예외 처리 추가
* 3777e22 Feat: state.json 저장 및 불러오기 구현 (UTF-8)
* 9b0c420 Feat: 최고 점수 확인 및 갱신 기능 구현
* 334b866 Feat: 퀴즈 목록 출력 기능 구현
* ca0b9bd Feat: 퀴즈 추가 기능 구현
* a0a88b5 Feat: 퀴즈 풀기 기능 구현 (정답 확인, 점수 계산)
* 7ca737e Chore: quiz_pkg __init__.py 패키지 초기화
* df9deb4 Feat: 메뉴 출력 및 선택 기능 구현
* 704a36e Feat: 기본 퀴즈 데이터 7개 추가 (파이썬 주제)
* bf25353 Feat: Quiz 클래스 정의 (question, choices, answer)
* fea731f Feat: 퀴즈 게임 기본 로직 구현 완료
* 7729abe Feat: 프로젝트 초기 구조 및 패키지 생성
```


### 커밋 타입별 통계
| 타입 | 개수 |
|------|------|
| `Feat` | 11개 |
| `Docs` | 2개 |
| `Chore` | 2개 |
| `Test` | 1개 |
| **합계** | **16개** |


## 🌿 Git 브랜치 전략

| 브랜치 | 용도 |
|---|---|
| `main` | 최종 안정 버전 |
| `feature/add-quiz` | 퀴즈 추가 기능 개발 |
| `feature/save-load` | 저장/불러오기 기능 개발 |

---

## 📋 기본 제공 퀴즈 목록

| # | 주제 |
|---|------|
| 1 | 파이썬 주석 기호 |
| 2 | 리스트 마지막 요소 제거 메서드 |
| 3 | 정수형 타입 키워드 |
| 4 | 반환값이 없는 함수의 반환값 |
| 5 | 딕셔너리 키 목록 메서드 |
| 6 | 클래스 정의 키워드 |
| 7 | for 루프 range 사용법 |