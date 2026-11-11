

# Step 01 - GitHub 저장소 만들기

## 목표
GitHub에 저장소를 만들고 내 컴퓨터와 연결한다.

---

## 순서

### 1. GitHub에서 저장소 만들기
1. [github.com](https://github.com) 로그인
2. 우측 상단 `+` 버튼 → `New repository` 클릭
3. 아래처럼 입력 후 `Create repository` 클릭

| 항목 | 입력값 |
|------|--------|
| Repository name | `python-quiz-game` |
| Description | `터미널 퀴즈 게임` |
| Public / Private | Public |
| README 추가 | ❌ 체크 안 함 |

---

### 2. 내 컴퓨터에 폴더 만들기

```bash
mkdir python-quiz-game
cd python-quiz-game
git init
```

> 💡 `git init` 은 이 폴더를 Git이 관리하도록 설정하는 명령어예요.

---

### 3. GitHub 저장소와 연결하기

```bash
git remote add origin https://github.com/내아이디/python-quiz-game.git
```

> ⚠️ `내아이디` 부분을 본인 GitHub 아이디로 바꿔주세요.

---

### 4. 연결 확인

```bash
git remote -v
```

아래처럼 나오면 성공이에요 ✅
```
origin  https://github.com/내아이디/python-quiz-game.git (fetch)
origin  https://github.com/내아이디/python-quiz-game.git (push)
```

---

## 체크리스트
- [ ] GitHub에 저장소 생성
- [ ] 로컬 폴더 생성 및 `git init`
- [ ] `git remote add origin` 으로 연결
- [ ] `git remote -v` 로 연결 확인



# Step 02 - 첫 파일 만들고 GitHub에 올리기

## 목표
`.gitignore` 와 `README.md` 를 만들고 GitHub에 첫 커밋을 올린다.

---

## 순서

### 1. .gitignore 파일 만들기

```bash
touch .gitignore
```

`.gitignore` 파일을 열고 아래 내용을 붙여넣기 하세요.

```
__pycache__/
*.pyc
.DS_Store
.env
```

> 💡 `.gitignore` 는 GitHub에 올리지 않을 파일을 지정하는 파일이에요.  
> 위 4줄은 파이썬 프로젝트에서 올릴 필요 없는 파일들이에요.

---

### 2. README.md 파일 만들기

```bash
touch README.md
```

`README.md` 파일을 열고 아래 내용을 붙여넣기 하세요.

```markdown
# 🎯 Python 퀴즈 게임

터미널에서 실행하는 파이썬 퀴즈 게임입니다.

## 실행 방법
python3 main.py

## 기술 스택
- Python 3
- JSON
```

> 💡 `README.md` 는 프로젝트를 소개하는 파일이에요.  
> GitHub 저장소에 들어가면 첫 화면에 보여요.

---

### 3. GitHub에 올리기

아래 명령어를 **순서대로** 입력하세요.

```bash
git add .
```
> 💡 변경된 파일을 전부 선택해요.

```bash
git commit -m "init: 프로젝트 초기 설정"
```
> 💡 선택한 파일을 저장해요. `""` 안에는 무엇을 했는지 적어요.

```bash
git push -u origin main
```
> 💡 저장한 내용을 GitHub에 올려요.

---

### 4. 확인
GitHub 저장소 페이지를 새로고침 하면  
`.gitignore` 와 `README.md` 파일이 보여야 해요 ✅

---

## 체크리스트
- [ ] `.gitignore` 생성 및 내용 작성
- [ ] `README.md` 생성 및 내용 작성
- [ ] `git add .` → `git commit` → `git push`
- [ ] GitHub에서 파일 업로드 확인

# Step 03 - 메뉴 화면 만들기

## 목표
`main.py` 를 만들고 게임의 메뉴 화면을 구현한다.

---

## 순서

### 1. main.py 파일 만들기

```bash
touch main.py
```

---

### 2. main.py 코드 작성

```python
def show_menu():
    """메뉴를 출력하는 함수"""
    print("\n=============================")
    print("       🎯 파이썬 퀴즈 게임")
    print("=============================")
    print("1. 퀴즈 시작")
    print("2. 점수 기록 보기")
    print("3. 도움말")
    print("4. 종료")
    print("=============================")


def main():
    """프로그램 시작점"""
    while True:                          # 계속 반복
        show_menu()                      # 메뉴 출력

        choice = input("번호를 입력하세요: ").strip()  # 입력 받기

        if choice == "1":
            print("\n▶ 퀴즈 시작! (다음 단계에서 구현)")
        elif choice == "2":
            print("\n▶ 점수 기록 (다음 단계에서 구현)")
        elif choice == "3":
            print("\n▶ 도움말 (다음 단계에서 구현)")
        elif choice == "4":
            print("\n👋 게임을 종료합니다.")
            break                        # 반복 종료
        else:
            print("\n⚠️  1~4 중에서 입력해주세요.")  # 잘못된 입력 처리


if __name__ == "__main__":
    main()
```

---

## 코드 설명

| 코드 | 설명 |
|------|------|
| `def show_menu():` | 메뉴를 출력하는 함수 |
| `def main():` | 프로그램이 시작되는 함수 |
| `while True:` | 종료할 때까지 계속 반복 |
| `input()` | 키보드 입력을 받음 |
| `.strip()` | 입력값 앞뒤 공백 제거 |
| `break` | 반복문 종료 |
| `if __name__ == "__main__":` | 이 파일을 직접 실행할 때만 `main()` 호출 |

---

## 실행 방법

```bash
python3 main.py
```

실행하면 아래처럼 보여야 해요 ✅
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

---

## Git 커밋

```bash
git add main.py
git commit -m "feat: 메뉴 화면 구현"
git push
```

---

## 체크리스트
- [ ] `main.py` 생성 및 코드 작성
- [ ] `python3 main.py` 로 실행 확인
- [ ] 1~4 입력 시 각각 다른 메시지 출력 확인
- [ ] 4 입력 시 종료 확인
- [ ] `git add` → `commit` → `push`

# Step 04 - Quiz 클래스 + 퀴즈 데이터 만들기

## 목표
퀴즈를 담는 `Quiz` 클래스를 만들고, 퀴즈 데이터를 JSON 파일에 저장한다.

---

## 순서

### 1. quiz.py 파일 만들기

```bash
touch quiz.py
```

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

## 체크리스트
- [ ] `quiz.py` 생성 및 코드 작성
- [ ] `quizzes.json` 생성 및 데이터 작성
- [ ] 동작 확인 테스트 통과
- [ ] `git add` → `commit` → `push`