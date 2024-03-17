class Coffee: 
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            if not hasattr(self, '_name') or self._name is None:
                self._name = value
            else:
                raise AttributeError("Cannot change the name of the coffee after instantiation.")
        else:
            raise ValueError("Name must be a string of length 3 or more characters.")
        
    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders_for_coffee = self.orders()
        if orders_for_coffee:
            total_price = sum(order.price for order in orders_for_coffee)
            return total_price / len(orders_for_coffee)
        else:
            return 0

class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError('Name must be a string of length 1 to 15 characters.')

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)  
        return order

    def orders(self):
        return self._orders
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})

class Order:
    def __init__(self, customer, coffee, price):
        self._price = None
        self.price = price
        self.customer = customer
        self.coffee = coffee
        coffee.add_order(self)  

    @property
    def price(self):
        return self._price
    
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            if not hasattr(self, '_price') or self._price is None:
                self._price = price
            else:
                raise AttributeError("Cannot change the price of the order after instantiation.")
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")             