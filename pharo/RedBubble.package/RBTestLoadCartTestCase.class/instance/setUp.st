initialization
setUp
	super setUp.
	rawitems := (NeoJSONReader on: self privateCartExample readStream) next