# storage.py
import json
import os

class Storage:
    """JSON 파일 읽기·쓰기 담당"""
    FILE = "state.json"

    @staticmethod
    def load():
        """state.json에서 데이터 읽기"""
        if not os.path.exists(Storage.FILE):
            print("📂 저장 파일이 없습니다.")
            return None

        try:
            with open(Storage.FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"✅ 불러오기 완료!")
            return data
        except Exception as e:
            print(f"❌ 읽기 오류: {e}")
            return None

    @staticmethod
    def save(data):
        """데이터를 state.json에 저장"""
        try:
            with open(Storage.FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("💾 저장 완료!")
        except Exception as e:
            print(f"❌ 저장 오류: {e}")