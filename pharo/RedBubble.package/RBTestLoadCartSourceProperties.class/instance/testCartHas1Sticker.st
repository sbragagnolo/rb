initialization
testCartHas1Sticker
	self assert: (rawitems select: [ :i | (i at: #'product-type') = 'sticker' ]thenCollect:[: i | i at: #quantity ]) first equals: 1