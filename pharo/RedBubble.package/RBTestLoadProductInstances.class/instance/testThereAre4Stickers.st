initialization
testThereAre4Stickers
	self assert: (products select: [ :p | p type = 'sticker' ]) size equals: 4