
class Order:
    x = 0
    priceDict = {'Pizza' : 10, 'Fountain Drink' : 2, 'Salad' : 6, 'Pasta' : 9}
    def __init__(self, orderSelections, userId):
        self.orderSelections = orderSelections
        self.userId = userId
        self.orderNumber = Order.x + 1
        Order.x = Order.x + 1
        self.totalCost = 0
        for i in self.orderSelections:
            self.totalCost = self.totalCost + Order.priceDict[i]
        
    def ChangeOrder(self, removeItem, addItem):
        for index, i in enumerate(self.orderSelections):
            if removeItem == i:
                self.orderSelections.pop(index)
                print('You removed', removeItem, 'from your order')
        if addItem != '':
            self.orderSelections.append(addItem)
            print('You added', addItem, 'to your order')
        print('The new total for your order is: $', self.GetNewCost())

    def GetNewCost(self):
        self.totalCost = 0
        for i in self.orderSelections:
            self.totalCost = self.totalCost + Order.priceDict[i]
        return self.totalCost
    
    def ManageOrder(self):
        print('Your order number is:', self.orderNumber)
        print('You ordered:', self.orderSelections)
        print('Your total is: $', self.totalCost)

    def CancelOrder(self):
        self.orderSelections = 0
        self.totalCost = 0
        print("Your order has been cancelled")

    def PlaceOrder(self):
        print("Thank you for your order! Your order will cost: $", self.GetNewCost())
        o = OrderDelivery(self.orderNumber)
        o.ScheduleDelivery()
        self.GetNewCost()

        ac = AccountCredit(self.userId)
        if ac.DebitBal(self.totalCost) > 0:
            ac.DebitBal(self.totalCost)
            print("Your gift card balance was debited: $", self.totalCost - ac.DebitBal(self.totalCost))
            print("The total after your gift card balance was subtracted is: $", ac.DebitBal(self.totalCost))
            pi = PaymentInfo(self.userId)
            pi.MakePayment(ac.DebitBal(self.totalCost))
        else:
            print("Your gift card balance was debited: $", self.totalCost, ". Your new gift card balance is $", ac.GetBal())
        
class PaymentInfo:
    def __init__(self, userId):
        self.userId = userId

    def addPayment(self, creditNum):
        self.creditNum = creditNum

    def MakePayment(self, totalCost):
        print("Your payment for $", totalCost, "has been processed and approved")

class AccountCredit:
    def __init__(self, userId):
        self.userId = userId
        self.giftCardBal = 25
        self.redeemedGiftCard = {1 : 25.00, 10 : 50.00}

    def GetBal(self):
        return self.giftCardBal
    
    def DebitBal(self, deb):
        if self.giftCardBal - deb < 0:
            return (self.giftCardBal - deb) * -1
            self.giftCardBal = 0
        else:
            self.giftCardBal = self.giftCardBal - deb
            return 0

    def CreditBal(self, cred):
        self.giftCardBal = self.giftCardBal + cred

class OrderDelivery:
    x = 0
    def __init__(self, orderNumber):
        self.deliveryNumber = OrderDelivery.x + 1
        OrderDelivery.x = OrderDelivery.x + 1
        self.orderNumber = orderNumber

    def CheckDelivery(self):
        d = AvailableDelivery()
        self.deliveryInfo = d.GetDelivery()
    
    def ScheduleDelivery(self):
        self.CheckDelivery()
        self.deliveryTime = '1:00 pm'
        self.driver = self.deliveryInfo[self.deliveryTime]
        print("Your order will be delivered at,", self.deliveryTime, "and your driver will be", self.driver)
   
class AvailableDelivery:
    def __init__(self):
        self.deliveryTimes = {'1:00 pm': 'Sean', '1:30 pm': 'Pierre', '2:00 pm': 'Katie'}

    def GetDelivery(self):
        return self.deliveryTimes
 
class Account:
    x = 0
    def __init__(self):
        self.userId = Account.x + 1
        Account.x = Account.x + 1

    def CreateUsername(self, userName):
        self.userName = userName

    def CreatePassword (self, password):
        self.password = password

class main():
    a = Account()
    a.CreateUsername('test')
    a.CreatePassword('test123')
    
    print("Demonstrating the order, payment, available delivery, order delivery, and account credit classes")
    o = Order(['Pizza', 'Fountain Drink', 'Salad'], a.userId)
    o.PlaceOrder()
    
    print("")
    print("Demonstrating how to change, manage, and cancel orders")
    o.ChangeOrder('Pizza', 'Pasta')
    o.ManageOrder()
    o.CancelOrder()
    
main()

        
