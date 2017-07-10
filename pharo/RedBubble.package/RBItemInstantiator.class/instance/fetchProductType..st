as yet unclassified
fetchProductType: aCollection
	^ aCollection
		at: #'product-type'
		ifPresent: [ :value | RBPropertyEqualsToCriteria property: #type value: value ]
		ifAbsent: [ RBAllwaysTruePropertyCriteria instance ]