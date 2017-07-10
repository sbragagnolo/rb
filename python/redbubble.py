import abc

"""
    Domain module defines the objects related with the business model.

    Product, Cart, CartItem, ProductSelector.

"""

class Product (object):
    """ docstring for Product. Product is a reification of a sellable product. It works as a DTO  """
    def __init__(self):
        super(Product,self).__init__()
        self.base_price = None
        self.print_locations = None
        self.colours = None
        self.type = None
        self.sizes = None
    def __repr__(self):
        return "<Product type:%s colours:%s sizes:%s>" % (self.type, self.colours, self.sizes)

class CartItem(object):
    """docstring for CartItem."""
    def __init__(self):
        super(CartItem, self).__init__()
        self.quantity = None
        self.artist_markup = None
        self.selector = None
        self.cart = None
    def product(self):
        return self.cart.productFor(self.selector)
    def unit_price(self):
        base = self.product().base_price
        return base + round(base * self.artist_markup / 100)
    def price(self):
        return self.unit_price() * self.quantity
    def __repr__(self):
        return "<CartItem selector:%s quantity:%s artist_markup:%s>" % (self.selector, self.quantity, self.artist_markup)



class Cart(object):
    """docstring for Cart."""
    def __init__(self, environment):
        super(Cart, self).__init__()
        self.items = []
        self.environment = environment
    def add_item(self, item):
        item.cart = self
        self.items.append(item)
    def productFor(self, selector):
        return self.environment.findStrictlyOneProductThatMatches(selector)
    def price(self):
        return sum([item.price() for item in self.items])

"""
    Instantiator objects have the responsibility of inflating objects from the given sources

"""

""" Python does not allow to throw exceptions from lambda expressions, but through the usage of a function """
def raiseException(exception):
    raise exception


class Instantiator(object):
    """docstring for Instantiator."""
    def __init__(self):
        super(Instantiator, self).__init__()
    def __fetchKeyOrDefault(self, jsonObject, key, default, extractor = lambda x: x):
        if(jsonObject.has_key(key)):
            return extractor(jsonObject[key])
        else:
            return default()



class ProductInstantiator(Instantiator):
    """
        docstring for ProductInstantiator.
        For a product is expected to have at least product type and base price.
        The rest of the properties are optional. All of them succeptible to have multiple values.

    """
    def __init__(self):
        super(ProductInstantiator, self).__init__()
    def instantiate(self, jsonObject):
        product = Product()
        product.base_price = self.fetchBasePriceFrom(jsonObject)
        product.colours = self.fetchColoursFrom (jsonObject)
        product.type = self.fetchProductTypeFrom (jsonObject)
        product.sizes = self.fetchSizesFrom (jsonObject)
        product.print_locations = self.fetchPrintLocations (jsonObject)
        return product
    def __fetchKeyOrDefault(self, jsonObject, key, default, extractor = lambda x: x):
        if(jsonObject.has_key(key)):
            return extractor(jsonObject[key])
        else:
            return default()


    def fetchBasePriceFrom(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject, 'base-price', lambda: raiseException(Exception("Base price not found")) )
    def fetchColoursFrom(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject['options'], 'colour', lambda: [] )
    def fetchProductTypeFrom(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject, 'product-type', lambda: raiseException(Exception("Product type not found")) )
    def fetchSizesFrom(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject['options'], 'size', lambda: [] )
    def fetchPrintLocations(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject['options'], 'print-location', lambda: [])




class ItemInstantiator(Instantiator):
    """docstring for ItemInstantiator.

        For an Item is expected to have quantity, artist markup and a product description (called selector)

    """
    def __init__(self):
        super(ItemInstantiator, self).__init__()
    def instantiate(self, jsonObject):
        item = CartItem()
        item.artist_markup = self.fetchArtistMarkup (jsonObject)
        item.quantity = self.fetchQuantity (jsonObject)
        item.selector = self.fetchSelector (jsonObject)
        return item

    def __fetchKeyOrDefault(self, jsonObject, key, default, extractor = lambda x: x):
        if(jsonObject.has_key(key)):
            return extractor(jsonObject[key])
        else:
            return default()
    def fetchArtistMarkup(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject, 'artist-markup', lambda: raiseException(Exception("Artist markup not found")) )
    def fetchQuantity(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject, 'quantity', lambda: raiseException(Exception("Quantity price not found")) )
    def fetchSelector(self, jsonObject):
        selector = ProductSelector()
        selector.colour = self.fetchColour (jsonObject)
        selector.print_location = self.fetchPrintLocation(jsonObject)
        selector.size = self.fetchSize(jsonObject)
        selector.type = self.fetchProductType(jsonObject)
        return selector

    def fetchColour(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject['options'], 'colour', lambda: AlwaysTrueCriteria(), lambda value: ContainsCriteria('colours',value))
    def fetchPrintLocation(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject['options'], 'print-location', lambda: AlwaysTrueCriteria(), lambda value: ContainsCriteria('print_locations', value, True) )
    def fetchSize(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject['options'], 'size',lambda: AlwaysTrueCriteria(), lambda value: ContainsCriteria('sizes',value))
    def fetchProductType(self, jsonObject):
        return self.__fetchKeyOrDefault(jsonObject, 'product-type', lambda: raiseException(Exception("Product type not found")), lambda value: EqualsCriteria('type',value) )




"""
    Criterias are objects that represent a way to query products.

"""

class Criteria(object):
    """docstring for Criteria."""
    def __init__(self):
        super(Criteria, self).__init__()
    def matches(self, product):
        raise Exception("Subclass responsibility")

class AlwaysTrueCriteria(Criteria):
    """docstring for AlwaysTrueCriteria."""
    def __init__(self):
        super(AlwaysTrueCriteria, self).__init__()
    def matches(self, product):
        return True

class ErrorCriteria(Criteria):
    """docstring for AlwaysTrueCriteria."""
    def __init__(self):
        super(ErrorCriteria, self).__init__()
    def matches(self, product):
        raise Exception("All properites must be configured")

class PropertyCriteria(Criteria):
    """docstring for ContainsCriteria."""
    def __init__(self, propertyName, value, optional = False):
        super(PropertyCriteria, self).__init__()
        self.propertyName = propertyName
        self.value = value
        self.optional = optional
    def isOptional(self):
        return self.optional
    def fetchProperty (self, product):
        return getattr(product, self.propertyName)




class EqualsCriteria(PropertyCriteria):
    """docstring for EqualsCriteria."""
    def __init__(self, propertyName, value, optional = False):
        super(EqualsCriteria, self).__init__(propertyName, value, optional)
    def matches(self, product):
        productValue = self.fetchProperty(product)
        if (productValue == None):
            return self.isOptional()
        return self.value == productValue
    def __repr__(self):
        return "<EqualsCriteria property:%s value:%s optional:%s >" % (self.propertyName, self.value, self.isOptional())



class ContainsCriteria(PropertyCriteria):
    """docstring for ContainsCriteria."""
    def __init__(self, propertyName, value, optional = False):
        super(ContainsCriteria, self).__init__(propertyName, value, optional)
    def matches(self, product):
        productValue = self.fetchProperty(product)
        if (productValue == None):
            return self.isOptional()
        if (isinstance(productValue, list) and len(productValue) == 0):
            return self.isOptional()
        return self.value in productValue
    def __repr__(self):
        return "<ContainsCriteria property:%s value:%s optional:%s >" % (self.propertyName, self.value, self.isOptional())


class ProductSelector(object):
    """docstring for ProductSelector. This object is in charge of selecting a product from a CartItem definition """
    def __init__(self):
        super(ProductSelector, self).__init__()
        self.type = ErrorCriteria()
        self.colour = ErrorCriteria()
        self.size = ErrorCriteria()
        self.print_location = ErrorCriteria()
    def matches(self, product):
        return reduce (lambda acc, value: acc and value.matches(product), [self.type , self.colour, self.size, self.print_location ], True)
    def __repr__(self):
        return "<ProductSelector type:%s colour:%s size:%s print_location:%s >" % (self.type.value, self.colour, self.size.value, self.print_location)


class Environment(object):
    """docstring for Environment."""
    def __init__(self, products):
        super(Environment, self).__init__()
        self.products = products
    def findAllProductsThatMatches(self, criteria):
        return [ x for x in self.products if (criteria.matches(x))]
    def findStrictlyOneProductThatMatches(self, criteria):
        result = self.findAllProductsThatMatches(criteria)
        if( len(result) == 0):
            raise Exception('There is no available product for %s ' % criteria)
        if ( len(result) > 1 ):
            raise Exception('There are multiple products for %s ' % criteria)
        return result[0]
