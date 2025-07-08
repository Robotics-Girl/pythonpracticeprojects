class DiscountStrategy: 
    def apply_discount(self, total): 
        return total 
class NoDiscount(DiscountStrategy): 
    def apply_discount(self, total):
        #return total 
        return super().apply_discount(total)
class StudentDiscount(DiscountStrategy): 
    def apply_discount(self, total):
        return 0.9* (super().apply_discount(total))
class BlackFridayDiscount(DiscountStrategy): 
    def apply_discount(self, total):
        return 0.5* (super().apply_discount(total))
class PaymentMethod: 
    def process_payment(self, amount): 
        self.amount = amount 
        print(f"Processing payment of ${self.amount}")
class CreditCard(PaymentMethod): 
    def process_payment(self, amount): 
        super().process_payment(amount)
        print(f"Charges ${amount} to credit card")
class PayPal(PaymentMethod): 
    def process_payment(self, amount): 
        super().process_payment(amount)
        print(f"Processed ${amount} via Paypal")
class Bitcoin(PaymentMethod): 
    def process_payment(self, amount): 
        super().process_payment(amount)
        print(f"Transferred ${amount} in Bitcoin")
class Cart: 
    def __init__(self, discount, payment_method): 
        self.items = []
        self.discount = discount 
        self.payment_method = payment_method
    def add_item(price): 
        self.items.append(price)
    def total_before_discount(self): 
        return sum(self.items)
    def checkout(self): 
        total = self.total_before_discount()
        print(f"Total before discount: ${total}")
        discounted_total = self.discount.apply_discount(total)
        print(f"Amount to pay after discount: ${discounted_total}")
        self.payment_method.process_payment(discounted_total)