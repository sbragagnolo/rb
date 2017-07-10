as yet unclassified
unitPrice
	| base |
	base := self product basePrice.
	^ base + (base * artistMarkup / 100) rounded