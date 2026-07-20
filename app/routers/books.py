from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.book_service import book_service
from app.schemas.book import (
    BookCreate,
    BookUpdate,
    BookResponse
)
from app.utils.exceptions import (
    BookNotFoundException,
    DuplicateBookException,
    InvalidNumberOfPagesException
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.post(
    "",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(
        book: BookCreate,
        db: Session = Depends(get_db)
):
    try:

        return book_service.create_book(
            db,
            book
        )
    except DuplicateBookException as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.get(
    "",
    response_model=list[BookResponse]
)
def get_books(
        db: Session = Depends(get_db)
):
    return book_service.get_books(db)


@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def get_book(
        book_id: int,
        db: Session = Depends(get_db)
):
    try:

        return book_service.get_book(
            db,
            book_id
        )
    except BookNotFoundException as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.put(
    "/{book_id}",
    response_model=BookResponse
)
def update_book(
        book_id: int,
        book: BookUpdate,
        db: Session = Depends(get_db)
):
    try:
        return book_service.update_book(
            db,
            book_id,
            book
        )
    except BookNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except InvalidNumberOfPagesException as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(
        book_id: int,
        db: Session = Depends(get_db)
):
    try:
        book_service.delete_book(
            db,
            book_id
        )
    except BookNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
