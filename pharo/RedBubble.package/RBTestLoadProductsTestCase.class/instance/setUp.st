initialization
setUp 
	super setUp.
	rawproducts :=( NeoJSONReader on: self productClassSourceExample readStream ) next. 