from sqlalchemy.orm import Session
from app.repositories.book_repository import book_repository
from app.utils.logger import logger
from app.schemas.book import BookUpdate
from app.utils.exceptions import (
    BookNotFoundException,
    InvalidNumberOfPagesException,
    DuplicateBookException
)

class BookService:
    def create_book(self, db, book):
        logger.info(
            f"Creating book {book.title}"
        )

        existing_book = (
            book_repository
            .get_by_title(db, book.title)
        )

        if existing_book:
            logger.warning(
                "Duplicate books detected"
            )

            raise DuplicateBookException(
                "Book already exists"
            )

        return book_repository.create(
            db,
            book
        )

    def get_books(
            self,
            db: Session
    ):

        return book_repository.get_all(db)

    def get_book(
            self,
            db: Session,
            book_id: int
    ):

        book = (
            book_repository
            .get_by_id(db, book_id)
        )

        if not book:
            raise BookNotFoundException(
                "Book not found"
            )

        return book

    def update_book(
            self,
            db: Session,
            book_id: int,
            updated_book: BookUpdate
    ):

        book = (
            book_repository
            .get_by_id(db, book_id)
        )

        if not book:
            raise BookNotFoundException(
                "Book not found"
            )

        if (
                updated_book.number_of_pages is not None
                and updated_book.number_of_pages < 0
        ):
            raise InvalidNumberOfPagesException(
                "Pages cannot be negative"
            )

        return book_repository.update(
            db,
            book,
            updated_book
        )

    def delete_book(
            self,
            db: Session,
            book_id: int
    ):

        book = (
            book_repository
            .get_by_id(db, book_id)
        )

        if not book:
            raise BookNotFoundException(
                "Book not found"
            )

        book_repository.delete(
            db,
            book
        )

book_service = BookService()
