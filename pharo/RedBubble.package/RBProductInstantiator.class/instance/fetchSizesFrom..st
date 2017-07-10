inflating
fetchSizesFrom: aCollection 
	| options |
	options := aCollection at: #options.
	^ options
		at: #size
		ifPresent: [ :c | 
			c isString
				ifTrue: [ {c} ]
				ifFalse: [ c ] ]
		ifAbsent: [ {} ]