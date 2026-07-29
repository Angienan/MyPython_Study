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



#会员类
class Member:
    #初始化 方法
    def __init__(self,member_id,name,password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrowed_books = []  #会员借阅书籍列表

    #借书
    def borrow_book(self,book:Book):
        #判断当前会员借阅数量是否最大
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅数量已达最大")
            return False

        #判断书籍是否可借
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}成功借阅了{book.title}")
            return True
        else:
            print(f"{self.name}借阅失败,{book.title}已借完")
            return False


    #还书
    def return_book(self,book:Book):
        #判断书籍是否可还
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name}成功还了{book.title}")
        else:
            print(f"{self.name}还书失败,{book.title}未借阅")


    #get方法
    def get_password(self):
        return self.__password
    def get_borrowed_books(self):
        return self.__borrowed_books
    def get_max_books(self) -> int: #获取最大借阅数量 子类实现
        pass


    #普通会员
class NormalMember(Member):
        #普通会员借阅数量
    def get_max_books(self) -> int:
        return 3


#VIP会员
class VIPMember(Member):
    #初始化方法增加vip会员等级属性
    def __init__(self,member_id,name,password,vip_level):
        super.__init__(member_id,name,password)
        self.vip_level = vip_level

    #获取最大借阅数量6+vip等级
    def get_max_books(self) -> int:
        return 6 + self.vip_level




