initialization
setUp
	| environment |
	super setUp.
	environment := RBEnvironment new.
	environment products: self products.
	cart := RBCart new.
	cart environment: environment.
	self items do: [ :i | cart addItem: i ]