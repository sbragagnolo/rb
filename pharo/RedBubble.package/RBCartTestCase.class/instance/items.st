initialization
items
	| loader |
	loader := RBItemInstantiator new.
	^ (NeoJSONReader on: self privateCartExample readStream) next
		collect: [ :rp | loader instantiate: rp ]