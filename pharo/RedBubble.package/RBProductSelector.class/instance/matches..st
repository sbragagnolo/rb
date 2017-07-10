accessing
matches: aProduct
	^ {type.
	colour.
	size.
	printLocation} allSatisfy: [ :c | c matches: aProduct ]