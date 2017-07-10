as yet unclassified
findAllProductsThatMatches: aCriteria
	^ products select: [ : p | aCriteria matches: p ]