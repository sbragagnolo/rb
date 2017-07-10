inflating
fetchColoursFrom: aCollection
	| options |
	options := aCollection at: #options.
	^ options
		at: #colour
		ifPresent: [ :c | 
			c isString
				ifTrue: [ {c} ]
				ifFalse: [ c ] ]
		ifAbsent: [ {} ]