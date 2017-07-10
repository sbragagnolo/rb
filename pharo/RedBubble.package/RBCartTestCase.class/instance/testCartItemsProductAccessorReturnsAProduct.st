initialization
testCartItemsProductAccessorReturnsAProduct
	self assert: (cart items allSatisfy: [ :i | i product isRBProduct ])