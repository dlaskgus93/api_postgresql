from pydantic import BaseModel
from typing import List, Optional

# [요청]
class WeightRequest(BaseModel):
    status: Optional[str] = None

# [알맹이] DB에서 뽑아올 개별 아이템
class WeightItem(BaseModel):
    weight_id: int
    model_name: str
    status: str

    class Config:
        from_attributes = True 

# 🌟 [응답 포장지] 사용자님이 찾으시던 바로 그 완벽한 Response 타입!
class WeightListResponse(BaseModel):
    total_count: int           # 총 몇 개인지 (보너스!)
    items: List[WeightItem]    # 진짜 리스트 데이터