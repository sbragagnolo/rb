as yet unclassified
instantiate: aCollection
	| item |
	item := RBCartItem new.
	item artistMarkup: (self fetchArtistMarkup: aCollection).
	item quantity: (self fetchQuantity: aCollection).
	item selector: (self fetchSelector: aCollection).
	^ item