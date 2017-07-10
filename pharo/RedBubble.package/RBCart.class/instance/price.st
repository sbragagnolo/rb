as yet unclassified
price
	^ items inject: 0 into: [ :acc :item | acc + item price ]