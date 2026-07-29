#书籍类
class Book:
    def __init__(self,book_id,title,author,total_num):
                self.book_id = book_id
                self.title = title
                self.author = author
                self.total_num = total_num

                self.__available_num = total_num

    def borrow_book(self): #借书
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    def return_book(self): #还数
        self.__available_num += 1


    def get_available_num(self):  #获取可用数量
        return self.__available_num


