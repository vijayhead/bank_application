class Bank:
    
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def debit(self,amount):
        self.__amount = amount
        if self.__amount < self.__balance:
            self.__balance = self.__balance-self.__amount
            return f"Rs.{self.__amount}/- is Debited"
        else:
            return "Insufficent Balance"
    
    def credit(self,amount):
        self.__amount = amount
        self.__balance = self.__balance + self.__amount
        return f"Rs.{self.__amount}/- is Credited"
    
    def show_balance(self):
        return f"Your A/c Balance is {self.__balance}/-"

user1 = Bank("Vijay",5000)
user2 = Bank("Gaurav",10000)

user1.debit(3000)
user2.credit(4000)
print(user1.show_balance())
print(user2.show_balance())