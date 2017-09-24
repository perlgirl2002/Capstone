#!/usr/bin/env python3
"""You can download LANL cyber data using this script."""
from urllib.request import urlretrieve
import sys
import gzip
import shutil

DATA_SETS = ["proc"]

for data in DATA_SETS:
    extracted_file = '{0}.txt'.format(data)
    target_file = extracted_file + '.gz'

    print("Downloading the {0} dataset to {1}.".format(data, target_file),
          file=sys.stderr)
    urlretrieve("http://csr.lanl.gov/data/cyber1/" + target_file, target_file)
    print("Successfully downloaded the {0} dataset.".format(data),
          file=sys.stderr)

    print("Extracting {0} to {1}".format(target_file, extracted_file),
          file=sys.stderr)
    with gzip.open(target_file, 'rb') as infile,\
         open(extracted_file, 'wb') as outfile:
        shutil.copyfileobj(infile, outfile)
    print("Successfully extracted the {0} dataset.".format(data),
          file=sys.stderr)
