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
# Python 3.11.0  

git --version
# git version 2.43.0  ← 이렇게 나오면 OK!

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

파일 구조

quiz-game/
└── quiz.py   ← 지금 만들 파일

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

python quiz.py
✅ STEP 1 완료 기준 : 터미널에서 퀴즈가 출제되고 점수가 출력된다

STEP 2 · 클래스로 구조화하기
🎯 목표 : 코드를 역할별로 나눠 읽기 쉽고 고치기 쉽게 만든다

클래스가 왜 필요한가요?

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




