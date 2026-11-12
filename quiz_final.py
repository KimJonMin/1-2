import json
import os

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])

class QuizGame:
    FILE = "state.json"

    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load()

    def load(self):
        """데이터 로드 (파일 없음/손상 시 복구 로직 포함)"""
        # 1. 파일이 없는 경우: 기본 데이터 사용
        if not os.path.exists(self.FILE):
            self._load_default()
            self.save()
            return

        # 2. 파일이 있는 경우 읽기 시도
        try:
            with open(self.FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data["best_score"]
        except (json.JSONDecodeError, KeyError, TypeError):
            # 📍 파일이 손상된 경우 (JSON 형식이 아니거나 데이터 구조가 틀린 경우)
            print("\n⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self._load_default()
            self.save()  # 복구된 데이터로 파일 덮어쓰기
        except Exception as e:
            print(f"\n⚠️ 알 수 없는 오류 발생: {e}")
            self._load_default()

    def _load_default(self):
        """기본 퀴즈 데이터 세팅"""
        self.quizzes = [
            Quiz("파이썬을 만든 사람은?", ["빌 게이츠", "귀도 반 로섬", "스티브 잡스", "리누스 토르발스"], 1),
            Quiz("Python의 의미는?", ["뱀", "프로그래밍 언어", "회사명", "사람이름"], 0),
            Quiz("git의 주 용도는?", ["버전 관리", "파일 압축", "이미지 편집", "음악 재생"], 0),
            Quiz("GitHub는 어디 회사?", ["구글", "마이크로소프트", "아마존", "애플"], 1),
        ]
        self.best_score = 0

    def save(self):
        data = {"quizzes": [q.to_dict() for q in self.quizzes], "best_score": self.best_score}
        with open(self.FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def play(self):
        """퀴즈 풀기 (재입력 로직 완벽 반영)"""
        if not self.quizzes:
            print("❌ 퀴즈가 없습니다!")
            return

        score = 0
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n[{i}/{len(self.quizzes)}] {quiz.question}")
            for j, choice in enumerate(quiz.choices, 1):
                print(f"  {j}. {choice}")

            while True:
                try:
                    user_input = input("답을 선택하세요 (1-4): ").strip()
                    if not user_input:
                        print("❌ 입력값이 없습니다. 숫자를 입력하세요!")
                        continue
                    
                    answer = int(user_input) - 1
                    if 0 <= answer < 4:
                        if answer == quiz.answer:
                            print("✅ 정답!")
                            score += 1
                        else:
                            print(f"❌ 틀렸습니다. 정답: {quiz.answer + 1}번")
                        break # 정답/오답 판단 후 다음 문제로
                    else:
                        print("❌ 1-4 사이의 숫자를 입력하세요!")
                except ValueError:
                    print("❌ 숫자를 입력하세요!")
                except (KeyboardInterrupt, EOFError):
                    print("\n⚠️ 게임을 중단합니다.")
                    return

        print(f"\n🎉 게임 종료! 점수: {score}/{len(self.quizzes)}")
        if score > self.best_score:
            self.best_score = score
            self.save()
            print(f"🏆 최고점수 갱신: {score}점")

    def add_quiz(self):
        """퀴즈 추가 (빈 값/범위 체크 적용)"""
        try:
            while True:
                question = input("문제를 입력하세요: ").strip()
                if question: break
                print("❌ 문제는 비어둘 수 없습니다!")

            choices = []
            for i in range(4):
                while True:
                    choice = input(f"선택지 {i+1}을 입력하세요: ").strip()
                    if choice:
                        choices.append(choice)
                        break
                    print(f"❌ 선택지 {i+1}을 입력해주세요!")

            while True:
                try:
                    ans_input = input("정답 번호를 입력하세요 (1-4): ").strip()
                    if not ans_input:
                        print("❌ 정답 번호를 입력해주세요!")
                        continue
                    answer = int(ans_input) - 1
                    if 0 <= answer < 4:
                        break
                    else:
                        print("❌ 1-4 사이의 숫자를 입력하세요!")
                except ValueError:
                    print("❌ 숫자를 입력하세요!")

            self.quizzes.append(Quiz(question, choices, answer))
            self.save()
            print("✅ 퀴즈가 추가되었습니다!")
        except (KeyboardInterrupt, EOFError):
            print("\n취소되었습니다.")

    def show_quizzes(self):
        if not self.quizzes:
            print("❌ 퀴즈가 없습니다!")
            return
        print(f"\n📋 전체 퀴즈 목록 ({len(self.quizzes)}개)")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question}")

    def show_score(self):
        print(f"\n🏆 최고 점수: {self.best_score}/{len(self.quizzes)}")

    def menu(self):
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
                if not choice:
                    print("❌ 메뉴 번호를 입력해주세요.")
                    continue
                
                if choice == "1": self.play()
                elif choice == "2": self.show_quizzes()
                elif choice == "3": self.add_quiz()
                elif choice == "4": self.show_score()
                elif choice == "5":
                    print("👋 게임을 종료합니다.")
                    break
                else:
                    print("❌ 1-5 사이의 숫자를 입력하세요!")
            except (KeyboardInterrupt, EOFError):
                print("\n👋 프로그램을 종료합니다.")
                break

if __name__ == "__main__":
    game = QuizGame()
    game.menu()