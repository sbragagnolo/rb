initialization
testThere6SizesOfHoodies
	self assert: ((products select: [ :p | p type = 'hoodie' ]) flatCollectAsSet: [ :p | p sizes ]) asSet size equals: 6