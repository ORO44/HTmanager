import os


class BookList():
    def init(self, path):
        author = os.listdir(path)
        author_path = []
        book_name = []
        book_path = []
        for i in author:
            author_path.append(path + '/' + i)
            book_name = os.listdir(path + '/' + i)
            for k in book_name:
                book_path.append(path + '/' + i + '/' + k)
