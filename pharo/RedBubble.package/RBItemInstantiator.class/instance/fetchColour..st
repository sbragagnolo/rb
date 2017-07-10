as yet unclassified
fetchColour: aCollection
	^ (aCollection at: #options)
		at: #colour
		ifPresent: [ :value |  RBPropertyContainsCriteria property: #colours value: value ]
		ifAbsent: [ RBAllwaysTruePropertyCriteria instance ]