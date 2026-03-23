# infra/postgresql/orm_client.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# 실제 DB 주소로 변경해주세요. (예: postgresql+asyncpg://user:pass@localhost:5432/dbname)
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://계정:비밀번호@주소:포트/DB이름"

# ORM 전용 엔진 (통신망)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# ORM 전용 세션 팩토리 (통역사 채용)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# 라우터에서 Depends로 가져다 쓸 세션 발급기!
async def get_orm_session():
    async with AsyncSessionLocal() as session:
        yield session