
class Account:
    """
    A class representing details for an account object
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to set default values for an account object
        :param name: Accounts name
        """
        self.__account_name = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to increase the account balance
        :param amount: The amount to increase
        :return: True if successful, False if unsuccessful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to decrease the account balance
        :param amount: The amount to decrease
        :return: True if successful, False if unsuccessful
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Method to access an accounts balance
        :return: Account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access an accounts name
        :return: Account name
        """
        return self.__account_name


if __name__ == '__main__':
    pass