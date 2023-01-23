#!/bin/bash

docker run -it --rm \
       --network=pg-network \
       taxi_ingest:v001 \
         --user=root \
         --password=root \
         --host=pg-database \
         --port=5432 \
         --db=ny_taxi \
         --table_name=yellow_taxi_trips \
         --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
