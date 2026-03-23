import pytest
from unittest.mock import AsyncMock, MagicMock
from func_new.repository import LoraWeightRepository

@pytest.mark.asyncio
async def test_repository_fetch_weights():
    # 1. 가짜 DB 통역사(Session) 생성
    mock_session = AsyncMock()
    
    # 2. DB가 돌려줄 결과(Result) 객체를 가짜로 만들기
    mock_result = MagicMock()
    mock_result.scalars().all.return_value = ["fake_db_data"]
    mock_session.execute.return_value = mock_result

    # 3. 리포지토리 실행
    repo = LoraWeightRepository(mock_session)
    result = await repo.fetch_weights(status="loaded")

    # 4. 검증: 결과를 잘 뱉어내고, session.execute를 호출했는지 확인
    assert result == ["fake_db_data"]
    assert mock_session.execute.called