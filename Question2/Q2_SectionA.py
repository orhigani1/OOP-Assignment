

class Security:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_value(self):
        return self.price * self.quantity
    
    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")



class Stock(Security):
    def __init__(self, name, price, quantity, dividend):
        super().__init__(name, price, quantity)
        self.dividend = dividend
    
    def calculate_dividend_income(self):
        return self.quantity * self.dividend



class Bond(Security):
    def __init__(self, name, price, quantity, interest_rate):
        super().__init__(name, price, quantity)
        self.interest_rate = interest_rate
    
    def calculate_annual_interest(self):
        return self.get_total_value() * self.interest_rate / 100



class Option(Security):
    def __init__(self, name, price, quantity, strike_price):
        super().__init__(name, price, quantity)
        self.strike_price = strike_price
    
    def calculate_intrinsic_value(self):
        return max(0, self.price - self.strike_price)



stock = Stock("AAPL", 150, 10, 5)
bond = Bond("Government Bond", 1000, 5, 3.5)
option = Option("Call Option", 50, 20, 45)

print("=== Stock Information ===")
stock.display_info()
print(f"Total Value: {stock.get_total_value()}")
print(f"Dividend Income: {stock.calculate_dividend_income()}\n")

print("=== Bond Information ===")
bond.display_info()
print(f"Total Value: {bond.get_total_value()}")
print(f"Annual Interest: {bond.calculate_annual_interest()}\n")

print("=== Option Information ===")
option.display_info()
print(f"Total Value: {option.get_total_value()}")
print(f"Intrinsic Value: {option.calculate_intrinsic_value()}")

