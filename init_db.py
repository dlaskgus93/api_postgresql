# init_db.py (테스트 환경 세팅용 스크립트)
import asyncio
from infra.postgresql.orm_client import engine, AsyncSessionLocal
from func_new.models import Base, LoraWeightEntity

async def init_test_db():
    # 1. test.db 파일 안에 테이블(거푸집)을 짠! 하고 만듭니다.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all) # 기존꺼 날리기
        await conn.run_sync(Base.metadata.create_all) # 새로 만들기

    # 2. 가짜 데이터(더미)를 3개 집어넣습니다.
    async with AsyncSessionLocal() as session:
        dummy1 = LoraWeightEntity(model_name="qwen2.5-lora", status="loaded", updated_by="admin")
        dummy2 = LoraWeightEntity(model_name="llama3-lora", status="loading", updated_by="admin")
        dummy3 = LoraWeightEntity(model_name="mistral-lora", status="unload", updated_by="system")
        
        session.add_all([dummy1, dummy2, dummy3])
        await session.commit()
        print("✅ 로컬 테스트 DB(test.db) 세팅 및 더미 데이터 삽입 완료!")

# 스크립트 실행!
asyncio.run(init_test_db())