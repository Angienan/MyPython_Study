class Book :
    def __init__(self,book_id,title,author,total_num):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.available_num = total_num

    def borrow_book(self):
        if self.total_num > 0:
            self.total_num -= 1
            return True
        else:
            return False

    def return_book(self):
        self.total_num += 1

    def get_available_num(self):
        return self.available_num



class Member:
    def __init__(self,member_id,name,password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrowed_books = []

    def borrow_book(self,book:Book):
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅数量已达最大")
            return False

        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}成功借阅了{book.title}")
            return True
        else:
            print(f"{self.name}借阅失败,{book.title}已借完")
            return False

    def return_book(self,book:Book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name}成功还了{book.title}")
        else:
            print(f"{self.name}还书失败,{book.title}未借阅")

    def get_password(self):
        return self.__password
    def get_borrowed_books(self):
        return self.__borrowed_books
    def get_max_books(self) -> int:
        pass



class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3

class VIPMember(Member):
    def __init__(self,member_id,name,password,vip_level):
        super.__init__(member_id,name,password)
        self.vip_level = vip_level
    def get_max_books(self) -> int:
        return 6 + self.vip_level


