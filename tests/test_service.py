import pytest
from unittest.mock import AsyncMock
from func_new.service import LoraWeightService

@pytest.mark.asyncio
async def test_service_get_weight_list():
    # 1. 가짜 창고 관리자(Mock Repository) 생성
    mock_repo = AsyncMock()
    
    # 2. 창고 관리자가 넘겨줄 가짜 DB 엔티티 객체 생성
    class FakeEntity:
        weight_id = 1
        model_name = "test-model"
        status = "loaded"
        
    mock_repo.fetch_weights.return_value = [FakeEntity()]

    # 3. 서비스에 가짜 창고 관리자를 주입하여 실행
    service = LoraWeightService(mock_repo)
    result = await service.get_weight_list(status="loaded")

    # 4. 검증: 결과가 잘 나오는지, fetch_weights 함수를 "loaded" 파라미터와 함께 잘 호출했는지 확인
    assert len(result) == 1
    assert result[0].model_name == "test-model"
    mock_repo.fetch_weights.assert_called_once_with("loaded")