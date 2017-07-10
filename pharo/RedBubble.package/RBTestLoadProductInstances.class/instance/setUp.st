initialization
setUp
	| loader | 
	super setUp. 
	loader := RBProductInstantiator new. 
	products := rawproducts collect: [ : rp |  loader instantiate: rp  ].