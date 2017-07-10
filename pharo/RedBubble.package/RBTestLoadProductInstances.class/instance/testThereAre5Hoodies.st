initialization
testThereAre5Hoodies
	self assert: (products select: [ :p | p type = 'hoodie' ]) size equals: 5