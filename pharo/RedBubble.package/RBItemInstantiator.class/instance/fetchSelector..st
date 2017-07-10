as yet unclassified
fetchSelector: aCollection
	| selector |
	selector := RBProductSelector new.
	selector colour: (self fetchColour: aCollection).
	selector printLocation: (self fetchPrintLocation: aCollection).
	selector size: (self fetchSize: aCollection).
	selector type: (self fetchProductType: aCollection).
	^ selector