initialization
testStickerMarkupArtistIs10
	self assert: (rawitems select: [ :i | (i at: #'product-type') = 'sticker' ] thenCollect: [ : i | i at:#'artist-markup']) first equals: 10