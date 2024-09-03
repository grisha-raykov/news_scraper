from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Article:
    title: str
    url: str
    content: str
    date_scraped: Optional[datetime] = None
    date_published: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    source: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None

# from sqlalchemy import Column, Integer, String, Text, DateTime
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


# class Article(Base):
#     __tablename__ = "articles"

#     id = Column(Integer, primary_key=True)
#     title = Column(String(255), nullable=False)
#     url = Column(String(255), unique=True, nullable=False)
#     content = Column(Text)
#     date = Column(DateTime)
#     source = Column(String(100))

#     def __repr__(self):
#         return f"<Article(id={self.id}, title='{self.title}', source='{self.source}')>"
