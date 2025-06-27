import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def old_collection():
    collection = BooksCollector()
    collection.books_genre = {'Книга_1':'Фантастика', 'Книга_2':'Детективы', 'Книга_3':'Мультфильмы'}

    return collection