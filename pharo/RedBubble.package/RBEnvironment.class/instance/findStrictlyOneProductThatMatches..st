as yet unclassified
findStrictlyOneProductThatMatches: aCriteria
	| matches |
	matches := products select: [ :p | aCriteria matches: p ].
	self assert: matches size = 1.
	^ matches first