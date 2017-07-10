as yet unclassified
fetchSize: aCollection
	^ (aCollection at: #options)
		at: #size
		ifPresent: [ :value | RBPropertyContainsCriteria property: #sizes value: value ]
		ifAbsent: [ RBAllwaysTruePropertyCriteria instance ]