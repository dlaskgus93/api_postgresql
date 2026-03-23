# app/core/config.py (또는 core/config.py)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # 1. .env 파일에 적어둔 키(Key) 이름과 똑같이 변수명을 적어줍니다.
    # Pydantic이 알아서 .env를 읽어서 이 변수들에 값을 채워 넣습니다!
    POSTGRES_HOST: str
    POSTGRES_PORT: int  # .env에는 글자("5432")로 적혀있어도 알아서 숫자로 바꿔줍니다!
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # 2. Settings 클래스의 환경 설정 (어느 파일에서 값을 읽어올지 지정)
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" # .env에 적혀있지만 여기 클래스에 없는 값은 무시하라는 뜻입니다.
    )

# 3. 프로젝트 전체에서 돌려 쓸 수 있도록 객체를 딱 하나만 생성해 둡니다. (싱글톤 패턴)
settings = Settings()