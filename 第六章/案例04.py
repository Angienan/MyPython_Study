from abc import ABC,abstractmethod
import  json
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

#抽象类:只能被继承,不能被直接实例化,规定子类实现那些方法
#Python中的抽象类: abc模块中的ABC类,-->ABC:Abstrace Base Class
#会员类
class Member(ABC):
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
    #抽象方法中必须实现的方法
    @abstractmethod
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
        super().__init__(member_id,name,password)
        self.vip_level = vip_level

    #获取最大借阅数量6+vip等级
    def get_max_books(self) -> int:
        return 6 + self.vip_level



#图书馆管理系统
class LibrarySystem:

    def __init__(self,):
        self.books = {} #书籍列表
        self.members = {} #会员列表
        self.current_member : Member|None = None

        #加载数据
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        with open("data/books.json","r",encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book["编号"]] = Book(book["编号"],book["标题"],book["作者"],book["数量"])
            print("加载书籍数据成功")


    def load_members_data(self):
        with open("data/members.json","r",encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'].startswith("N") :
                    self.members[member["卡号"]] = NormalMember(member["卡号"],member["姓名"],member["密码"])
                elif member['卡号'].startswith("V") :
                    self.members[member["卡号"]] = VIPMember(member["卡号"],member["姓名"],member["密码"],member["会员等级"])
            print("加载会员数据成功")

#登录
    def login(self):
     while True:
         print("登录")
         member_id = input("请输入会员卡号:")
         password = input("请输入密码:")

         # 判断会员卡是否存在
         if member_id not in self.members:
             print("会员卡不存在")
             continue

         member = self.members[member_id]
         if member.get_password() == password:
             print(f" {member.name} 登录成功")
             self.current_member = member
             return True
         else:
             print("密码错误")
             continue

#借书
    def borrow_book(self):
        #展示图书列表
        for book in self.books.values():
            print(f"编号:{book.book_id} 标题:{book.title} 作者:{book.author} 总数:{book.total_num} 可借数量:{book.get_available_num()}")
        book_id = input("请输入图书编号:")
        if book_id not in self.books:
            print("图书编号不存在")
            return
        self.current_member.borrow_book(self.books[book_id])

#还书
    def return_book(self):
        #展示已借书籍列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("[已借书籍列表]:")
        for book in borrowed_books:
            print(f"编号:{book.book_id} 标题:{book.title}")
        # 获取用户输入的图书编号
        book_id = input("请输入归还图书编号:")
        if book_id not in self.books:
            print("图书编号不存在")
            return
        self.current_member.return_book(self.books[book_id])

#查看已借书籍列表
    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) == 0:
            print("您没有借阅书籍")
        else:
            print("[已借书籍列表]:")
            for book in borrowed_books:
                print(f"编号:{book.book_id} 标题:{book.title}")

#运行
    def run(self):
        print("欢迎来到图书馆管理系统")
        if self.login():
            while True:
                print("\n1.借书")
                print("2.还书")
                print("3.查看已借书籍")
                print("4.退出")
                choice = input("请选择(1-4):")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统")
                        break
                    case _:
                        print("无效的选择,重新选择")


if __name__ == "__main__":
    print("欢迎来到图书馆管理系统")
    library_system = LibrarySystem()
    library_system.run()


