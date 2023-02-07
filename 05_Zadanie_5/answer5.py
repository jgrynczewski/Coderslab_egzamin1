from exam_lib import Book


class EBook(Book):
    def __init__(self, title, author, pages, size, registration_code):
        self.size = size
        if self.check_code(registration_code):
            self._registration_code = registration_code
        else:
            self._registration_code = None
        super().__init__(title, author, pages)

    @staticmethod
    def check_code(code):
        if type(code) == str and len(code) == 16:
            return True
        return False

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, new_code):
        if self.check_code(new_code):
            self._registration_code = new_code
