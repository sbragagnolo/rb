as yet unclassified
fetchPrintLocation: aCollection
	^ (aCollection at: #options)
		at: #'print-location'
		ifPresent: [ :value | 
			(RBPropertyEqualsToCriteria property: #printLocations value: value)
				beOptional;
				yourself ]
		ifAbsent: [ RBAllwaysTruePropertyCriteria instance ]