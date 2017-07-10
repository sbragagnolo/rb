initialization
testHoodieMarkupArtistIs20
	self assert: (rawitems select: [ :i | (i at: #'product-type') = 'hoodie' ] thenCollect: [ : i | i at:#'artist-markup']) first equals: 20