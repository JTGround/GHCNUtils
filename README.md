## Description
This repository provides a basic framework to access and
manipulate the National Weather Service's Global Historical Climatology Network dataset. 
The GHCN dataset contains decades of daily climate records from over 100,000 stations.

## The Dataset  
This package handles the stations, countries, states, 
and the "daily" climate files (and their respective schemas and types) that can be  found at the following source:  

The summary and main search page:  
https://www.ncei.noaa.gov/access/search/datasets/daily-summaries/  

Bulk download:  
S3 Bucket: https://noaa-ghcn-pds.s3.amazonaws.com/index.html  
Direct Download: https://www.ncei.noaa.gov/pub/data/ghcn/daily/  


## File type conversions
The original fixed-width files can be converted to CSV, GEOJSON file types for easier manipulation.
```
from pathlib import Path
from ghcn_utils import stations_copy_to_csv, dly_copy_to_csv

stations_source = Path("C:/ghcnd-download/ghcnd-stations.txt")
stations_copy_to_csv(stations_source)

dly_source = Path("C:/ghcnd-download/ghcnd-stations.txt")
dly_copy_to_csv(dly_source)
```


# Load data into MySql

### Convert txt to csv
convert_countries_csv(source_path, target_path, delete_source)

### Load data into table
LOAD DATA INFILE '/path/to/ghcnd-countries.csv' INTO TABLE GHCN.countries;

must disable --secure-file-priv variable in my.cnf to 'Load Data Infile'