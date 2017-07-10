initialization
testThereIs1Leggings
	self assert: (products select: [ :p | p type = 'leggings' ]) size equals: 1