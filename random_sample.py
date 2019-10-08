import numpy as np
from astropy.table import Table

cat = Table.read('Catalogs/non_mergers.csv')

rows = np.random.randint(0, len(cat)-1, 9000)

new_cat = cat[rows]
Table.write(new_cat, 'Catalogs/non_mergers_subset.csv')
