import unittest
import redbubble

"""
def productsExample():
    return [{"product-type": "hoodie","options": {"colour": ["white", "dark"],"size": ["small", "medium"]},"base-price": 3800},{"product-type": "hoodie","options": {"size": "large","colour": "white"},"base-price": 3848},{"product-type": "hoodie","options": {"colour": "white","size": ["xl", "2xl", "3xl"]},"base-price": 4108},{"product-type": "hoodie","options": {"colour": "dark","size": "large"},"base-price": 4212},{"product-type": "hoodie","options": {"colour": "dark","size": ["xl", "2xl", "3xl"]},"base-price": 4368},{"product-type": "sticker","options": {"size": "small"},"base-price": 221},{"product-type": "sticker","options": {"size": "medium"},"base-price": 583},{"product-type": "sticker","options": {"size": "large"},"base-price": 1000},{"product-type": "sticker","options": {"size": "xl"},"base-price": 1417},{"product-type": "leggings","options": {},"base-price": 5000}]
def cartExample():
    return  [{"product-type": "hoodie", "options": { "size": "small",  "colour": "dark", "print-location": "front"  },  "artist-markup": 20,  "quantity": 2},{  "product-type": "sticker",  "options": { "size": "small"  },  "artist-markup": 10,  "quantity": 1} ]
def products():
    instanciator = redbubble.ProductInstantiator()
    return map(lambda jp: instanciator.instantiate(jp), productsExample())
def items():
    instanciator = redbubble.ItemInstantiator()
    return map(lambda jp: instanciator.instantiate(jp), cartExample())
environment = redbubble.Environment(products())
cart = redbubble.Cart(environment)
[ cart.add_item(item) for item in items() ]
"""

class TestCart (unittest.TestCase):
    def productsExample(self):
        return [{"product-type": "hoodie","options": {"colour": ["white", "dark"],"size": ["small", "medium"]},"base-price": 3800},{"product-type": "hoodie","options": {"size": "large","colour": "white"},"base-price": 3848},{"product-type": "hoodie","options": {"colour": "white","size": ["xl", "2xl", "3xl"]},"base-price": 4108},{"product-type": "hoodie","options": {"colour": "dark","size": "large"},"base-price": 4212},{"product-type": "hoodie","options": {"colour": "dark","size": ["xl", "2xl", "3xl"]},"base-price": 4368},{"product-type": "sticker","options": {"size": "small"},"base-price": 221},{"product-type": "sticker","options": {"size": "medium"},"base-price": 583},{"product-type": "sticker","options": {"size": "large"},"base-price": 1000},{"product-type": "sticker","options": {"size": "xl"},"base-price": 1417},{"product-type": "leggings","options": {},"base-price": 5000}]
    def cartExample(self):
        return  [{"product-type": "hoodie", "options": { "size": "small",  "colour": "dark", "print-location": "front"  },  "artist-markup": 20,  "quantity": 2},{  "product-type": "sticker",  "options": { "size": "small"  },  "artist-markup": 10,  "quantity": 1} ]
    def products(self):
        instanciator = redbubble.ProductInstantiator()
        return map(lambda jp: instanciator.instantiate(jp), self.productsExample())
    def items(self):
        instanciator = redbubble.ItemInstantiator()
        return map(lambda jp: instanciator.instantiate(jp), self.cartExample())
    def setUp(self):
        self.environment = redbubble.Environment(self.products())
        self.cart = redbubble.Cart(self.environment)
        [ self.cart.add_item(item) for item in self.items() ]
    def test_cart_items_belong_to_the_cart(self):
        self.assertTrue(reduce ( lambda acc, i: acc and i.cart == self.cart, self.cart.items, True))

    def test_product_accessor_fetches_product(self):
        self.assertTrue(reduce ( lambda acc, i: acc and isinstance(i.product(), redbubble.Product), self.cart.items, True))

    def test_cart_item_respects_formule(self):
        formule = lambda item: (item.product().base_price + round(item.product().base_price * item.artist_markup / 100)) * item.quantity
        self.assertTrue(reduce ( lambda acc, i: acc and i.price() == formule(i),  self.cart.items, True))
    def tests_cart_total_is_as_expected(self):
        smallStickerPrice = 1 * (221 + round(221 * 0.1) )
        smallDarkHoodiesPrice = 2 * (3800 + round(3800 * 0.2))
        self.assertEquals(self.cart.price(), smallStickerPrice + smallDarkHoodiesPrice)

if __name__ == '__main__':
    unittest.main()
