
# Table of Contents



Howework at
<https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_1_docker_sql/homework.md>

-   Question 1
    
        docker build --help
        
        -->   --iidfile string  Write the image ID to the file

-   Question 2
    
        docker run -it --entrypoint /bin/bash python:3.9
        pip list
        
        --> 3

-   Prepare Postgres
    
        download green_tripdata_2019-01.csv.gz
        download taxi+_zone_lookup.csv (needed only for Q6?)

-   Question 3
    
        terminal 1: ./start_postgres.sh
        terminal 2: ./pgcli.sh
        
        Open Homework_upload_data.ipynb and run it to upload the data to PostgresSQL.
        DONE. 
        
        in terminal 2:
          select count(1) from green_taxi_data where (DATE(lpep_pickup_datetime) = '2019-01-15' and date(lpep_dropoff_datetime) = '2019-01-15')   
        
        --> 20530

-   Question 4
    
        select lpep_pickup_datetime,trip_distance from green_taxi_data order by trip_distance desc limit 1
        
        --> 2019-01-15

-   Question 5
    
        select passenger_count,count(*) from green_taxi_data where (date(lpep_pickup_datetime) = '2019-01-01' ) group by passenger_count
        
        --> 2: 1282 ; 3: 254

-   Question 6
    
         select zdo."Zone",t.tip_amount from green_taxi_data t join zones zpu on t."PULocationID"=zpu."LocationID" join zones zdo on t."DOLocationID"=zdo."LocationID" where zpu."Zone"='Astoria' orde
        r by t.tip_amount desc limit 1
        
        --> Long Island City/Queens Plaza (tip: 88.0)

Howework at
<https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_1_terraform/homework.md>

-   Question 1
    Already done in `../Terraform+GCP/terraform/.terraform-version`
    
    Needed to change environment variable to:
    
        GOOGLE_APPLICATION_CREDENTIALS=/home/angelv/Learning/DE-Zoomcamp_2023/GCP-keys/de-zoomcamp-375218-5ae85fadc034.json
    
    and file `.terraform-version` to 1.3.7, the installed version in my machine
    
    the Project ID can be obtained from IAM and admin section in GCP
    
        $ terraform apply
        var.project
          Your GCP Project ID
        
          Enter a value: de-zoomcamp-375218
        
        
        Terraform used the selected providers to generate the following execution
        plan. Resource actions are indicated with the following symbols:
          + create
        
        Terraform will perform the following actions:
        
          # google_bigquery_dataset.dataset will be created 
        
        [...]

