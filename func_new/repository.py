# func_new/repository.py
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from func_new.models import LoraWeightEntity

class LoraWeightRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def fetch_weights(self, status: str = None):
        # 기본 쿼리: 전체 조회
        query = select(LoraWeightEntity)
        
        # 만약 status 값이 들어왔다면 WHERE 조건 추가
        if status:
            query = query.where(LoraWeightEntity.status == status)
            
        result = await self.session.execute(query)
        return result.scalars().all() # DB 객체 리스트 반환