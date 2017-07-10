initialization
testThere2ColoursOfHoodies
	self assert: ((products select: [ :c | c type = 'hoodie' ]) flatCollectAsSet: [ :c | c colours ]) asSet size equals: 2