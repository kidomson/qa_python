import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):               #добавление 2х книг
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2      #было assert len(collector.get_books_rating()) == 2

    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['', 'паштет' * 7])
    def test_add_new_book_empty_or_long_name(self, name):          #добавление книги с пустым или слишком длинным именем
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_set_book_genre_installing_the_genre(self):               #установка жанра книги
        collector = BooksCollector()
        collector.add_new_book('Атака титанов')
        collector.set_book_genre('Атака титанов', 'Фантастика')
        assert collector.get_book_genre('Атака титанов') == 'Фантастика'

    def test_set_book_genre_non_existent_genre(self):          #установка несуществующего жанра
        collector = BooksCollector()
        collector.add_new_book('Золотой жук')
        collector.set_book_genre('Золотой жук', 'Несуществующий жанр')
        assert collector.get_book_genre('Золотой жук') == ''

    def test_get_books_with_definite_genre(self):             #получение книги с определенным жанром
        collector = BooksCollector()
        collector.add_new_book('Атака титанов')
        collector.set_book_genre('Атака титанов', 'Фантастика')
        collector.add_new_book('Кошмары')
        collector.set_book_genre('Кошмары', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Атака титанов']

    def test_get_books_genre_getting_dictionary(self):           #получение словаря
        collector = BooksCollector()
        collector.add_new_book('Атака титанов')
        assert collector.get_books_genre() == {'Атака титанов': ''}

    def test_get_books_for_children(self):                  #получение книг для детей
        collector = BooksCollector()
        collector.add_new_book('Атака титанов')
        collector.set_book_genre('Атака титанов', 'Фантастика')
        collector.add_new_book('Кошмары')
        collector.set_book_genre('Кошмары', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Атака титанов' in children_books and 'Кошмары' not in children_books

    def test_add_book_in_favorites_added_to_favorites(self):         #добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book('Атака титанов')
        collector.add_book_in_favorites('Атака титанов')
        assert 'Атака титанов' in collector.favorites

    def test_add_book_in_favorites_adding_non_existent_book_favorites(self):        #добавление несуществующей книги в избранное
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.favorites

    def test_delete_book_from_favorites(self):                   #удаление из избранного
        collector = BooksCollector()
        collector.add_new_book('Атака титанов')
        collector.add_book_in_favorites('Атака титанов')
        collector.delete_book_from_favorites('Атака титанов')
        assert 'Атака титанов' not in collector.favorites

    def test_get_list_of_favorites_books(self):               #получение списка избранных книг
        collector = BooksCollector()
        collector.add_new_book('Атака титанов')
        collector.add_book_in_favorites('Атака титанов')
        assert collector.get_list_of_favorites_books() == ['Атака титанов']