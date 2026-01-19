class Invoice:
    def __init__(self, invoice_id, customer_name, amount, tax_rate):
        self.invoice_id = invoice_id              
        self.customer_name = customer_name        
        self._amount = amount                     
        self.tax_rate = tax_rate                  
        self.__is_paid = False                    

    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount > 0:
            self._amount = new_amount
        else:
            raise ValueError("Amount must be positive")


    def calculate_total(self):
        return self._amount * (1 + self.tax_rate)

    
    def mark_as_paid(self):
        self.__is_paid = True

    
    @property
    def is_paid(self):
        return self.__is_paid

