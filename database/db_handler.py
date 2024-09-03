from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.article import Base, Article


class DatabaseHandler:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def insert_article(self, title, url, content, date, source):
        article = Article(
            title=title, url=url, content=content, date=date, source=source
        )
        try:
            self.session.add(article)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"Error inserting article: {str(e)}")

    def close_connection(self):
        self.session.close()
