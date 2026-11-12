# 🎯 Python 퀴즈 게임 개요

터미널에서 실행하는 파이썬 퀴즈 게임입니다.  
객관식 문제를 풀고 점수를 기록할 수 있어요.

---

## 📌 퀴즈 주제 선정 이유

이 게임의 퀴즈 주제는 **파이썬 기초 문법**입니다.
선정 이유는 다음과 같아요.

- 파이썬을 처음 배우는 사람도 쉽게 풀 수 있어요
- 문제를 풀면서 배운 내용을 복습할 수 있어요
- 정답과 오답을 바로 확인할 수 있어서 학습에 도움이 돼요

---

## ▶ 실행 방법

### 1. 저장소 다운로드

```bash
git clone https://github.com/내아이디/python-quiz-game.git
cd python-quiz-game
```

> ⚠️ `내아이디` 부분을 본인 GitHub 아이디로 바꿔주세요.

### 2. 게임 실행

```bash
python3 main.py
```

### 3. 메뉴 선택

```
=============================
       🎯 파이썬 퀴즈 게임
=============================
1. 퀴즈 시작
2. 점수 기록 보기
3. 도움말
4. 종료
=============================
번호를 입력하세요:
```

> 💡 1~4 숫자를 입력하고 Enter 를 누르세요.

---

## 🛠 기능 목록

| 번호 | 기능 | 설명 |
|------|------|------|
| 1 | 퀴즈 시작 | 랜덤으로 문제를 출제하고 정답을 확인 |
| 2 | 점수 기록 보기 | 지금까지 플레이한 점수 기록을 출력 |
| 3 | 도움말 | 게임 방법을 안내 |
| 4 | 종료 | 게임 종료 |

---

## 📁 파일 구조

```
python-quiz-game/
│
├── main.py          # 프로그램 시작점, 메뉴 화면
├── quiz.py          # Quiz 클래스 정의
│
├── quizzes.json     # 퀴즈 문제 데이터
├── state.json       # 점수 기록 데이터 (자동 생성)
│
├── .gitignore       # Git 제외 파일 목록
└── README.md        # 프로젝트 설명 (이 파일)
```

---

## 📂 데이터 파일 설명

### 📄 quizzes.json — 퀴즈 문제 데이터

퀴즈 문제, 선택지, 정답이 저장된 파일이에요.  
게임을 실행하면 이 파일에서 문제를 불러와요.

```json
{
  "quizzes": [
    {
      "question": "파이썬을 만든 사람은 누구인가요?",
      "choices": ["제임스 고슬링", "귀도 반 로섬", "리누스 토르발스", "빌 게이츠"],
      "answer": 2
    }
  ]
}
```

| 항목 | 설명 |
|------|------|
| `question` | 문제 텍스트 |
| `choices` | 선택지 4개 (리스트) |
| `answer` | 정답 번호 (1~4) |

---

### 📄 state.json — 점수 기록 데이터

게임을 플레이하면 **자동으로 생성**되는 파일이에요.  
플레이 횟수, 점수, 날짜가 기록돼요.

```json
{
  "records": [
    {
      "date": "2025-01-01",
      "score": 5,
      "total": 7
    },
    {
      "date": "2025-01-02",
      "score": 7,
      "total": 7
    }
  ]
}
```

| 항목 | 설명 |
|------|------|
| `date` | 플레이한 날짜 |
| `score` | 맞힌 문제 수 |
| `total` | 전체 문제 수 |

> 💡 `state.json` 은 처음 실행할 때 자동으로 만들어져요.  
> 직접 수정하지 않아도 돼요.

---

## 🛠 사용 기술

| 기술 | 용도 |
|------|------|
| Python 3 | 게임 전체 구현 |
| JSON | 퀴즈 데이터 및 점수 저장 |
| Git / GitHub | 버전 관리 및 코드 업로드 |

---

# 📚 Python 퀴즈 게임 — 학습 정리

---

# 1️⃣ Python 기초

## ✅ 변수
> 변수란 **데이터를 담는 상자**예요.

```python
name = "홍길동"   # 상자 이름: name, 담긴 값: "홍길동"
age  = 20         # 상자 이름: age,  담긴 값: 20
```

**왜 사용하나요?**
- 값을 저장해두고 나중에 다시 꺼내 쓸 수 있어요
- 같은 값을 여러 번 쓸 때 변수 하나만 바꾸면 돼요

---

## ✅ 자료형 5가지

| 자료형 | 의미 | 예시 |
|--------|------|------|
| `int` | 정수 | `10`, `-3`, `0` |
| `str` | 문자열 | `"안녕"`, `"hello"` |
| `bool` | 참/거짓 | `True`, `False` |
| `list` | 순서 있는 목록 | `[1, 2, 3]` |
| `dict` | 키-값 쌍 | `{"name": "홍길동"}` |

```python
age     = 20              # int
name    = "홍길동"         # str
is_pass = True            # bool
scores  = [90, 80, 70]    # list
person  = {"name": "홍길동", "age": 20}  # dict
```

---

## ✅ 조건문 if / elif / else
> 조건에 따라 **다른 동작**을 수행해요.

```python
score = 85

if score >= 90:
    print("A 학점")       # score가 90 이상일 때
elif score >= 80:
    print("B 학점")       # score가 80 이상일 때
else:
    print("C 학점 이하")  # 위 조건이 모두 아닐 때
```

| 키워드 | 역할 |
|--------|------|
| `if` | 첫 번째 조건 확인 |
| `elif` | 두 번째, 세 번째... 조건 확인 |
| `else` | 모든 조건이 아닐 때 실행 |

---

## ✅ 반복문 for vs while

```python
# for - 횟수가 정해진 반복
for i in range(3):
    print(i)       # 0, 1, 2 출력

# while - 조건이 참인 동안 반복
count = 0
while count < 3:
    print(count)   # 0, 1, 2 출력
    count += 1
```

| | `for` | `while` |
|--|-------|---------|
| 언제 사용? | 반복 횟수가 **정해진** 경우 | 조건이 **만족하는 동안** |
| 예시 | 퀴즈 7문제 출제 | 정답 입력할 때까지 반복 |

---

## ✅ 함수

```python
# 함수 정의
def add(a, b):       # a, b = 매개변수
    result = a + b
    return result    # 반환값

# 함수 호출
total = add(3, 5)
print(total)         # 8
```

| 용어 | 설명 |
|------|------|
| `def` | 함수를 만들 때 쓰는 키워드 |
| 매개변수 | 함수에 전달하는 값 (`a`, `b`) |
| `return` | 함수가 돌려주는 값 |

---

# 2️⃣ 클래스와 객체

## ✅ 클래스란?
> 클래스는 **설계도**, 객체는 **설계도로 만든 실제 물건**이에요.

```
클래스 = 붕어빵 틀
객체   = 붕어빵 틀로 만든 붕어빵
```

**왜 사용하나요?**
- 관련된 데이터와 기능을 **하나로 묶을 수 있어요**
- 같은 설계도로 **여러 객체**를 만들 수 있어요

---

## ✅ `__init__` 과 `self`

```python
class Quiz:
    def __init__(self, question, answer):
        #          ↑ 객체 만들 때 자동 실행
        self.question = question
        self.answer   = answer
        # ↑ self = 지금 만들어지는 이 객체 자신

# 객체 생성
q = Quiz("파이썬을 만든 사람은?", 2)
print(q.question)   # 파이썬을 만든 사람은?
```

| 용어 | 설명 |
|------|------|
| `__init__` | 객체를 만들 때 **자동으로 실행**되는 함수 |
| `self` | **지금 이 객체 자신**을 가리키는 말 |

---

## ✅ 속성과 메서드

```python
class Quiz:
    def __init__(self, question, answer):
        self.question = question   # 속성 (데이터)
        self.answer   = answer     # 속성 (데이터)

    def display(self):             # 메서드 (기능)
        print(self.question)

    def check(self, user_answer):  # 메서드 (기능)
        return self.answer == user_answer
```

| 용어 | 설명 | 예시 |
|------|------|------|
| 속성 | 객체가 가진 **데이터** | `self.question` |
| 메서드 | 객체가 가진 **기능** | `display()`, `check()` |

---

# 3️⃣ 파일 입출력

## ✅ 파일 열기 / 읽기 / 쓰기

```python
# 파일 쓰기
with open("test.txt", "w") as f:
    f.write("안녕하세요")

# 파일 읽기
with open("test.txt", "r") as f:
    content = f.read()
    print(content)   # 안녕하세요
```

| 모드 | 의미 |
|------|------|
| `"r"` | 읽기 (파일이 없으면 오류) |
| `"w"` | 쓰기 (파일이 없으면 새로 생성) |
| `"a"` | 이어쓰기 (기존 내용 유지) |

---

## ✅ JSON 이란?
> 데이터를 **텍스트로 저장**하는 형식이에요.  
> 파이썬의 딕셔너리/리스트와 생김새가 거의 같아요.

```python
import json

# 딕셔너리 → JSON 파일로 저장
data = {"name": "홍길동", "score": 5}

with open("state.json", "w") as f:
    json.dump(data, f)

# JSON 파일 → 딕셔너리로 불러오기
with open("state.json", "r") as f:
    loaded = json.load(f)
    print(loaded["score"])   # 5
```

| 함수 | 설명 |
|------|------|
| `json.dump()` | 딕셔너리 → JSON 파일로 **저장** |
| `json.load()` | JSON 파일 → 딕셔너리로 **불러오기** |

---

## ✅ try / except — 오류 처리

```python
try:
    with open("state.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    # 파일이 없을 때 실행
    data = {"records": []}
```

| 키워드 | 역할 |
|--------|------|
| `try` | 오류가 날 수 있는 코드 실행 |
| `except` | 오류가 났을 때 대신 실행 |

---

# 4️⃣ Git 기초

## ✅ Git 이란?
> **코드의 변경 기록을 저장**하는 도구예요.

**왜 필요한가요?**
- 실수로 코드를 망쳐도 **이전 상태로 되돌릴 수 있어요**
- 여러 사람이 **동시에 작업**할 수 있어요

---

## ✅ 핵심 명령어 7가지

```bash
# 1. init - 이 폴더를 Git으로 관리 시작
git init

# 2. add - 저장할 파일 선택
git add .

# 3. commit - 선택한 파일 저장 (스냅샷 찍기)
git commit -m "메시지"

# 4. push - GitHub에 올리기
git push

# 5. pull - GitHub에서 최신 내용 가져오기
git pull

# 6. checkout - 브랜치 이동 또는 파일 되돌리기
git checkout 브랜치이름

# 7. clone - GitHub 저장소를 내 컴퓨터로 복사
git clone 주소
```

| 명령어 | 한 줄 설명 |
|--------|-----------|
| `init` | Git 관리 시작 |
| `add` | 저장할 파일 선택 |
| `commit` | 변경사항 저장 |
| `push` | GitHub에 올리기 |
| `pull` | GitHub에서 가져오기 |
| `checkout` | 브랜치 이동 |
| `clone` | 저장소 복사 |

---

## ✅ 브랜치 생성과 병합

```bash
# 브랜치 생성 + 이동
git checkout -b feature/quiz

# 작업 후 커밋
git add .
git commit -m "feat: 퀴즈 기능 추가"

# main 브랜치로 이동
git checkout main

# 병합
git merge feature/quiz
```

> 💡 브랜치는 **작업용 복사본**이에요.  
> 원본(main)을 건드리지 않고 새 기능을 만들 수 있어요.

---

## ✅ clone 과 pull

```bash
# clone - 처음 저장소를 내 컴퓨터로 가져올 때
git clone https://github.com/아이디/python-quiz-game.git

# pull - 이미 clone한 저장소의 최신 내용을 가져올 때
git pull
```

| | `clone` | `pull` |
|--|---------|--------|
| 언제? | **처음** 가져올 때 | **이미 있는** 저장소 업데이트 |

---


---

### 2. quiz.py 코드 작성

```python
class Quiz:
    """퀴즈 하나를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question   # 문제
        self.choices  = choices    # 선택지 리스트
        self.answer   = answer     # 정답 번호 (1~4)

    def display(self):
        """문제와 선택지를 출력"""
        print(f"\n📝 {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")

    def check_answer(self, user_answer):
        """정답이면 True, 오답이면 False 반환"""
        return self.answer == user_answer
```

---

## 코드 설명

| 코드 | 설명 |
|------|------|
| `class Quiz:` | 퀴즈를 담는 설계도(클래스) |
| `__init__()` | 객체를 만들 때 자동으로 실행되는 함수 |
| `self.question` | 이 객체의 문제를 저장 |
| `self.choices` | 이 객체의 선택지를 저장 |
| `self.answer` | 이 객체의 정답 번호를 저장 |
| `display()` | 문제와 선택지를 출력하는 함수 |
| `check_answer()` | 정답 여부를 확인하는 함수 |
| `enumerate(list, start=1)` | 리스트를 1번부터 번호 붙여 순회 |

---

### 3. quizzes.json 파일 만들기

```bash
touch quizzes.json
```

---

### 4. quizzes.json 데이터 작성

```json
{
  "quizzes": [
    {
      "question": "파이썬(Python)을 만든 사람은 누구인가요?",
      "choices": ["제임스 고슬링", "귀도 반 로섬", "리누스 토르발스", "빌 게이츠"],
      "answer": 2
    },
    {
      "question": "다음 중 파이썬의 리스트(list)를 만드는 올바른 방법은?",
      "choices": ["list = (1, 2, 3)", "list = {1, 2, 3}", "list = [1, 2, 3]", "list = <1, 2, 3>"],
      "answer": 3
    },
    {
      "question": "파이썬에서 주석을 작성할 때 사용하는 기호는?",
      "choices": ["//", "/* */", "--", "#"],
      "answer": 4
    },
    {
      "question": "파이썬에서 아무것도 없음을 나타내는 값은?",
      "choices": ["null", "undefined", "None", "empty"],
      "answer": 3
    },
    {
      "question": "다음 중 파이썬의 반복문이 아닌 것은?",
      "choices": ["for", "while", "loop", "for ~ in"],
      "answer": 3
    },
    {
      "question": "파이썬에서 함수를 정의할 때 사용하는 키워드는?",
      "choices": ["function", "func", "def", "define"],
      "answer": 3
    },
    {
      "question": "파이썬 딕셔너리(dictionary)를 만드는 올바른 방법은?",
      "choices": ["[key: value]", "{key: value}", "(key: value)", "<key: value>"],
      "answer": 2
    }
  ]
}
```

> 💡 **JSON 이란?**  
> 데이터를 저장하는 텍스트 형식이에요.  
> `{ }` 는 딕셔너리, `[ ]` 는 리스트와 같아요.

---

## 동작 확인

터미널에서 아래 명령어로 테스트해요.

```bash
python3 -c "
from quiz import Quiz
q = Quiz('파이썬을 만든 사람은?', ['고슬링', '귀도', '리누스', '빌게이츠'], 2)
q.display()
print('정답(2):', q.check_answer(2))
print('오답(1):', q.check_answer(1))
"
```

아래처럼 나오면 성공이에요 ✅
```
📝 파이썬을 만든 사람은?
  1. 고슬링
  2. 귀도
  3. 리누스
  4. 빌게이츠
정답(2): True
오답(1): False
```

---

## Git 커밋

```bash
git add quiz.py quizzes.json Step04.md
git commit -m "feat: Quiz 클래스 및 퀴즈 데이터 추가"
git push
```

---

프로젝트 루트/state.json
📋 역할
퀴즈 데이터(문제·선택지·정답)를 영구 저장합니다.
최고 점수를 저장하여 프로그램 재실행 후에도 유지합니다.
파일이 없으면 기본 퀴즈 데이터로 자동 초기화됩니다.
파일이 손상된 경우 안내 메시지 출력 후 기본 데이터로 복구됩니다.

---

# 📋 전체 학습 목표 체크리스트

### Python 기초
- [ ] 변수가 무엇이고 왜 사용하는지 설명할 수 있다
- [ ] int, str, bool, list, dict 의 차이를 설명할 수 있다
- [ ] if/elif/else 로 조건에 따라 다른 동작을 수행할 수 있다
- [ ] for 와 while 의 차이를 설명하고 적절히 선택할 수 있다
- [ ] 함수를 정의하고 매개변수와 반환값을 활용할 수 있다

### 클래스와 객체
- [ ] 클래스가 무엇이고 왜 사용하는지 설명할 수 있다
- [ ] `__init__` 메서드와 `self` 의 역할을 설명할 수 있다
- [ ] 속성과 메서드를 정의하고 활용할 수 있다

### 파일 입출력
- [ ] 파일을 열고 읽고 쓰는 기본 과정을 설명할 수 있다
- [ ] JSON 형식이 무엇이고 왜 사용하는지 설명할 수 있다
- [ ] try/except 로 오류를 처리할 수 있다

### Git 기초
- [ ] Git 이 무엇이고 왜 필요한지 설명할 수 있다
- [ ] init, add, commit, push, pull, checkout, clone 을 설명할 수 있다
- [ ] 브랜치를 생성하고 병합할 수 있다
- [ ] clone 과 pull 의 차이를 설명할 수 있다

---

# 🎯 Python Quiz Game

제출 전 아래 항목을 모두 확인하세요!

---

## 📋 제출 전 아래 항목을 모두 확인하세요!

## [ ] 퀴즈가 10문제 이상 있다
## [ ] 문제가 랜덤으로 나온다
## [ ] 점수가 저장된다 (파일로)
## [ ] 클래스를 사용했다
## [ ] GitHub에 올라가 있다
## [ ] README.md 파일이 있다

---

## ✅ 최종 제출 점검

### 💚 제출 전 최종 체크리스트

#### 📌 코드 확인

- [ ] `python main.py` 로 오류 없이 실행된다
- [ ] 퀴즈 문제가 10개 이상 있다
- [ ] 문제가 랜덤으로 출력된다
- [ ] 정답/오답이 올바르게 표시된다
- [ ] 점수가 `scores.json` 에 저장된다
- [ ] 점수 보기 메뉴가 잘 동작한다
- [ ] `Quiz` 클래스를 사용했다

#### 📌 파일 구조 확인

- [ ] `main.py` 가 있다
- [ ] `quiz.py` 가 있다
- [ ] `data.py` 가 있다
- [ ] `storage.py` 가 있다
- [ ] `README.md` 가 있다

#### 📌 Git 확인

- [ ] GitHub 저장소가 만들어져 있다
- [ ] 커밋이 10개 이상 있다
- [ ] 브랜치를 나눠서 작업했다
- [ ] 모든 브랜치가 `main` 에 합쳐졌다
- [ ] 커밋 메시지가 규칙에 맞게 작성됐다