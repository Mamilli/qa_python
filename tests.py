import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

@pytest.mark.parametrize('name',[
        '',
        'Увлекательная_книга_про_микро_организмы_в',
        'Увлекательная_книга_про_микроорганизмы_в_коде_разработчиков'
    ])
    def test_add_book_negative_name_book_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_book_genre()) == 0, 'Нельзя добавить книгу с недопустимым названием'

    def test_add_new_book_not_dublicat(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_new_book('Библия')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_actual_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.books_genre['Шерлок Холмс'] == 'Детективы'

    def test_get_book_genre_book(self):
        collector = BooksCollector()
        collector.add_new_book('Эркюль Пуаро')
        collector.get_book_genre('Эркюль Пуаро', 'Детективы')
        assert collector.get_books_genre('Эркюль Пуаро') == 'Детективы'

    def test_get_books_with_specific_genre_said_gener(self):
        collector = BooksCollector()
        collector.add_new_book('Синяя птица')
        collector.set_book_genre('Синяя птица','Фантастика')
        collector.add_new_book('Старик Хоттабыч')
        collector.set_book_genre('Старик Хоттабыч','Комедии')

        assert collector.get_books_with_specific_genre('Комедии') == ['Старик Хоттабыч']

    def test_get_book_genre_received_empty_dictionary(self, old_collection):

        assert old_collection.get_books_genre() == {}

    def test_get_books_for_children_onli_children(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Хелло Китти')
        collector.set_book_genre('Хелло Китти','Мультфильмы')
        collector.add_new_book('Ночь на улице Вязов')
        collector.set_book_genre('Ночь на улице Вязов', 'Ужасы')

        return collector.get_books_for_children() == ['Хелло Китти']

    def test_add_book_in_favorites_successful_addition(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Кролик Питер')
        collector.set_book_genre('Кролик Питер','Мультфильмы')
        collector.add_book_in_favorites('Кролик Питер')
        assert collector.favorites ==['Кролик Питер']

    def test_add_book_in_favorites_dubl(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Машины сказки')
        collector.set_book_genre('Машины сказки','Мультфильмы')
        collector.add_book_in_favorites('Машины сказки')
        collector.add_book_in_favorites('Машины сказки')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_successfully(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец','Фантастика')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Валькирия')
        collector.add_book_in_favorites('Валькирия')
        assert collector.favorites == collector.get_list_of_favorites_books()