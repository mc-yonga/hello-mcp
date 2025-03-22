import os


def seminar_attendees() -> str:
    # 현재 스크립트 파일의 디렉토리 경로를 기준으로 파일 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "seminar.md")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"
