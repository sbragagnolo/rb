initialization
testHoodieMarkupArtistIs20
	self assert: (items select: [ :i | i selector type value = 'hoodie' ] thenCollect: [ :i | i artistMarkup ]) first equals: 20