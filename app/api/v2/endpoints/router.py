# app/api/v2/endpoints/router.py
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.schemas import WeightRequest, WeightListResponse
from infra.postgresql.orm_client import get_orm_session
from func_new.repository import LoraWeightRepository
from func_new.service import LoraWeightService

router = APIRouter()

# 🌟 response_model에 List[WeightItem]을 지정하면, 
# Pydantic이 알아서 DB 객체의 나머지 컬럼(registered_at 등)은 쳐내고 딱 3개만 JSON으로 내보냅니다!
@router.get("/lora_weights", response_model=WeightListResponse)
async def get_lora_weights_api(
    request: WeightRequest = Depends(),
    session: AsyncSession = Depends(get_orm_session) # ORM 세션 주입
):
    # 1. 객체 조립 (Dependency Injection)
    repo = LoraWeightRepository(session)
    service = LoraWeightService(repo)
    
    # 2. 서비스 실행 및 결과 반환
    items = await service.get_weight_list(request.status)
    
    # 🌟 최종 응답 포장지에 예쁘게 담아서 리턴!
    return WeightListResponse(
        total_count=len(items),
        items=items
    )