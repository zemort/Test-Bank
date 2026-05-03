from random import randint


class RandomNumberGenerator:
    @staticmethod
    def generate_amount_deposit(min_value: int = 1000, max_value: int = 9000) -> int:
        return randint(min_value, max_value)


    @staticmethod
    def generate_amount_transfer(min_value: int = 500, max_value: int = 10000) -> int:
        return randint(min_value, max_value)

    @staticmethod
    def generate_amount_credit(min_value: int = 5000, max_value: int = 15000):
        return randint(min_value, max_value)

    @staticmethod
    def generate_term_months(value=12):
        return value