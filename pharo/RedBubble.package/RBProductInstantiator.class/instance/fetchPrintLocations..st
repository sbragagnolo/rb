inflating
fetchPrintLocations: aCollection 
	| options |
	options := aCollection at: #options.
	^ options
		at: #'print-location'
		ifPresent: [ :c | 
			c isString
				ifTrue: [ {c} ]
				ifFalse: [ c ] ]
		ifAbsent: [ {} ]