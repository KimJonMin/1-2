📋 전체 로드맵 (14단계)

[준비]
 1️⃣  GitHub 저장소 생성 & 로컬 연결
 2️⃣  프로젝트 폴더 구조 & .gitignore, README.md
 
[개발 - main 브랜치]
 3️⃣  메인 메뉴 뼈대 만들기 (실행/종료)
 4️⃣  공통 입력 함수 만들기 (예외 처리)
 5️⃣  Quiz 클래스 만들기
 6️⃣  기본 퀴즈 데이터 5개 작성
 
[개발 - 브랜치 활용]
 7️⃣  퀴즈 풀기 기능 (feature 브랜치 → main 병합)
 8️⃣  퀴즈 추가 기능
 9️⃣  퀴즈 목록 기능
 🔟 점수 기능
 
[마무리]
 1️⃣1️⃣ QuizGame 클래스로 전체 리팩토링
 1️⃣2️⃣ state.json 저장/불러오기 완성
 1️⃣3️⃣ README.md 완성
 1️⃣4️⃣ clone/pull 실습

 🚀 1단계: GitHub 저장소 생성 & 로컬 연결
① GitHub에서 저장소 만들기
github.com 로그인
오른쪽 상단 + → New repository 클릭
다음과 같이 입력:
Repository name: python-quiz-game (원하는 이름)
Description: 터미널에서 동작하는 Python 퀴즈 게임
Public 선택 (공개 저장소)
⚠️ "Add a README file" 체크 안 함 (우리가 직접 만들 거예요)
⚠️ .gitignore, license도 체크 안 함
Create repository 클릭
② 로컬에 폴더 만들고 Git 초기화
터미널(Windows는 PowerShell/Git Bash, Mac은 Terminal)을 열고:


# 작업할 폴더로 이동 (예: 바탕화면)
cd ~/Desktop

# 프로젝트 폴더 생성 & 이동
mkdir python-quiz-game
cd python-quiz-game

# Git 초기화
git init

# 기본 브랜치명을 main으로 변경 (혹시 master라면)
git branch -M main

③ GitHub 저장소와 연결
GitHub 저장소 페이지에 나오는 HTTPS 주소를 복사한 뒤:

bash
📋 복사
# 원격 저장소 연결 (자신의 주소로 바꾸세요!)
git remote add origin https://github.com/본인아이디/python-quiz-game.git

# 연결 확인
git remote -v

origin https://github.com/.../python-quiz-game.git (fetch) 처럼 나오면 성공!

✅ 1단계 체크리스트
GitHub에 저장소 생성 완료
로컬에 폴더 만들고 git init 완료
git remote -v 명령으로 origin이 보임

# 1단계: GitHub 저장소 생성 & 로컬 연결

> 🎯 **목표**: GitHub에 원격 저장소를 만들고, 내 컴퓨터(로컬)의 프로젝트 폴더와 연결한다.

---

## 📋 사전 준비

시작 전에 아래가 설치되어 있는지 확인하세요.

```bash
# Git 설치 확인
git --version

# Python 설치 확인
python --version
# 또는
python3 --version
```

- ✅ 버전이 출력되면 정상
- ❌ `command not found` 라면 [Git 다운로드](https://git-scm.com/) / [Python 다운로드](https://www.python.org/)에서 설치

또한 **GitHub 계정**이 필요합니다. ([github.com](https://github.com) 회원가입)

---

## ① GitHub에서 원격 저장소 만들기

1. [github.com](https://github.com) 에 로그인
2. 오른쪽 상단 **`+`** 아이콘 → **New repository** 클릭
3. 아래와 같이 입력:

| 항목 | 값 |
|------|-----|
| Repository name | `python-quiz-game` |
| Description | `터미널에서 동작하는 Python 퀴즈 게임` |
| 공개 범위 | **Public** |
| Add a README file | ❌ **체크 안 함** |
| Add .gitignore | ❌ **체크 안 함** |
| Choose a license | ❌ **None** |

> 💡 README, .gitignore는 다음 단계에서 **직접** 만들 것이므로 여기선 체크하지 않습니다.

4. **Create repository** 버튼 클릭
5. 다음 화면에 나오는 **HTTPS 주소를 복사**해 둡니다.
   - 예: `https://github.com/본인아이디/python-quiz-game.git`

---

## ② 로컬 폴더 만들기 & Git 초기화

터미널을 엽니다.
- **Windows**: PowerShell 또는 Git Bash
- **Mac/Linux**: Terminal

```bash
# 1. 작업할 위치로 이동 (예: 바탕화면)
cd ~/Desktop

# 2. 프로젝트 폴더 생성
mkdir python-quiz-game

# 3. 폴더로 진입
cd python-quiz-game

# 4. Git 저장소로 초기화
git init

# 5. 기본 브랜치명을 main으로 설정
git branch -M main
```

### 📌 각 명령어 의미

| 명령어 | 설명 |
|--------|------|
| `cd ~/Desktop` | 바탕화면으로 이동 |
| `mkdir python-quiz-game` | 폴더 생성 |
| `cd python-quiz-game` | 생성한 폴더로 이동 |
| `git init` | 현재 폴더를 Git으로 관리 시작 |
| `git branch -M main` | 기본 브랜치명을 `main`으로 지정 |

---

## ③ 원격 저장소(GitHub)와 연결

```bash
# 원격 저장소 등록 (아래 주소는 본인 것으로 교체!)
git remote add origin https://github.com/본인아이디/python-quiz-game.git

# 연결 상태 확인
git remote -v
```

### ✅ 정상 출력 예시

```
origin  https://github.com/본인아이디/python-quiz-game.git (fetch)
origin  https://github.com/본인아이디/python-quiz-game.git (push)
```

이렇게 2줄이 나오면 연결 성공입니다! 🎉

---

## ✅ 체크리스트

- [ ] GitHub에 `python-quiz-game` 저장소를 만들었다
- [ ] 로컬에 같은 이름의 폴더를 만들었다
- [ ] `git init` 으로 Git 초기화를 했다
- [ ] 기본 브랜치명이 `main` 이다
- [ ] `git remote -v` 실행 시 origin 주소가 보인다

---

## ⚠️ 자주 겪는 문제

### Q1. `git` 명령어가 인식되지 않아요
- Git이 설치되지 않았거나, 환경변수(PATH)에 등록되지 않은 상태입니다.
- Windows: Git 재설치 시 **"Git from the command line..."** 옵션 선택

### Q2. `git remote add` 할 때 이미 존재한다고 나와요
```bash
# 기존 origin을 삭제 후 다시 등록
git remote remove origin
git remote add origin https://github.com/본인아이디/python-quiz-game.git
```

### Q3. push할 때 로그인하라고 나와요
- GitHub는 비밀번호 대신 **Personal Access Token(PAT)** 을 사용합니다.
- GitHub → Settings → Developer settings → Personal access tokens 에서 발급
- 비밀번호 입력창에 토큰을 붙여넣으세요.

---

# 2단계: .gitignore & README.md 생성 + 첫 커밋/푸시

> 🎯 **목표**: Git이 추적하지 말아야 할 파일을 지정(.gitignore)하고, 프로젝트 소개 파일(README.md)을 만든 뒤, **첫 번째 커밋과 푸시**를 수행한다.

---

## 📚 왜 이 파일들이 필요한가요?

### `.gitignore`
- Git이 **추적하지 않을 파일/폴더 목록**을 적는 파일
- 예: Python 캐시 파일(`__pycache__/`), 가상환경 폴더, OS가 만드는 숨김 파일 등
- 쓸데없는 파일이 GitHub에 올라가는 걸 막아줍니다

### `README.md`
- 저장소 첫 화면에 보이는 **프로젝트 설명서**
- 다른 사람(그리고 미래의 나)이 프로젝트를 이해하도록 돕습니다
- 지금은 **기본 뼈대만** 만들고, 마지막 13단계에서 완성합니다

---

## ① `.gitignore` 파일 생성

프로젝트 폴더(`python-quiz-game`) 안에 `.gitignore` 파일을 만듭니다.

### 📌 파일 생성 방법

**방법 A. 터미널에서 생성 (Mac/Linux/Git Bash)**
```bash
touch .gitignore
```

**방법 B. VS Code 등 에디터에서 직접 생성**
- 에디터에서 새 파일 → 파일명을 `.gitignore` 로 저장

### 📝 `.gitignore` 내용

아래 내용을 복사해서 붙여넣으세요:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd

# 가상환경
venv/
env/
.venv/

# IDE / 에디터 설정
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# 로그 파일
*.log
```

### 📌 각 항목 설명

| 항목 | 설명 |
|------|------|
| `__pycache__/` | Python 실행 시 자동 생성되는 캐시 폴더 |
| `*.py[cod]` | 컴파일된 Python 파일 (.pyc, .pyo, .pyd) |
| `venv/`, `.venv/` | 가상환경 폴더 |
| `.vscode/`, `.idea/` | 에디터 개인 설정 |
| `.DS_Store` | Mac에서 자동 생성되는 숨김파일 |
| `Thumbs.db` | Windows 썸네일 캐시 |

> 💡 **주의**: 미션 요구사항에 따라 `state.json`은 `.gitignore`에 **추가하지 않습니다**. 퀴즈 데이터는 저장소에 함께 올려야 합니다.

---

## ② `README.md` 파일 생성 (기본 뼈대)

### 📌 파일 생성

```bash
touch README.md
```

또는 에디터에서 `README.md` 파일 생성

### 📝 초기 내용 (뼈대)

```markdown
# 🎯 Python Quiz Game

터미널에서 동작하는 Python 퀴즈 게임입니다.

## 📖 프로젝트 소개

Python 기본 문법, 객체지향(OOP), JSON 파일 입출력, Git 버전 관리를 학습하기 위한 프로젝트입니다.

## 🚧 개발 진행 중

현재 개발 중인 프로젝트입니다. 완성 후 아래 항목이 추가됩니다.

- [ ] 프로젝트 개요
- [ ] 퀴즈 주제와 선정 이유
- [ ] 실행 방법
- [ ] 기능 목록
- [ ] 파일 구조
- [ ] 데이터 파일 설명

## 🛠 기술 스택

- Python 3.x
- JSON (데이터 저장)
- Git & GitHub (버전 관리)
```

> 💡 자세한 내용은 **13단계**에서 완성할 것이므로, 지금은 이 정도로 충분합니다.

---

## ③ 첫 커밋 & 푸시

이제 파일 2개(+폴더에 있는 1단계 문서)를 **Git에 기록**하고 **GitHub에 올립니다**.

### 1️⃣ 현재 상태 확인

```bash
git status
```

### ✅ 출력 예시
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        docs/
```

- `Untracked files` = Git이 아직 추적하지 않는 새 파일들

### 2️⃣ 파일을 스테이징 (커밋 대기 영역에 올리기)

```bash
# 모든 변경사항 추가
git add .
```

### 3️⃣ 다시 상태 확인

```bash
git status
```

### ✅ 출력 예시
```
Changes to be committed:
        new file:   .gitignore
        new file:   README.md
        new file:   docs/step01-github-setup.md
        new file:   docs/step02-gitignore-readme.md
```

초록색으로 `new file` 표시가 나오면 OK!

### 4️⃣ 커밋하기

```bash
git commit -m "chore: 프로젝트 초기 설정 (.gitignore, README.md)"
```

### ✅ 출력 예시
```
[main (root-commit) a1b2c3d] chore: 프로젝트 초기 설정 (.gitignore, README.md)
 4 files changed, 60 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 ...
```

### 5️⃣ GitHub에 푸시 (업로드)

```bash
git push -u origin main
```

> 💡 `-u` 옵션은 "앞으로 `git push` 만 입력해도 origin/main 에 올려라"라는 설정입니다. **처음 한 번만** 사용합니다.

### ✅ 성공 출력 예시
```
Enumerating objects: 6, done.
...
To https://github.com/본인아이디/python-quiz-game.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

---

## ④ GitHub에서 확인

브라우저에서 내 GitHub 저장소를 열어봅니다:
`https://github.com/본인아이디/python-quiz-game`

- ✅ `.gitignore`, `README.md`, `docs/` 폴더가 보이면 성공!
- ✅ README의 내용이 저장소 하단에 렌더링되어 보임

---

## 💬 커밋 메시지 컨벤션 (알아두면 좋아요)

커밋 메시지 앞에 붙는 단어들은 변경 성격을 나타냅니다:

| 타입 | 의미 |
|------|------|
| `feat:` | 새 기능 추가 |
| `fix:` | 버그 수정 |
| `chore:` | 설정, 환경 등 기타 작업 |
| `docs:` | 문서 변경 (README 등) |
| `refactor:` | 코드 구조 개선 (기능 변화 X) |

> 💡 꼭 지켜야 하는 건 아니지만, 팀 협업 시 매우 유용합니다.

---

## ✅ 체크리스트

- [ ] `.gitignore` 파일을 만들었다
- [ ] `README.md` 파일을 만들었다 (기본 뼈대)
- [ ] `git add .` 로 스테이징했다
- [ ] `git commit -m "..."` 으로 커밋했다
- [ ] `git push -u origin main` 으로 GitHub에 업로드했다
- [ ] GitHub 웹페이지에서 파일들이 보인다

---

## ⚠️ 자주 겪는 문제

### Q1. `git push` 할 때 인증 오류가 나요
```
remote: Support for password authentication was removed...
```
- GitHub는 비밀번호 대신 **Personal Access Token(PAT)** 을 사용합니다
- GitHub → Settings → Developer settings → Personal access tokens → **Generate new token (classic)**
- 권한(`repo`) 체크 후 발급 → 비밀번호 입력창에 **토큰을 붙여넣기**

### Q2. 커밋할 이름/이메일 설정이 안 되어 있다고 나와요
```bash
git config --global user.name "본인이름"
git config --global user.email "본인이메일@example.com"
```

### Q3. `.gitignore`를 만들었는데도 파일이 추적돼요
- `.gitignore`는 **아직 추적되지 않은 파일에만** 적용됩니다
- 이미 `git add` 된 파일을 무시하려면:
  ```bash
  git rm --cached 파일명
  ```

### Q4. 잘못된 커밋 메시지를 바꾸고 싶어요 (아직 push 안 한 경우)
```bash
git commit --amend -m "수정된 메시지"
```

---

