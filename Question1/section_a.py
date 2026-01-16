class Invoice:
    def __init__(self, invoice_id, customer_name, amount, tax_rate):
        self.invoice_id = invoice_id              # public
        self.customer_name = customer_name        # public
        self._amount = amount                     # protected
        self.tax_rate = tax_rate                  # public
        self.__is_paid = False                    # private

    # PROPERTY לקריאה של amount
    @property
    def amount(self):
        return self._amount

    # PROPERTY לכתיבה עם ולידציה
    @amount.setter
    def amount(self, new_amount):
        if new_amount > 0:
            self._amount = new_amount
        else:
            raise ValueError("Amount must be positive")

    # חישוב סכום כולל
    def calculate_total(self):
        return self._amount * (1 + self.tax_rate)

    # שינוי סטטוס תשלום
    def mark_as_paid(self):
        self.__is_paid = True

    # PROPERTY לקריאה בלבד של סטטוס תשלום
    @property
    def is_paid(self):
        return self.__is_paid
