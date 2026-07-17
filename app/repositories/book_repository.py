from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class BookRepository:

    def create(self, db: Session, book: BookCreate):
        db_book = Book(**book.model_dump())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    def get_all(self, db: Session):
        return db.query(Book).all()

    def get_by_id(self, db: Session, book_id: int):
        return db.query(Book).filter(Book.id == book_id).first()

    def get_by_title(self, db: Session, title: str):
        return db.query(Book).filter(Book.title == title).first()

    def update(
            self,
            db: Session,
            db_book: Book,
            updated_book: BookUpdate
    ):
        updates = updated_book.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(db_book, key, value)

        db.commit()
        db.refresh(db_book)
        return db_book

    def delete(self, db: Session, db_book: Book):
        db.delete(db_book)
        db.commit()


book_repository = BookRepository()
