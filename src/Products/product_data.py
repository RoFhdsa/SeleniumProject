from dataclasses import dataclass, field


@dataclass
class Products:
    """продукты"""
    product: dict = field(default_factory=lambda:
    {1: {'name': 'Sauce Labs Backpack', 'price': '$29.99',
         'image': 'https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg'},
     2: {'name': 'Sauce Labs Bike Light', 'price': '$9.99',
         'image': 'https://www.saucedemo.com/static/media/bike-light-1200x1500.37c843b0.jpg'},
     3: {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99',
         'image': 'https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c2599ac5.jpg'},
     4: {'name': 'Sauce Labs Fleece Jacket', 'price': '$49.99',
         'image': 'https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg'},
     5: {'name': 'Sauce Labs Onesie', 'price': '$7.99',
         'image': 'https://www.saucedemo.com/static/media/red-onesie-1200x1500.2ec615b2.jpg'},
     6: {'name': 'Test.allTheThings() T-Shirt (Red)', 'price': '$15.99',
         'image': 'https://www.saucedemo.com/static/media/red-tatt-1200x1500.30dadef4.jpg'}
     })