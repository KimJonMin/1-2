# 🎮 나만의 퀴즈 게임 만들기 — 완전 초보자 가이드

> **문법을 *아는 것*에서 → 프로그램을 *만드는 것*으로**
> 처음부터 끝까지, 혼자서, 완성까지.

## 📌 목차

- [🎯 미션 소개](#-미션-소개)
- [🛠️ 준비하기](#️-준비하기)
- [🗺️ 전체 로드맵](#️-전체-로드맵)
- [STEP 1 · 기본 버전 만들기](#step-1--기본-버전-만들기)
- [STEP 2 · 클래스로 구조화하기](#step-2--클래스로-구조화하기)
- [STEP 3 · JSON으로 데이터 저장하기](#step-3--json으로-데이터-저장하기)
- [STEP 4 · Git으로 이력 관리하기](#step-4--git으로-이력-관리하기)
- [STEP 5 · GitHub에 공개하기](#step-5--github에-공개하기)
- [📚 핵심 개념 카드](#-핵심-개념-카드)
- [✅ 완료 체크리스트](#-완료-체크리스트)

---

## 🎯 미션 소개

### 왜 이 미션인가요?

책으로 배운 수영 이론만으로는 절대 수영할 수 없습니다.
직접 물에 들어가야 합니다.

- if문이 뭔지 안다 → if문으로 정답 판별을 만든다
- 변수가 뭔지 안다 → 변수로 점수를 직접 관리한다
- 클래스가 뭔지 안다 → 클래스로 퀴즈를 직접 설계한다


### 무엇을 만드나요?

터미널에서 동작하는 **나만의 퀴즈 게임** 🎮
```
╔══════════════════════════════════╗
║       🎮 나만의 퀴즈 게임!       ║
╠══════════════════════════════════╣
║  🏅 역대 점수 순위               ║
║     🥇 홍길동 — 3점              ║
║     🥈 김철수 — 2점              ║
╠══════════════════════════════════╣
║  이름을 입력하세요: 이영희        ║
║                                  ║
║  Q1. 파이썬을 만든 사람은?       ║
║    1. 빌 게이츠                  ║
║    2. 귀도 반 로섬               ║
║    3. 스티브 잡스                ║
║  정답 번호 입력: 2               ║
║  ✅ 정답입니다!                  ║
║                                  ║
║  🏆 최종 점수: 3 / 3             ║
║  💾 점수가 저장되었습니다!       ║
╚══════════════════════════════════╝
```

### 이 미션으로 얻는 것
 "docs: README 내용 추가" 입력
| 영역 | 배우는 것 | 결과물 |
|:---:|:---|:---:|
| 🐍 Python | 입출력 · 리스트 · 딕셔너리 · 클래스 | `.py` 파일 |
| 💾 데이터 | JSON 파일 저장 · 불러오기 | `scores.json` |
| 🌿 Git | 커밋 · 브랜치 · 병합 | 커밋 이력 |
| 🌐 GitHub | 공개 저장소 · README | 포트폴리오 |

---

## 🛠️ 준비하기

### Python 설치 확인

```bash
python --version
# Python 3.11.0  ← 이렇게 나오면 OK!
설치가 안 되어 있다면 → https://www.python.org/downloads/
⚠️ 설치 시 Add Python to PATH 체크박스를 반드시 체크하세요!

Git 설치 확인

git --version
# git version 2.43.0  ← 이렇게 나오면 OK!
설치가 안 되어 있다면 → https://git-scm.com/downloads

프로젝트 폴더 만들기

mkdir quiz-game   # 폴더 생성
cd quiz-game      # 폴더 안으로 이동
🗺️ 전체 로드맵

┌─────────────────────────────────────────────────────┐
│                                                     │
│  STEP 1          STEP 2          STEP 3             │
│  기본 버전   →   클래스 버전  →  JSON 저장          │
│  quiz.py         quiz_oop.py     quiz_final.py      │
│                                                     │
│                      ↓                              │
│                                                     │
│  STEP 4                    STEP 5                   │
│  Git 커밋 & 브랜치    →    GitHub 공개 🌐           │
│                                                     │
└─────────────────────────────────────────────────────┘
추천 일정
일차	목표	완료 기준
Day 1	환경 설정 + STEP 1	python quiz.py 실행 성공
Day 2	STEP 2	클래스 3개 작성 완료
Day 3	STEP 3	scores.json 생성 확인
Day 4	STEP 4 + 5	GitHub 저장소 공개 완료
STEP 1 · 기본 버전 만들기
🎯 목표 : Python 기본 문법으로 퀴즈 게임이 동작하게 만든다

파일 구조

quiz-game/
└── quiz.py   ← 지금 만들 파일
코드
python

# quiz.py ─ 퀴즈 게임 기본 버전
# 사용 문법: 리스트, 딕셔너리, for문, if문, input/print

# ① 퀴즈 목록
questions = [
    {
        "question": "파이썬을 만든 사람은?",
        "options": ["빌 게이츠", "귀도 반 로섬", "스티브 잡스"],
        "answer": "2"
    },
    {
        "question": "파이썬 파일의 확장자는?",
        "options": [".java", ".py", ".js"],
        "answer": "2"
    },
    {
        "question": "print()는 무엇을 하는 함수인가?",
        "options": ["입력받기", "계산하기", "출력하기"],
        "answer": "3"
    }
]

# ② 점수 변수
score = 0

# ③ 게임 시작
print("=" * 40)
print("  🎮 나만의 퀴즈 게임!")
print("=" * 40)

name = input("이름을 입력하세요: ")
print(f"\n안녕하세요, {name}님! 퀴즈를 시작합니다.\n")

# ④ 문제 반복 출제
for i, q in enumerate(questions):
    print(f"Q{i+1}. {q['question']}")
    for j, option in enumerate(q['options']):
        print(f"  {j+1}. {option}")

    user_answer = input("정답 번호 입력: ")

    if user_answer == q['answer']:
        print("✅ 정답입니다!\n")
        score += 1
    else:
        print(f"❌ 오답! 정답은 {q['answer']}번이에요.\n")

# ⑤ 최종 점수
print("=" * 40)
print(f"🏆 {name}님의 최종 점수: {score} / {len(questions)}")
print("=" * 40)
실행

python quiz.py
✅ STEP 1 완료 기준 : 터미널에서 퀴즈가 출제되고 점수가 출력된다

STEP 2 · 클래스로 구조화하기
🎯 목표 : 코드를 역할별로 나눠 읽기 쉽고 고치기 쉽게 만든다

클래스가 왜 필요한가요?
code

# 클래스 없이 ─ 모든 것이 한 곳에 뒤섞임
score = 0
name = ""
questions = [...]       # 😵 길어질수록 관리가 어렵다

# 클래스 있으면 ─ 역할별로 깔끔하게 분리
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│    Quiz     │  │   Player    │  │    Game     │
│─────────────│  │─────────────│  │─────────────│
│ 문제 출제   │  │ 이름 관리   │  │ 전체 흐름   │
│ 정답 확인   │  │ 점수 관리   │  │ 조율        │
└─────────────┘  └─────────────┘  └─────────────┘
코드

# quiz_oop.py ─ 클래스(객체 지향) 버전

# ══════════════════════════════
# Quiz 클래스 ─ 문제 하나를 표현
# ══════════════════════════════
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question   # 문제
        self.options  = options    # 보기 목록
        self.answer   = answer     # 정답 번호

    def show(self, number):
        """문제와 보기를 출력"""
        print(f"\nQ{number}. {self.question}")
        for i, option in enumerate(self.options):
            print(f"  {i+1}. {option}")

    def check(self, user_input):
        """정답이면 True, 오답이면 False"""
        return user_input == self.answer


# ══════════════════════════════
# Player 클래스 ─ 플레이어 정보 관리
# ══════════════════════════════
class Player:
    def __init__(self, name):
        self.name  = name
        self.score = 0

    def add_score(self):
        """점수 1점 추가"""
        self.score += 1

    def show_result(self, total):
        """최종 결과 출력"""
        print("\n" + "=" * 40)
        print(f"🏆 {self.name}님의 최종 점수: {self.score} / {total}")
        print("=" * 40)


# ══════════════════════════════
# Game 클래스 ─ 전체 흐름 관리
# ══════════════════════════════
class Game:
    def __init__(self):
        self.quizzes = [
            Quiz("파이썬을 만든 사람은?",
                 ["빌 게이츠", "귀도 반 로섬", "스티브 잡스"], "2"),
            Quiz("파이썬 파일의 확장자는?",
                 [".java", ".py", ".js"], "2"),
            Quiz("print()는 무엇을 하는 함수인가?",
                 ["입력받기", "계산하기", "출력하기"], "3"),
        ]

    def start(self):
        print("=" * 40)
        print("  🎮 나만의 퀴즈 게임!")
        print("=" * 40)

        name   = input("이름을 입력하세요: ")
        player = Player(name)
        print(f"\n안녕하세요, {player.name}님!\n")

        for i, quiz in enumerate(self.quizzes):
            quiz.show(i + 1)
            answer = input("정답 번호 입력: ")

            if quiz.check(answer):
                print("✅ 정답입니다!")
                player.add_score()
            else:
                print(f"❌ 오답! 정답은 {quiz.answer}번이에요.")

        player.show_result(len(self.quizzes))


# ══════════════════════════════
# 실행
# ══════════════════════════════
if __name__ == "__main__":
    game = Game()
    game.start()
실행

python quiz_oop.py
✅ STEP 2 완료 기준 : Quiz · Player · Game 클래스 3개가 각자 역할을 수행한다

STEP 3 · JSON으로 데이터 저장하기
🎯 목표 : 프로그램을 꺼도 점수가 유지되

도록 파일에 저장한다

### JSON이 왜 필요한가요?
JSON 없이 JSON 있으면
────────────────────── ──────────────────────
프로그램 실행 → 점수 생성 프로그램 실행 → 점수 생성
프로그램 종료 → 점수 사라짐 프로그램 종료 → scores.json 에 저장
다시 실행 → 점수 없음 다시 실행 → scores.json 에서 불러옴


### scores.json 파일 구조

```json
{
  "홍길동": 3,
  "김철수": 2,
  "이영희": 3
}
💡 JSON = 사람도 읽기 쉽고, 프로그램도 읽기 쉬운 데이터 저장 형식

파일 구조

quiz-game/
├── quiz.py
├── quiz_oop.py
├── quiz_final.py    ← 지금 만들 파일
└── scores.json      ← 자동으로 생성됨
코드
python

# quiz_final.py ─ 최종 완성 버전 (JSON 저장 포함)

import json
import os

# ══════════════════════════════
# Quiz 클래스
# ══════════════════════════════
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options  = options
        self.answer   = answer

    def show(self, number):
        print(f"\nQ{number}. {self.question}")
        for i, option in enumerate(self.options):
            print(f"  {i+1}. {option}")

    def check(self, user_input):
        return user_input == self.answer


# ══════════════════════════════
# Player 클래스
# ══════════════════════════════
class Player:
    def __init__(self, name):
        self.name  = name
        self.score = 0

    def add_score(self):
        self.score += 1

    def show_result(self, total):
        print("\n" + "=" * 40)
        print(f"🏆 {self.name}님의 최종 점수: {self.score} / {total}")
        print("=" * 40)


# ══════════════════════════════
# ScoreManager 클래스 ─ JSON 저장/불러오기
# ══════════════════════════════
class ScoreManager:
    def __init__(self, filename="scores.json"):
        self.filename = filename

    def load(self):
        """파일이 없으면 빈 딕셔너리 반환"""
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, name, score):
        """점수를 파일에 저장"""
        scores = self.load()
        scores[name] = score
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
        print("💾 점수가 저장되었습니다!")

    def show_ranking(self):
        """역대 점수 순위 출력"""
        scores = self.load()

        if not scores:
            print("📭 아직 저장된 점수가 없습니다.")
            return

        # 점수 높은 순 정렬
        sorted_scores = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        medals = ["🥇", "🥈", "🥉"]

        print("\n" + "=" * 40)
        print("  🏅 역대 점수 순위")
        print("=" * 40)
        for rank, (name, score) in enumerate(sorted_scores, start=1):
            icon = medals[rank - 1] if rank <= 3 else f"  {rank}위"
            print(f"  {icon}  {name} — {score}점")
        print("=" * 40)


# ══════════════════════════════
# Game 클래스 ─ 전체 흐름 관리
# ══════════════════════════════
class Game:
    def __init__(self):
        self.quizzes = [
            Quiz("파이썬을 만든 사람은?",
                 ["빌 게이츠", "귀도 반 로섬", "스티브 잡스"], "2"),
            Quiz("파이썬 파일의 확장자는?",
                 [".java", ".py", ".js"], "2"),
            Quiz("print()는 무엇을 하는 함수인가?",
                 ["입력받기", "계산하기", "출력하기"], "3"),
        ]
        self.score_manager = ScoreManager()

    def start(self):
        print("=" * 40)
        print("  🎮 나만의 퀴즈 게임!")
        print("=" * 40)

        # 시작 전 역대 순위 표시
        self.score_manager.show_ranking()

        name   = input("\n이름을 입력하세요: ")
        player = Player(name)
        print(f"\n안녕하세요, {player.name}님! 퀴즈를 시작합니다.\n")

        # 문제 출제
        for i, quiz in enumerate(self.quizzes):
            quiz.show(i + 1)
            answer = input("정답 번호 입력: ")

            if quiz.check(answer):
                print("✅ 정답입니다!")
                player.add_score()
            else:
                print(f"❌ 오답! 정답은 {quiz.answer}번이에요.")

        # 결과 출력 & 저장
        player.show_result(len(self.quizzes))
        self.score_manager.save(player.name, player.score)

        # 저장 후 최신 순위 표시
        self.score_manager.show_ranking()


# ══════════════════════════════
# 실행
# ══════════════════════════════
if __name__ == "__main__":
    game = Game()
    game.start()
실행 & 확인


# 1. 게임 실행
python quiz_final.py

# 2. scores.json 생성 확인
cat scores.json        # Mac / Linux
type scores.json       # Windows
실행 결과 예시

========================================
  🎮 나만의 퀴즈 게임!
========================================
📭 아직 저장된 점수가 없습니다.

이름을 입력하세요: 홍길동

안녕하세요, 홍길동님! 퀴즈를 시작합니다.

Q1. 파이썬을 만든 사람은?
  1. 빌 게이츠
  2. 귀도 반 로섬
  3. 스티브 잡스
정답 번호 입력: 2
✅ 정답입니다!

  ... (이하 생략)

========================================
🏆 홍길동님의 최종 점수: 3 / 3
========================================
💾 점수가 저장되었습니다!

========================================
  🏅 역대 점수 순위
========================================
  🥇  홍길동 — 3점
========================================
✅ STEP 3 완료 기준 : 프로그램 종료 후 재실행해도 이전 점수가 순위에 표시된다

STEP 4 · Git으로 이력 관리하기
🎯 목표 : 기능 단위로 변경 이력을 기록하고 브랜치를 경험한다

Git이 왜 필요한가요?

Git 없이                       Git 있으면
────────────────────────       ────────────────────────
quiz_최종.py                   quiz_final.py 파일 하나로
quiz_최종2.py                  모든 변경 이력을
quiz_진짜최종.py       →       깔끔하게 관리한다 ✅
quiz_진짜진짜최종.py
Git 핵심 흐름

[내가 수정]  →  git add  →  [저장 대기]  →  git commit  →  [로컬 저장소]
                "이거 저장"                   "이력 + 메모"
초기 설정 (처음 한 번만)

# Git 시작
git init

# 내 정보 등록
git config --global user.name  "내이름"
git config --global user.email "내이메일@example.com"

# 불필요한 파일 제외 목록 생성
echo "__pycache__/"  > .gitignore
echo "*.pyc"        >> .gitignore
echo "scores.json"  >> .gitignore   # 점수 파일은 개인 데이터라 제외
기능 단위로 커밋하기

# ── STEP 1 완료 후 ─────────────────────────
git add quiz.py
git commit -m "feat: 퀴즈 게임 기본 버전 구현"

# ── STEP 2 완료 후 ─────────────────────────
git add quiz_oop.py
git commit -m "refactor: 클래스 기반으로 코드 구조화"

# ── STEP 3 완료 후 ─────────────────────────
git add quiz_final.py
git commit -m "feat: JSON 점수 저장·불러오기 기능 추가"
좋은 커밋 메시지 규칙

feat:      새로운 기능 추가
fix:       버그 수정
refactor:  기능 변경 없이 코드 구조 개선
docs:      문서(README 등) 수정
chore:     설정 파일 변경

✅ 좋은 예   feat: 점수 순위 출력 기능 추가
✅ 좋은 예   fix: 정답 비교 오류 수정
❌ 나쁜 예   수정함
❌ 나쁜 예   코드 고침
브랜치 사용해보기

# 1. 새 브랜치 만들고 이동
git checkout -b feature/score-ranking

# 2. 이 브랜치에서 작업 후 커밋
git add .
git commit -m "feat: 점수 순위 기능 구현"

# 3. main 으로 돌아오기
git checkout main

# 4. 작업 내용을 main 에 합치기
git merge feature/score-ranking

# 5. 다 쓴 브랜치 삭제
git branch -d feature/score-ranking
브랜치 흐름 시각화

main   ──●──────────────────────────●── (merge)
          \                        /
feature    ●── 작업 ── 커밋 ── 커밋
상태 확인 명령어

git status          # 변경된 파일 목록 확인
git log --oneline   # 커밋 이력 한 줄로 보기
git diff            # 변경 내용 상세 비교
✅ STEP 4 완료 기준 : git log --oneline 실행 시 커밋 3개 이상 확인된다

STEP 5 · GitHub에 공개하기
🎯 목표 : 내 코드를 인터넷에 공개하고 첫 포트폴리오를 완성한다

GitHub 저장소 연결 & 업로드

# 1. github.com → New Repository
#    이름: quiz-game / 공개(Public) 설정

# 2. 로컬 저장소와 연결
git remote add origin https://github.com/내아이디/quiz-game.git

# 3. 처음 업로드
git push -u origin main

# 4. 이후 변경사항 업로드
git push
README.md 작성하기
GitHub 저장소 첫 화면에 자동으로 표시되는 프로젝트 소개 파일입니다.


# 🎮 나만의 퀴즈 게임

터미널에서 동작하는 Python 퀴즈 게임입니다.

## 실행 방법

python quiz_final.py

## 사용 기술

- Python 3.11
- JSON 파일 저장
- 객체 지향 프로그래밍 (OOP)

## 기능

- ✅ 퀴즈 출제 및 정답 확인
- ✅ 점수 자동 저장 (scores.json)
- ✅ 역대 점수 순위 출력

git add README.md
git commit -m "docs: README 작성"
git push
✅ STEP 5 완료 기준 : GitHub 저장소 URL이 생기고 코드가 공개된다

📚 핵심 개념 카드
🐍 Python

# 리스트 ─ 여러 값을 순서대로 저장
questions = ["문제1", "문제2", "문제3"]

# 딕셔너리 ─ 이름표(key)와 값(value)을 쌍으로 저장
quiz = {
    "question": "파이썬을 만든 사람은?",
    "answer"  : "2"
}

# 클래스 ─ 데이터와 기능을 하나로 묶은 설계도
class Quiz:
    def __init__(self, question, answer):   # 초기화
        self.question = question
        self.answer   = answer

    def check(self, user_input):            # 기능
        return user_input == self.answer

# 객체 ─ 클래스로 만든 실제 물건
my_quiz = Quiz("파이썬을 만든 사람은?", "2")
💾 JSON

import json

# Python → JSON 파

일로 저장
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump({"홍길동": 3}, f, ensure_ascii=False, indent=2)

# JSON 파일 → Python으로 불러오기
with open("scores.json", "r", encoding="utf-8") as f:
    data = json.load(f)
🌿 Git

git init                     # Git 시작
git add 파일명               # 저장할 파일 선택
git commit -m "메시지"       # 변경 이력 저장
git push                     # GitHub에 올리기
git log --oneline            # 이력 확인
git checkout -b 브랜치명     # 새 브랜치 생성 & 이동
git merge 브랜치명           # 브랜치 병합
✅ 완료 체크리스트
아래 항목을 하나씩 체크하며 진행하세요!

STEP 1 · 기본 버전

□ quiz.py 파일을 직접 작성했다
□ python quiz.py 실행에 성공했다
□ 퀴즈가 출제되고 점수가 출력된다
STEP 2 · 클래스 버전

□ Quiz 클래스를 작성했다
□ Player 클래스를 작성했다
□ Game 클래스를 작성했다
□ python quiz_oop.py 실행에 성공했다
STEP 3 · JSON 저장

□ ScoreManager 클래스를 작성했다
□ python quiz_final.py 실행에 성공했다
□ scores.json 파일이 생성되었다
□ 프로그램 재실행 시 이전 점수가 불러와진다
□ 역대 순위가 올바르게 출력된다
STEP 4 · Git 관리

□ git init 으로 저장소를 초기화했다
□ .gitignore 파일을 만들었다
□ 커밋이 3개 이상 존재한다
□ git log --oneline 으로 이력을 확인했다
□ 브랜치를 만들고 merge 해봤다
STEP 5 · GitHub 공개

□ GitHub 저장소를 생성했다
□ git push 로 코드를 업로드했다
□ README.md 를 작성했다
□ MISSION_GUIDE.md 를 업로드했다
□ GitHub URL 이 생겼다  →  https://github.com/내아이디/quiz-game
🗂️ 최종 폴더 구조

quiz-game/
│
├── 📄 quiz.py              ← STEP 1 : 기본 버전
├── 📄 quiz_oop.py          ← STEP 2 : 클래스 버전
├── 📄 quiz_final.py        ← STEP 3 : 최종 완성 버전
│
├── 📊 scores.json          ← 자동 생성 (점수 저장)
│
├── 🚫 .gitignore           ← Git 제외 목록
├── 📖 README.md            ← 프로젝트 소개
└── 📋 MISSION_GUIDE.md     ← 이 가이드 문서
❓ 개념 이해 확인 퀴즈
미션을 마쳤다면 아래 질문에 답해보세요!

Q1. 클래스와 객체의 차이를 한 문장으로 설명하면?
    힌트 → 설계도 vs 실제 물건

Q2. JSON 파일을 사용하는 이유는?
    힌트 → 프로그램을 꺼도 데이터가...

Q3. git commit 과 git push 의 차이는?
    힌트 → 내 컴퓨터 저장 vs 인터넷 저장

Q4. 브랜치(branch)를 사용하는 이유는?
    힌트 → main 코드를 건드리지 않고...
💡 정답 확인 (클릭)
🗓️ 추천 진행 일정

Day 1 ── 환경 설정 & STEP 1
  ├── Python, Git 설치 확인
  ├── quiz.py 작성
  └── 터미널에서 실행 성공 ✅

Day 2 ── STEP 2
  ├── 클래스(Class) 개념 이해
  ├── Quiz, Player, Game 클래스 작성
  └── quiz_oop.py 실행 성공 ✅

Day 3 ── STEP 3
  ├── JSON 개념 이해
  ├── ScoreManager 클래스 작성
  └── scores.json 생성 확인 ✅

Day 4 ── STEP 4 & 5
  ├── Git 커밋 이력 정리
  ├── 브랜치 만들고 merge
  ├── GitHub 저장소 생성
  ├── README.md 작성
  └── 최종 push 완료 🎉




<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>🎮 나만의 퀴즈 게임 만들기</title>
<style>
:root {
  --bg: #f0f2f8;
  --panel: #ffffff;
  --panel2: #f5f7ff;
  --line: #d4d9ee;
  --text: #1a1f36;
  --muted: #5a6080;
  --blue: #2563eb;
  --green: #0d9488;
  --yellow: #d97706;
  --red: #dc2626;
  --purple: #7c3aed;
  --code: #1e2235;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--text);
  font: 15px/1.75 "Pretendard","Noto Sans KR",system-ui,sans-serif;
}

/* ── 레이아웃 ── */
.layout { max-width: 1200px; margin: auto; display: flex; }

/* ── 사이드바 ── */
.side {
  width: 240px; flex-shrink: 0;
  position: sticky; top: 0; height: 100vh; overflow-y: auto;
  padding: 28px 14px; border-right: 1px solid var(--line);
  background: var(--panel);
}
.side-title {
  font-size: 10px; font-weight: 800; letter-spacing: 2px;
  color: var(--muted); padding: 0 10px; margin-bottom: 14px;
}
.side a {
  display: block; text-decoration: none; color: var(--muted);
  padding: 7px 11px; border-radius: 8px; font-size: 13px;
  transition: all .15s;
}
.side a:hover { background: var(--panel2); color: var(--blue); }

/* ── 메인 ── */
main { flex: 1; min-width: 0; padding: 38px 36px 80px; }

/* ── 히어로 ── */
.hero {
  background: linear-gradient(130deg,#dbeafe,#f0f2f8 65%);
  border: 1px solid var(--line); border-radius: 18px;
  padding: 28px 32px; margin-bottom: 36px;
}
.hero-tag { font-size: 11px; font-weight: 700; color: var(--green); margin-bottom: 8px; }
.hero h1 { font-size: 28px; line-height: 1.35; margin-bottom: 10px; }
.hero p { color: var(--muted); font-size: 14px; }

/* ── 섹션 ── */
section { margin: 36px 0; scroll-margin-top: 20px; }
.sec-head { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }
.sec-num {
  background: #70a5ff20; color: var(--blue);
  padding: 4px 11px; border-radius: 8px; font-weight: 800; font-size: 13px;
}
.sec-head h2 { font-size: 20px; }
.sec-sub { color: var(--muted); font-size: 13px; margin-bottom: 14px; }

/* ── 카드 ── */
.card {
  background: var(--panel); border: 1px solid var(--line);
  border-radius: 13px; margin: 12px 0; overflow: hidden;
}
.card-body { padding: 18px 20px; }
.card-body p, .card-body li { color: var(--muted); margin-bottom: 6px; }
.card-body strong { color: var(--text); }
.card-body ul { padding-left: 18px; }

/* ── 콜아웃 ── */
.call {
  padding: 12px 15px; border-left: 3px solid var(--blue);
  background: #70a5ff12; border-radius: 7px;
  margin: 12px 0; color: var(--muted); font-size: 13px;
}
.call.warn { border-color: var(--yellow); background: #f5c95b12; }
.call.good { border-color: var(--green); background: #45d6ae12; }

/* ── 코드 블록 ── */
.code-wrap { position: relative; margin: 12px 0; }
pre {
  background: var(--code); border: 1px solid #2e3350;
  border-radius: 9px; padding: 16px 16px 16px 16px;
  color: #c8d4f0; font: 13px/1.65 Consolas,monospace;
  overflow-x: auto; white-space: pre;
}
.copy-btn {
  position: absolute; top: 8px; right: 8px;
  background: var(--panel2); border: 1px solid var(--line);
  color: var(--muted); padding: 3px 9px; border-radius: 5px;
  cursor: pointer; font-size: 11px;
}
code {
  background: #1e2235; padding: 2px 6px;
  border-radius: 4px; color: #93c5fd; font-size: 13px;
}

/* ── 테이블 ── */
table { border-collapse: collapse; width: 100%; font-size: 13px; margin: 12px 0; }
th, td { text-align: left; border-bottom: 1px solid var(--line); padding: 9px 11px; vertical-align: top; }
th { background: var(--panel2); color: var(--blue); font-weight: 700; }
td { color: var(--muted); }

/* ── 플로우 ── */
.flow { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: 12px 0; }
.flow span {
  background: var(--panel2); border: 1px solid var(--line);
  padding: 7px 12px; border-radius: 8px; font-size: 13px;
}
.arrow { color: var(--green); font-weight: 700; }

/* ── 체크리스트 ── */
.checklist { list-style: none; padding: 0; }
.checklist li {
  display: flex; gap: 10px; align-items: flex-start;
  padding: 6px 0; color: var(--muted); font-size: 14px;
}
.checklist input[type="checkbox"] { margin-top: 4px; accent-color: var(--green); }

/* ── 스텝 배지 ── */
.step-badge {
  display: inline-block; background: var(--blue); color: #fff;
  font-size: 11px; font-weight: 700; padding: 3px 10px;
  border-radius: 20px; margin-bottom: 10px;
}

/* ── 폴더 트리 ── */
.tree {
  background: var(--code); border-radius: 9px;
  padding: 16px; font: 13px/1.8 Consolas,monospace;
  color: #c8d4f0; margin: 12px 0;
}

/* ── 반응형 ── */
@media(max-width:800px) {
  .side { display: none; }
  main { padding: 20px 16px 50px; }
  .hero h1 { font-size: 22px; }
}
</style>
</head>
<body>
<div class="layout">

<!-- ══════════════ 사이드바 ══════════════ -->
<nav class="side">
  <div class="side-title">QUIZ GAME GUIDE</div>
  <a href="#intro">🎯 미션 소개</a>
  <a href="#ready">🛠️ 준비하기</a>
  <a href="#roadmap">🗺️ 전체 로드맵</a>
  <a href="#step1">STEP 1 · 기본 버전</a>
  <a href="#step2">STEP 2 · 클래스</a>
  <a href="#step3">STEP 3 · JSON 저장</a>
  <a href="#step4">STEP 4 · Git</a>
  <a href="#step5">STEP 5 · GitHub</a>
  <a href="#concepts">📚 핵심 개념 카드</a>
  <a href="#checklist">✅ 완료 체크리스트</a>
</nav>

<!-- ══════════════ 메인 ══════════════ -->
<main>

<!-- 히어로 -->
<div class="hero">
  <div class="hero-tag">BEGINNER GUIDE · PYTHON / GIT / GITHUB</div>
  <h1>🎮 나만의 퀴즈 게임 만들기<br>— 완전 초보자 가이드</h1>
  <p>문법을 <strong>아는 것</strong>에서 → 프로그램을 <strong>만드는 것</strong>으로<br>
  처음부터 끝까지, 혼자서, 완성까지.</p>
</div>

<!-- ══════════════ 미션 소개 ══════════════ -->
<section id="intro">
  <div class="sec-head">
    <span class="sec-num">🎯</span>
    <h2>미션 소개</h2>
  </div>

  <div class="card">
    <div class="card-body">
      <p><strong>왜 이 미션인가요?</strong></p>
      <p>책으로 배운 수영 이론만으로는 절대 수영할 수 없습니다. 직접 물에 들어가야 합니다.</p>
      <ul>
        <li>if문이 뭔지 안다 → if문으로 <strong>정답 판별</strong>을 만든다</li>
        <li>변수가 뭔지 안다 → 변수로 <strong>점수를 직접 관리</strong>한다</li>
        <li>클래스가 뭔지 안다 → 클래스로 <strong>퀴즈를 직접 설계</strong>한다</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <p><strong>무엇을 만드나요?</strong> — 터미널에서 동작하는 나만의 퀴즈 게임 🎮</p>
      <div class="code-wrap">
        <pre>╔══════════════════════════════════╗
║       🎮 나만의 퀴즈 게임!       ║
╠══════════════════════════════════╣
║  🏅 역대 점수 순위               ║
║     🥇 홍길동 — 3점              ║
║     🥈 김철수 — 2점              ║
╠══════════════════════════════════╣
║  이름을 입력하세요: 이영희        ║
║                                  ║
║  Q1. 파이썬을 만든 사람은?       ║
║    1. 빌 게이츠                  ║
║    2. 귀도 반 로섬               ║
║    3. 스티브 잡스                ║
║  정답 번호 입력: 2               ║
║  ✅ 정답입니다!                  ║
║                                  ║
║  🏆 최종 점수: 3 / 3             ║
║  💾 점수가 저장되었습니다!       ║
╚══════════════════════════════════╝</pre>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <p><strong>이 미션으로 얻는 것</strong></p>
      <table>
        <tr><th>영역</th><th>배우는 것</th><th>결과물</th></tr>
        <tr><td>🐍 Python</td><td>입출력 · 리스트 · 딕셔너리 · 클래스</td><td><code>.py</code> 파일</td></tr>
        <tr><td>💾 데이터</td><td>JSON 파일 저장 · 불러오기</td><td><code>scores.json</code></td></tr>
        <tr><td>🌿 Git</td><td>커밋 · 브랜치 · 병합</td><td>커밋 이력</td></tr>
        <tr><td>🌐 GitHub</td><td>공개 저장소 · README</td><td>포트폴리오</td></tr>
      </table>
    </div>
  </div>
</section>

<!-- ══════════════ 준비하기 ══════════════ -->
<section id="ready">
  <div class="sec-head">
    <span class="sec-num">🛠️</span>
    <h2>준비하기</h2>
  </div>

  <div class="card">
    <div class="card-body">
      <p><strong>Python 설치 확인</strong></p>
      <div class="code-wrap">
        <button class="copy-btn" onclick="cp(this)">복사</button>
        <pre>python --version
# Python 3.11.0  ← 이렇게 나오면 OK!</pre>
      </div>
      <div class="call warn">설치가 안 되어 있다면 → <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a><br>
      ⚠️ 설치 시 <strong>Add Python to PATH</strong> 체크박스를 반드시 체크하세요!</div>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <p><strong>Git 설치 확인</strong></p>
      <div class="code-wrap">
        <button class="copy-btn" onclick="cp(this)">복사</button>
        <pre>git --version
# git version 2.43.0  ← 이렇게 나오면 OK!</pre>
      </div>
      <div class="call warn">설치가 안 되어 있다면 → <a href="https://git-scm.com/downloads" target="_blank">https://git-scm.