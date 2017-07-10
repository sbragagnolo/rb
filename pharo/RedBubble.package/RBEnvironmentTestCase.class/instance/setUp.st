initialization
setUp
	super setUp.
	environment := RBEnvironment new.
	environment products: self products.

