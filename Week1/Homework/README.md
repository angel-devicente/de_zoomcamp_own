
# Table of Contents



Howework at
<https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_1_docker_sql/homework.md>

-   Question 1
    
    docker build &#x2013;help
    
    &#x2013;>   &#x2013;iidfile string  Write the image ID to the file

-   Question 2
    
    docker run -it &#x2013;entrypoint /bin/bash python:3.9
    pip list
    
    &#x2013;> 3

-   Prepare Postgres
    
    download green<sub>tripdata</sub><sub>2019</sub>-01.csv.gz
    download taxi+<sub>zone</sub><sub>lookup.csv</sub> (needed only for Q6?)

-   Question 3
    terminal 1: ./start<sub>postgres.sh</sub>
    terminal 2: ./pgcli.sh
    
    Open Homework<sub>upload</sub><sub>data.ipynb</sub> and run it to upload the data to PostgresSQL.
    DONE. 
    
    in terminal 2:
      select count(1) from green<sub>taxi</sub><sub>data</sub> where (DATE(lpep<sub>pickup</sub><sub>datetime</sub>) = '2019-01-15' and date(lpep<sub>dropoff</sub><sub>datetime</sub>) = '2019-01-15')   
    
    &#x2013;> 20530

-   Question 4
    select lpep<sub>pickup</sub><sub>datetime,trip</sub><sub>distance</sub> from green<sub>taxi</sub><sub>data</sub> order by trip<sub>distance</sub> desc limit 1
    
    &#x2013;> 2019-01-15

-   Question 5
    select passenger<sub>count,count</sub>(\*) from green<sub>taxi</sub><sub>data</sub> where (date(lpep<sub>pickup</sub><sub>datetime</sub>) = '2019-01-01' ) group by passenger<sub>count</sub>
    
    &#x2013;> 2: 1282 ; 3: 254

-   Question 6
     select zdo."Zone",t.tip<sub>amount</sub> from green<sub>taxi</sub><sub>data</sub> t join zones zpu on t."PULocationID"`zpu."LocationID" join zones zdo on t."DOLocationID"=zdo."LocationID" where zpu."Zone"`'Astoria' orde
    r by t.tip<sub>amount</sub> desc limit 1
    
    &#x2013;> Long Island City/Queens Plaza (tip: 88.0)

Howework at
<https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_1_terraform/homework.md>

-   Question 1
    Already done in ../Terraform+GCP/terraform/.terraform-version
    
    Needed to change environment variable to:
    GOOGLE<sub>APPLICATION</sub><sub>CREDENTIALS</sub>=/home/angelv/Learning/DE-Zoomcamp<sub>2023</sub>/GCP-keys/de-zoomcamp-375218-5ae85fadc034.json
    
    and file .terraform-version to 1.3.7, the installed version in my machine
    
    the Project ID can be obtained from IAM and admin section in GCP
    
    ,-&#x2014;
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">$ terraform apply</td>
    </tr>
    
    
    <tr>
    <td class="org-left">var.project</td>
    </tr>
    
    
    <tr>
    <td class="org-left">Your GCP Project ID</td>
    </tr>
    
    <tbody>
    <tr>
    </tr>
    </tbody>
    
    
    <tr>
    <td class="org-left">Enter a value: de-zoomcamp-375218</td>
    </tr>
    
    <tbody>
    <tr>
    </tr>
    </tbody>
    
    <tbody>
    <tr>
    </tr>
    </tbody>
    
    
    <tr>
    <td class="org-left">Terraform used the selected providers to generate the following execution</td>
    </tr>
    
    
    <tr>
    <td class="org-left">plan. Resource actions are indicated with the following symbols:</td>
    </tr>
    
    
    <tr>
    <td class="org-left">+ create</td>
    </tr>
    
    <tbody>
    <tr>
    </tr>
    </tbody>
    
    
    <tr>
    <td class="org-left">Terraform will perform the following actions:</td>
    </tr>
    
    <tbody>
    <tr>
    </tr>
    </tbody>
    
    
    <tr>
    <td class="org-left"># google<sub>bigquery</sub><sub>dataset.dataset</sub> will be created</td>
    </tr>
    
    <tbody>
    <tr>
    </tr>
    </tbody>
    
    
    <tr>
    <td class="org-left">[&#x2026;]</td>
    </tr>
    </tbody>
    </table>
    
    \`-&#x2014;

