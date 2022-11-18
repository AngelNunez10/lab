import pytest
from account import *

class Test():
    def setup_method(self):
        self.p1 = Account('John')
        self.p2 = Account('Angel')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p2.get_name() == 'Angel'

        assert self.p1.get_balance() == 0
        assert self.p1.get_balance() == 0


    def test_deposit(self):

        assert self.p1.deposit(30) == True
        assert self.p1.get_balance() == 30

        assert self.p1.deposit(-10) == False
        assert self.p1.get_balance() == 30

        assert self.p2.deposit(5.0) == True
        assert self.p2.get_balance() == 5.0

        assert self.p2.deposit(0) == False
        assert self.p2.get_balance() == 5.0



    def test_withdraw(self):
        assert self.p1.deposit(15) == True
        assert self.p1.get_balance() == 15
        assert self.p1.withdraw(30) == False
        assert self.p1.get_balance() == 15

        assert self.p1.withdraw(-10) == False
        assert self.p1.get_balance() == 15

        assert self.p2.deposit(20) == True
        assert self.p2.withdraw(5.0) == True
        assert self.p2.get_balance() == 15.0

        assert self.p2.withdraw(0) == False
        assert self.p2.get_balance() == 15.0

