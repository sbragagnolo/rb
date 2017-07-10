# rb
RB Interview. 
Multiple implementations.


# Requirements

Create a simple price calculator command-line program. In order to make this exercise programming language agnostic, the inputs and outputs are defined as JSON.

    Your command-line program should take two arguments:
        a file representing a cart, and
        a file representing a list of base prices.
    The cart schema is available at: /cart.schema.json.
    The base price schema is available at: /base-prices.schema.json.
    You can assume that the options keys for a product-type are constant.
    For example, if the first record with the product-type 'hoodie' in the list of base prices only consists of the options keys 'colour' and 'size', all records with the product-type 'hoodie' will only have the options keys 'colour' and 'size'.
    The price calculation for one item is as follows: (base_price + round(base_price * artist_markup)) * quantity
    Your program is expected to output the total price in cents followed by a newline character.
    An example of base prices is available at: /base-prices.json.
    Some example carts are available at: /cart-4560.json, /cart-9363.json, /cart-9500.json, and /cart-11356.json.
    The file name includes the expected output for the above-mentioned example base prices.

Important notes:

    We currently have more than 1,000 base prices. Make sure the running time of the base price lookup is constant.
    Write tested, production-quality code.
    Make sure a human can understand how to run your program.
    You will extend this program in subsequent interview steps.





# Possible Designs


## Design 1: 
	
Products and item as first citizen. Each object has well known static properties: Easier to debug, predictable behaviour. Easy to test.
The product description is spawned as a selector, an object capable to understand if it matches with a given product.

The items know their cart. A cart works as a scope for looking up products.
The cart inside an environment, to fetch products as well and to solve non-functional technical problems as configuration.


## Design 2: 

Products and item as first citizen. Each object has dynamic properties: Harder to debug or predict. Needs exahustive testing for unexepected cases.
The product description is spawned as a selector, an object capable to understand if it matches with a given product.

The items know their cart. A cart works as a scope for looking up products.
The cart inside an environment, to fetch products as well and to solve non-functional technical problems as configuration.



## Design 3: 
	
Products and item as dictionary (hashed tables) or basic dto json wobjects. Each object has dynamic properties: Harder to debug or predict. 
Needs exahustive testing for unexepected cases.
The responsibility of matching in between products is a specfic kind of stream that does the magic. Harder to specialize or diversify behaviours.

All the coding API is implemented at the level of the execution environment, where the configuration is solved as well. Simpler to code, harder to understand doubt to the lack of domain representation. 

# Chosen design
	
Since the first language used for this development was Pharo, language that provides a powerful TDD interface, in order to have a dynamic approach for the prototyping, I took the first proposed design. 
	
With my current knowledge of the domain, there is not really a solution that is really better than the other two. For making a better decision I should have clear understanding of the system that uses the proposed excercise.
	

# Architecture 

## Architecture - library
Provide a simple controler-like object (facade), with a minimal API based on the requirements: given two files, calculate the price of the cart. 
This facade object may work as environment, where well known datasources may be accessed, when there is need for data.


## Architecture - command line
Provide a simple facade object that allows to access to the library facade features, inside a secure are, with some different kind strategy of error handling.


















