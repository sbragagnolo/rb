initialization
testStickerMarkupArtistIs10
	self assert: (items select: [ :i | i selector type value = 'sticker' ] thenCollect: [ :i | i artistMarkup ]) first equals: 10