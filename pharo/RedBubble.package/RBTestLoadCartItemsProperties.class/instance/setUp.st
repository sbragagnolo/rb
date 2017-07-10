initialization
setUp
	| instantiator |
	super setUp.
	instantiator := RBItemInstantiator new.
	items := rawitems collect: [ :ri | instantiator instantiate: ri ]