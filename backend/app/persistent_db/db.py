#таблица будет состоять из столбиков: id, user_link, new_link, qr_code, created_at
from sqlalchemy import  Column, UUID, Float, DateTime, Text, LargeBinary
from sqlalchemy.orm import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class Link(Base):
    __tablename__ = "links"
    id = Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    user_link = Column(Text, nullable=False)
    new_link = Column(Text, nullable = False)
    qr_code = Column(LargeBinary)
    created_at = Column(DateTime, default = datetime.utcnow)
