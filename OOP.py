# Task 1
class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        if isinstance(self, Student):
            return "{}.{}.1@btu.edu.ge".format(self.firstname, self.lastname)
        if isinstance(self, Lecturer):
            return "{}.{}@btu.edu.ge".format(self.firstname, self.lastname)


class Student(People):
    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.courses = courses
        courses = ["python", "kotlin", "java", "html", "css"]


class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary


object1 = Lecturer("lika", "svanadze", 2000)
object2 = Student("Dachi", "Avkopashvili", "python")
print(object1.get_email())
print(object2.get_email())

# Task 2
class LibraryItem:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == "available":
            print("Successful booking")
        elif self.status == "occupied" or isinstance(self, CD):
            print("Unsuccessful booking")


class Book(LibraryItem):
    def __init__(self, ISBN, authors, title, subject, status):
        super().__init__(title, subject, status)
        self.ISBN = ISBN
        self.authors = authors


class CD(LibraryItem):
    def __init__(self, title, status):
        LibraryItem.__init__(self, title, status, 1)


class Magazine(LibraryItem):
    def __init__(self, journalName, volume, status):
        LibraryItem.__init__(self, 1, 1, status)
        self.journalName = journalName
        self.volume = volume


obj1 = Magazine("saxeli", 1000, "available")
obj2 = CD("saxeli", "available")

obj1.booking()
obj2.booking()

# Task 3
class Contacts:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class MailSender:
    def send_mail(self):
        return "თქვენი მეილი გაიგზავნა ამ მისამართზე: {}".format(self.email)


class Friend(Contacts, MailSender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email


class Family(Contacts, MailSender):
    def __init__(self, name, phone, email, birthdate):
        super().__init__(name, phone)
        self.email = email
        self.birthdate = birthdate




obj1 = Family("dachi", "5579799xx", "dachi.avkopashvili@btu.edu.ge", "29/10/2002")
obj2 = Friend("nika", "555xxxyyy", "nika@gmail.com")

print(obj1.send_mail())
print(obj2.send_mail())

# Task 4
class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        if isinstance(self, Student):
            return "{}.{}.1@btu.edu.ge".format(self.firstname, self.lastname)
        if isinstance(self, Lecturer):
            return "{}.{}@btu.edu.ge".format(self.firstname, self.lastname)


class Student(People):
    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.courses = courses
        courses = ["python", "kotlin", "java", "html", "css"]


class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        self.salary = salary
        super().__init__(firstname, lastname)


class Doctoral_student(Lecturer, Student):
    def __init__(self, firstname, lastname, courses, salary):
        super().__init__(firstname, lastname, salary)
        super().__init__(firstname, lastname, courses)

    def get_email(self):
        if isinstance(self, Student):
            return "{}.{}.1@btu.edu.ge".format(self.firstname, self.lastname)
        if isinstance(self, Lecturer):
            return "{}.{}@btu.edu.ge".format(self.firstname, self.lastname)


object1 = Lecturer("lika", "svanadze", 2000)
object2 = Student("Dachi", "Avkopashvili", "python")
print(object1.get_email())
print(object2.get_email())