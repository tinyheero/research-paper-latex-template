supplemental : suptabs/order.tsv

#----------
# Supplemental Tables
#----------

suptabs/order.tsv : suptabs/catalog.tsv
	python suptabs/reorder-suptabs.py
