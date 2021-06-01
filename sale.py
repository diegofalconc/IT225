import datetime

class Sale():
    def __init__(self, status, totalPrice):
        self.items=[]
        self.dateCreated=datetime.date.today()
        self.status = status
        self.totalPrice = totalPrice

    def getPrice(self):
        return self.totalPrice

    def getStatus(self):
        return self.status

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def getItem(self, item):
        return self.items[item]

    def getItems(self):
        return self.items 

    def getDate(self):
        return self.dateCreated

sae = Sale('active', 20)

sae.addItem(1)
sae.addItem(2)

print(sae.getItems())

