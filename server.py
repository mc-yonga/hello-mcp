from mcp.server.fastmcp import FastMCP
from seminar import seminar_attendees
from datetime import datetime
import json

mcp = FastMCP("Seminar Management System")


@mcp.tool()
def get_seminar_details(party_name: str) -> str:
    """
    특정 세미나/파티의 상세 정보를 가져옵니다.

    Args:
        party_name: 세미나/파티 이름

    Returns:
        세미나 상세 정보(JSON 형식)
    """
    attendees = seminar_attendees(party_name)

    seminar_info = {
        "name": party_name,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "location": f"Conference Room {party_name}",
        "total_attendees": len(attendees),
        "attendees": attendees,
        "status": "scheduled",
    }

    return json.dumps(seminar_info, ensure_ascii=False, indent=2)


@mcp.tool()
def register_attendee(party_name: str, attendee_name: str) -> str:
    """
    새로운 참석자를 세미나에 등록합니다.

    Args:
        party_name: 세미나/파티 이름
        attendee_name: 새 참석자 이름

    Returns:
        등록 결과 메시지
    """

    # 실제 구현에서는 데이터베이스에 참석자를 추가하는 로직이 있을 것입니다

    return f"성공: {attendee_name}님이 {party_name} 세미나에 등록되었습니다."


@mcp.prompt()
def prompt(message: str) -> str:
    """
    사용자 메시지를 처리하기 위한 프롬프트를 생성합니다.

    Args:
        message: 사용자 메시지

    Returns:
        모델에게 전달될 프롬프트
    """
    return f"""
당신은 세미나 관리 시스템의 AI 어시스턴트입니다. 사용자에게 친절하고 도움이 되는 응답을 제공하세요.

사용 가능한 도구:
- get_seminar_details(party_name) - 특정 세미나의 상세 정보를 조회합니다.
- register_attendee(party_name, attendee_name) - 새 참석자를 등록합니다.

- 세미나 참석자 정보는 'seminar://파티이름' 형식의 리소스를 통해 접근할 수 있습니다.
- 파티이름은 순수하게 알파벳 문자만 포함해야 합니다.
    - ex) A조 -> seminar://A조 (X), seminar://A (O)

사용자 메시지: {message}

위 메시지를 분석하여 적절한 도구를 사용하거나, 직접 응답하세요. 요청이 명확하지 않은 경우 추가 정보를 요청하세요.
"""


if __name__ == "__main__":
    mcp.run()
