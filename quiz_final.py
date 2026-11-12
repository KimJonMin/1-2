import json
import os


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

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
    FILE = "state.json"

    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load()

    # ✅ 이 메서드가 필요함!
    def load(self):
        """저장된 퀴즈 데이터 불러오기"""
        if not os.path.exists(self.FILE):
            print("📂 저장 파일이 없습니다. 기본 퀴즈로 시작합니다.")
            self._load_default()
            self.save()
            return

        try:
            with open(self.FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data["best_score"]
            print(f"✅ 불러오기 완료! 퀴즈 {len(self.quizzes)}개")
        except Exception as e:
            print(f"❌ 오류: {e}")
            self._load_default()

    def _load_default(self):
        """기본 퀴즈 로드"""
        self.quizzes = [
            Quiz("파이썬을 만든 사람은?",
                 ["빌 게이츠", "귀도 반 로섬", "스티브 잡스", "리누스 토르발스"], 1),
            Quiz("Python의 의미는?",
                 ["뱀", "프로그래밍 언어", "회사명", "사람이름"], 0),
            Quiz("git의 주 용도는?",
                 ["버전 관리", "파일 압축", "이미지 편집", "음악 재생"], 0),
            Quiz("GitHub는 어디 회사?",
                 ["구글", "마이크로소프트", "아마존", "애플"], 1),
            Quiz("JSON 형식의 확장자는?",
                 [".txt", ".json", ".xml", ".csv"], 1),
            Quiz("Python 리스트의 인덱스는?",
                 ["1부터 시작", "0부터 시작", "-1부터 시작", "정해지지 않음"], 1),
            Quiz("다음 중 Python 문법이 아닌 것은?",
                 ["if", "for", "while", "goto"], 3),
            Quiz("딕셔너리의 키는 어떤 타입?",
                 ["리스트만 가능", "정수만 가능", "불변 타입", "모든 타입"], 2),
            Quiz("UTF-8의 주 용도는?",
                 ["압축", "문자 인코딩", "이미지 형식", "동영상 형식"], 1),
            Quiz("예외 처리의 기본 문법은?",
                 ["try-except", "if-else", "for-in", "while-do"], 0),
        ]
        self.best_score = 0

    def save(self):
        """퀴즈 데이터 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        try:
            with open(self.FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("💾 저장 완료!")
        except Exception as e:
            print(f"❌ 저장 오류: {e}")

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
        """퀴즈 추가하기"""
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
        """퀴즈 목록 보기"""
        if not self.quizzes:
            print("❌ 퀴즈가 없습니다!")
            return

        print(f"\n📋 전체 퀴즈 ({len(self.quizzes)}개)\n")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")
            for j, choice in enumerate(quiz.choices, 1):
                print(f"    {j}. {choice}")
            print()

    def show_score(self):
        """최고 점수 보기"""
        print(f"\n🏆 최고 점수: {self.best_score}/{len(self.quizzes)}")

    def menu(self):
        """메뉴 표시"""
        while True:
            print("\n" + "="*30)
            print("       🐍 Python 퀴즈 게임")
            print("="*30)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 목록 보기")
            print("3. 퀴즈 추가하기")
            print("4. 최고 점수 보기")
            print("5. 종료")
            print("="*30)

            try:
                choice = input("메뉴를 선택하세요 (1-5): ").strip()
                if choice == "1":
                    self.play()
                elif choice == "2":
                    self.show_quizzes()
                elif choice == "3":
                    self.add_quiz()
                elif choice == "4":
                    self.show_score()
                elif choice == "5":
                    print("👋 게임을 종료합니다. 수고하셨습니다!")
                    break
                else:
                    print("❌ 1-5 사이의 숫자를 입력하세요!")
            except (KeyboardInterrupt, EOFError):
                print("\n\n👋 게임을 종료합니다.")
                break


if __name__ == "__main__":
    game = QuizGame()
    game.menu()