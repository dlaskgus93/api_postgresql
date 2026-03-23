from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

# 사용자님의 실제 FastAPI app을 불러오세요 (경로는 프로젝트에 맞게 수정)
from main import app 

client = TestClient(app)

# 🌟 서비스의 get_weight_list 함수 자체를 가로채서 가짜(Mock)로 만듭니다!
@patch("func_new.service.LoraWeightService.get_weight_list", new_callable=AsyncMock)
def test_get_lora_weights_router(mock_get_weight_list):
    
    # 1. 가짜 서비스가 반환할 가짜 데이터 세팅 (DB 안 거침!)
    mock_get_weight_list.return_value = [
        {"weight_id": 1, "model_name": "qwen2.5-lora", "status": "loaded"}
    ]

    # 2. API 호출 (상태가 'loaded'인 것 요청)
    response = client.get("/api/v2/lora_weights?status=loaded")

    # 3. 검증 (응답 코드 200, 응답 스키마가 기대한 형태인지 확인)
    assert response.status_code == 200
    
    data = response.json()
    assert data["total_count"] == 1
    assert data["items"][0]["model_name"] == "qwen2.5-lora"
    assert data["items"][0]["status"] == "loaded"