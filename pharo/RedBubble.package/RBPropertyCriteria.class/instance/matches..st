testing
matches: aProduct
	| propertyValue |
	propertyValue := self fetchProperty: aProduct.
	^ propertyValue isEmptyOrNil ifTrue: [ self isOptional ] ifFalse: [ self privateSpecializedMatch: propertyValue ]