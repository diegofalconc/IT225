import unittest
from sale import Sale
from customer import Customer
import datetime

class TestSale(unittest.TestCase):
    def setUp(self):
        self.s = Sale('active', 20)
    
    def test_totalprice(self):
        self.assertEqual(int(self.s.getPrice()), 20)
    
    def test_status(self):
        self.assertEqual(str(self.s.getStatus()), 'active')
    
    def test_datecreated(self):
        self.assertEqual(self.s.getDate(), datetime.date.today())

    def test_addItem(self):
        self.s.addItem(2)
        self.assertEqual(self.s.getItem(0), 2)

    def test_removeItem(self):
        self.s.addItem(3)
        self.s.addItem(2)
        self.s.addItem(1)
        self.assertEqual(self.s.getItem(0), 3)
        self.s.removeItem(3)
        self.assertEqual(self.s.getItem(0), 2)

    def test_getItems(self):
        self.s.addItem(3)
        self.s.addItem(2)
        self.s.addItem(1)
        self.assertEqual(self.s.getItems(), [3,2,1])


class Test_Customer(unittest.TestCase):
    def setUp(self):
        self.c = Customer('Joe', '2132-avenue-6', 'joedoe@hotmail.com', 213)

    def test_getCustomerName(self):
        self.assertEqual(self.c.getCustomerName(), 'Joe')

    def test_getAddress(self):
        self.assertEqual(self.c.getAddress(), '2132-avenue-6')

    def test_getMembershipCardID(self):
        self.assertEqual(self.c.getMembershipCardId(), 213)

    def test_getEmail(self):
        self.assertEqual(self.c.getEmail(), 'joedoe@hotmail.com')