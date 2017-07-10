initialization
testCartItemsPriceRespectsTheFormule
	cart items
		do: [ :i | 
			self
				assert: (i product basePrice + (i product basePrice * (i artistMarkup / 100))) rounded * i quantity
				equals: i price ]