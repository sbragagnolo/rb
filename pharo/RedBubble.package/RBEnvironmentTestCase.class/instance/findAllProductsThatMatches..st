as yet unclassified
findAllProductsThatMatches: aCollection
	^ environment
		findAllProductsThatMatches:
			(self
				buildSelectorFor:
					(aCollection asDictionary
						at: #options ifAbsentPut: [ Dictionary new ];
						yourself))