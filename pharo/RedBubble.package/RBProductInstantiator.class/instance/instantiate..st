instance creation
instantiate: aCollection 
	| product |
	
	self assert: aCollection isDictionary.
	self assert: aCollection size = 3. 
	product := RBProduct new.
	product basePrice: (self fetchBasePriceFrom: aCollection ).
	product type: (self fetchProductTypeFrom: aCollection ).
	product colours: (self fetchColoursFrom: aCollection ).
	product sizes: (self fetchSizesFrom: aCollection ).
	product printLocations: (self fetchPrintLocations: aCollection ).
	^ product 
	