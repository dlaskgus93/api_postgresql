# main.py
from fastapi import FastAPI

# 우리가 열심히 만든 라우터를 불러옵니다!
# (as lora_router 라고 이름표를 붙여주면 나중에 헷갈리지 않습니다)
from app.api.v2.endpoints.router import router as lora_router

# 1. FastAPI 앱(서버 객체) 생성
# 여기에 적는 title과 description이 그대로 Swagger UI(/docs)의 예쁜 제목이 됩니다!
app = FastAPI(
    title="LoRA 가중치 관리 API",
    description="PostgreSQL DB에서 LoRA 가중치 목록과 상태를 조회하는 API입니다.",
    version="2.0.0"
)

# 2. 라우터 등록 (건물에 방을 연결하는 작업)
# prefix="/api/v2"를 붙여주면, 우리 엔드포인트가 자동으로 "/api/v2/lora_weights" 가 됩니다.
app.include_router(lora_router, prefix="/api/v2", tags=["LoRA Weights"])

# 3. (보너스) 서버가 잘 켜졌는지 확인하는 기본 홈 화면
@app.get("/")
async def root():
    return {
        "message": "서버가 정상적으로 실행 중입니다! 🚀",
        "guide": "Swagger UI 문서(테스트 화면)를 보려면 주소창 끝에 /docs 를 입력하세요."
    }