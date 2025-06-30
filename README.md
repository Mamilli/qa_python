# qa_python
Мария Голуб 24+25 когорта, проект 4 спринта

Реализованые тесты: 
test_add_book_negative_name_book_not_added
-тест c параметризацией проверяет, что книга неподходящим именем( пустое значение, 41 и 59 сивмолов) не добавляется в список

test_add_new_book_not_dublicat
-тест который проверят что невозможно добавить одну и ту же книгу, два раза

test_set_book_genre_actual_book
-тест проверяет установку актуального жанра

test_get_book_genre_book
-тест проверяет получение книги по жанру

test_get_books_with_specific_genre_said_gener
-тест проверят получение списка книг с определенным жанром

test_get_book_genre_received_empty_dictionary
-получение словаря old_collection

test_get_books_for_children_onli_children
-получение книг которые подходят детям

test_add_book_in_favorites_successful_addition
-проверяем что книга добавлена в избранное

test_add_book_in_favorites_dubl
-проверяем что нельзя дважды добавить книгу в избранное

test_delete_book_from_favorites_successfully
-проверяем что книга успешно удалилась

test_get_list_of_favorites_books
-получаем список избранных книг