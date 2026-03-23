# func_new/service.py
from func_new.repository import LoraWeightRepository

class LoraWeightService:
    def __init__(self, repository: LoraWeightRepository):
        self.repository = repository

    async def get_weight_list(self, status: str = None):
        # 1. 인프라(Repo)에 데이터 요청
        weights = await self.repository.fetch_weights(status)
        
        # 2. 추가 비즈니스 로직이 있다면 여기서 처리 (현재는 바로 반환)
        return weights