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
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_books_genre_true(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_favorites_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_genre_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_book_with_long_name_cant_be_added(self):
        collector = BooksCollector()
        long_name = '1' * 41
        collector.add_new_book(long_name)
        assert collector.books_genre == {}

    def test_set_book_genre_existing_genre_can_be_added_to_book(self):
        collector = BooksCollector()
        collector.add_new_book('Песнь льда и пламени')
        collector.set_book_genre('Песнь льда и пламени', 'Фантастика')
        assert collector.get_book_genre('Песнь льда и пламени') == 'Фантастика'

    def test_get_book_genre_return_correct_genre_after_adding(self):
        collector = BooksCollector()
        name = 'Ревизор'
        book_genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, book_genre)
        getted_genre = collector.get_book_genre(name)
        assert getted_genre == book_genre

    @pytest.mark.parametrize('book_name, book_genre, expected', [
        ['Ревизор', 'Комедии', []],
        ['Песнь льда и пламени', 'Фантастика', ['Песнь льда и пламени']]
    ])
    def test_get_books_with_specific_genre_fantasy_books_returns_correct(self, book_name, book_genre, expected):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_books_with_specific_genre('Фантастика') == expected

    def test_get_books_genre_returns_correct_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        collector.add_new_book('Песнь льда и пламени')
        collector.set_book_genre('Песнь льда и пламени', 'Фантастика')
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        expected_result = {
            'Ревизор': 'Комедии',
            'Песнь льда и пламени': 'Фантастика',
            'Пикник на обочине': 'Фантастика'
        }
        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_returns_books_with_kid_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Теремок')
        collector.set_book_genre('Теремок', 'Мультфильмы')
        collector.add_new_book('Книга Дарьи Донцовой')
        collector.set_book_genre('Книга Дарьи Донцовой', 'Детективы')
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        expected_result = ['Теремок', 'Ревизор']
        assert collector.get_books_for_children() == expected_result

    @pytest.mark.parametrize('name', [
        'Теремок',
        'Ревизор',
        'Песнь льда и пламени'
    ])
    def test_add_book_in_favorites_already_added_book_cant_be_added_again(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Теремок')
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Теремок')
        collector.add_book_in_favorites('Ревизор')
        collector.delete_book_from_favorites('Ревизор')
        assert 'Ревизор' not in collector.favorites

    def test_get_list_of_favorites_books_returns_only_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Теремок')
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Теремок')
        assert collector.get_list_of_favorites_books() == ['Теремок']
