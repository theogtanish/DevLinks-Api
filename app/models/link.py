from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tags = Column(String, nullable=True)  # comma-separated for now
    created_at = Column(DateTime, server_default=func.now())