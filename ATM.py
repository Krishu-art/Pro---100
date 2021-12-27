class ATM(object):
 def __init__(self, CardNumber, PinNumber):
     self.CardNumber = CardNumber
     self.PinNumber = PinNumber

 def BalanceEnquiry(self):
     print("Your Account Balance is 1,00,000")

 def CashWithdrawl(self,amount):
     new_amount = 1,00,000 - amount
     print("You have  CashWithdrawn amount"+str(amount) +". Your remaining balance is "+ str(new_amount))
     
def main():
     
     
     CardNumber = input("Enter your CardNumber:-")
     PinNumber = input("Enter your PinNumber:-")

     new_user = ATM(CardNumber, PinNumber)

     print("Choose your Activity")
     print("1.BalanceEnquiry 2.CashWithdrawl")
     Activity = int(input("Enter the Acitivity Number:-"))

     if (Activity == 1):
         new_user.BalanceEnquiry()
     elif (Activity == 2):
         amount =  int(input("Enter the amount of CashWithdrawl you wanna do:-"))
         new_user.CashWithdrawl(amount)
     else:
         print("enter Valid Number")
         
     
if __name__ == "__main__":
    main()    

     
     
