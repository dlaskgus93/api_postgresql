# func_new/models.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LoraWeightEntity(Base):
    __tablename__ = "lora_weights" # 실제 DB 테이블 이름 확인 후 수정 요망
    # __table_args__ = {"schema": "KIE"}

    weight_id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False)
    registered_at = Column(TIMESTAMP, server_default=func.now())
    updated_by = Column(String(64), nullable=False)