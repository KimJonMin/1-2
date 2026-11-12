# quiz.py
from storage import Storage

class Quiz:
    """개별 퀴즈 데이터"""
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
    def display(self):
        """퀴즈 문제와 선택지 표시"""
        print(f"\n❓ {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"   {i}. {choice}")

    def check_answer(self, user_answer):
        """사용자 답변 확인"""
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])


class QuizGame:
    """퀴즈 게임 로직"""
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load()

    def load(self):
        """저장된 데이터 불러오기"""
        data = Storage.load()
        
        if data is None:
            self._load_default()
            self.save()
            return

        try:
            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data["best_score"]
            print(f"✅ 퀴즈 {len(self.quizzes)}개 로드됨")
        except Exception as e:
            print(f"❌ 오류: {e}")
            self._load_default()

    def _load_default(self):
        """기본 퀴즈 로드"""
        self.quizzes = [
            Quiz("파이썬을 만든 사람은?", ["빌 게이츠", "귀도 반 로섬", "스티브 잡스", "리누스 토르발스"], 1),
            Quiz("Python의 의미는?", ["뱀", "프로그래밍 언어", "회사명", "사람이름"], 0),
            Quiz("git의 주 용도는?", ["버전 관리", "파일 압축", "이미지 편집", "음악 재생"], 0),
            Quiz("GitHub는 어디 회사?", ["구글", "마이크로소프트", "아마존", "애플"], 1),
            Quiz("JSON 형식의 확장자는?", [".txt", ".json", ".xml", ".csv"], 1),
            Quiz("Python 리스트의 인덱스는?", ["1부터 시작", "0부터 시작", "-1부터 시작", "정해지지 않음"], 1),
            Quiz("다음 중 Python 문법이 아닌 것은?", ["if", "for", "while", "goto"], 3),
            Quiz("딕셔너리의 키는 어떤 타입?", ["리스트만 가능", "정수만 가능", "불변 타입", "모든 타입"], 2),
            Quiz("UTF-8의 주 용도는?", ["압축", "문자 인코딩", "이미지 형식", "동영상 형식"], 1),
            Quiz("예외 처리의 기본 문법은?", ["try-except", "if-else", "for-in", "while-do"], 0),
        ]
        self.best_score = 0

    def save(self):
        """게임 데이터 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        Storage.save(data)

    def play(self):
        """퀴즈 풀기"""
        if not self.quizzes:
            print("❌ 퀴즈가 없습니다!")
            return

        score = 0
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n[{i}/{len(self.quizzes)}] {quiz.question}")
            for j, choice in enumerate(quiz.choices, 1):
                print(f"  {j}. {choice}")

            try:
                answer = int(input("답을 선택하세요 (1-4): ")) - 1
                if 0 <= answer < len(quiz.choices):
                    if answer == quiz.answer:
                        print("✅ 정답!")
                        score += 1
                    else:
                        print(f"❌ 틀렸습니다. 정답: {quiz.answer + 1}번")
                else:
                    print("❌ 1-4 사이의 숫자를 입력하세요!")
            except ValueError:
                print("❌ 숫자를 입력하세요!")
            except (KeyboardInterrupt, EOFError):
                print("\n\n게임을 종료합니다.")
                return

        print(f"\n🎉 게임 종료! 점수: {score}/{len(self.quizzes)}")
        if score > self.best_score:
            self.best_score = score
            self.save()
            print(f"🏆 새로운 최고점수! {score}점")

    def add_quiz(self):
        """새 퀴즈 추가"""
        try:
            question = input("문제를 입력하세요: ")
            if not question.strip():
                print("❌ 문제를 입력하세요!")
                return

            choices = []
            for i in range(4):
                choice = input(f"선택지 {i+1}을 입력하세요: ")
                if not choice.strip():
                    print("❌ 모든 선택지를 입력하세요!")
                    return
                choices.append(choice)

            answer = int(input("정답 번호를 입력하세요 (1-4): ")) - 1
            if not (0 <= answer < 4):
                print("❌ 1-4 사이의 숫자를 입력하세요!")
                return

            self.quizzes.append(Quiz(question, choices, answer))
            self.save()
            print("✅ 퀴즈가 추가되었습니다!")
        except ValueError:
            print("❌ 숫자를 입력하세요!")
        except (KeyboardInterrupt, EOFError):
            print("\n취소되었습니다.")

    def show_quizzes(self):
        """모든 퀴즈 표시"""
        if not self.quizzes:
            print("❌ 퀴즈가 없습니다!")
            return

        print(f"\n📋 전체 퀴즈 ({len(self.quizzes)}개)\n")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")
            for j, choice in enumerate(quiz.choices, 1):
                marker = "✓" if j - 1 == quiz.answer else " "
                print(f"    {j}. [{marker}] {choice}")

    def show_best_score(self):
        """최고 점수 표시"""
        print(f"\n🏆 최고 점수: {self.best_score}점")

    def menu(self):
        """메인 메뉴"""
        while True:
            print("\n" + "="*40)
            print("🎮 퀴즈 게임 메뉴")
            print("="*40)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 최고 점수")
            print("5. 종료")
            print("="*40)

            try:
                choice = input("선택하세요 (1-5): ")
                if choice == "1":
                    self.play()
                elif choice == "2":
                    self.add_quiz()
                elif choice == "3":
                    self.show_quizzes()
                elif choice == "4":
                    self.show_best_score()
                elif choice == "5":
                    print("👋 게임을 종료합니다!")
                    break
                else:
                    print("❌ 1-5 사이의 숫자를 입력하세요!")
            except (KeyboardInterrupt, EOFError):
                print("\n\n👋 게임을 종료합니다!")
                break