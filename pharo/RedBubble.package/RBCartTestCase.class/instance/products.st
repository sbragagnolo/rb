initialization
products
	| loader |
	loader := RBProductInstantiator new.
	^ (NeoJSONReader on: self productClassSourceExample readStream) next
		collect: [ :rp | loader instantiate: rp ]