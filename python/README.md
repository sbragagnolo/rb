# rb
RB Interview. 
Python version 

# Getting the code 
	git clone git@github.com:sbragagnolo/rb.git


# Running tests
	
For timing reasons the python version only implements the integration tests. 
For running the tests
		cd python
		python tests.py

This tests contemplates the pairing in between the selection on the cart item description, the price formule respect, the cart total, and the proper spawning of domain objects


# Running examples

The command-line util is defined in the file cmd.py.
for running examples just step into the python folder and execute the cmd.py file

		cd python
		python cmd.py -p ../files/products.json -c ../files/cart-9500.json
		python cmd.py -p ../files/products.json -c ../files/cart-9363.json
		python cmd.py -p ../files/products.json -c ../files/cart-4560.json


for running with some errors, you can use the badly defined products files 

		cd python
		python cmd.py -p ../files/products-no-white-small-hoodie.json -c ../files/cart-9500.json
		python cmd.py -p ../files/products-multiple-white-small-hoodie.json -c ../files/cart-9500.json


Or using wrong parameters

		cd python
		python cmd.py 
		python cmd.py -p no/valid/path -c other/no/valid/path
