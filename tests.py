from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_to_books_genre(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        books = collector.get_books_genre()
        assert book_name in books and books[book_name] == ''

    def test_add_new_book_long_name_to_books_genre(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер Гарри Поттер Гарри Поттер Гарри Поттер'
        collector.add_new_book(book_name)
        books = collector.get_books_genre()
        assert book_name not in books

    def test_set_book_genre_true(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_genre()
        assert books[book_name] == genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Опера'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_genre()
        assert books[book_name] != genre

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        book = collector.get_book_genre(book_name)
        assert book == genre

    def test_get_books_with_specific_genre_ret_books(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        book = collector.get_books_with_specific_genre(genre)
        assert book == [book_name]

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        book = collector.get_books_genre()
        assert book == {book_name: genre}

    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()
        book_name_1 = 'Гарри Поттер'
        genre_1 = 'Фантастика'
        book_name_2 = 'Пила'
        genre_2 = 'Ужасы'
        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)
        collector.set_book_genre(book_name_1, genre_1)
        collector.set_book_genre(book_name_2, genre_2)
        book = collector.get_books_for_children()
        assert book == [book_name_1]

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)
        book = collector.get_list_of_favorites_books()
        assert book == [book_name]

    def test_add_book_in_favorites_does_nothing_if_book_not_exists(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        collector.add_book_in_favorites(book_name)
        book = collector.get_list_of_favorites_books()
        assert book_name not in book

    def test_delete_book_from_favorites_books_removes_book(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        book = collector.get_list_of_favorites_books()
        assert book_name not in book

    def test_get_list_of_favorites_books_returns_favorites(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)
        book = collector.get_list_of_favorites_books()
        assert book == [book_name]
