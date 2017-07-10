as yet unclassified
findStrictlyOneProductThatMatches: aCollection 
	^ environment
		findStrictlyOneProductThatMatches:
			(self
				buildSelectorFor:
					(aCollection asDictionary
						at: #options ifAbsentPut: [ Dictionary new ];
						yourself))