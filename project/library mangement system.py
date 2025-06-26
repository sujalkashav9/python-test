print("LTSU LIBRAY\n")
class library:
    def _init_(self,bookName,author,issuedate,nameofstduent):
        self.bookName=bookName
        self.author=author
        self.issuedate=issuedate
        self.nameofstduent=nameofstduent

    def display(self):
        return f"Book name is {self.bookName} .It is written by {self.author}"

    def data(self):
        return f"book is issued on{self.issuedate} taken by {self.nameofstduent}"

lb=library("harry_potter","harman","18may","shivansh")
print(lb)
