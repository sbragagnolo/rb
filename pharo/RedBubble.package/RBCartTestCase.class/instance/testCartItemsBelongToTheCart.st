initialization
testCartItemsBelongToTheCart
	self assert: (cart items allSatisfy: [ :i | i cart = cart ])