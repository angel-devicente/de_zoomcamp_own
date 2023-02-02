
# Table of Contents



Homework at
<https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_2_workflow_orchestration/homework.md>

-   Question 1
    
        python etl_web_to_gcs.py
        
        [...]
        01:07:54.432 | INFO    | Task run 'clean-b9fd7e03-0' - rows: 447770
        [...]
    
    &#x2013;> 447770

-   Question 2
    
    the arguments for a cron job are: `Min Hour Mday Month Wday Command`
    so the first day of every mont at 5AM is:
    
    &#x2013;> 0 5 1 \* \*

-   Question 3
    
    First we need to upload yellow taxi data for 2019/02 and 2019/03 to GCS. For
    that, after creating the data/yellow directory we run: `python
      etl_web_to_gcs_Q3.py` which downloads it locally and uploads the data to GCS
    Bucket. 
    
    The code is in `etl_gcs_to_bq.py`. To create the deployment:
    
        prefect deployment build ./etl_gcs_to_bq.py:etl_gcs_to_bq -n "Homework Q3"
    
    Edit `etl_gcs_to_bq-deployment.yaml`, so that parameters becomes:
    
        parameters: {'sets': [{'color': "yellow", 'year': 2019,'month': 2},
                            {'color': "yellow", 'year': 2019,'month': 3}]}
    
    Apply the deployment by doing: `prefect deployment apply
      etl_gcs_to_bq-deployment.yaml` 
    
    Start the agent with `prefect agent start -q 'default'`
    
    In the Orion UI, go to the newly created deployment (Homework Q3) and click on
    Quick Run.
    
    We see that the agent starts logging information about the different flows,
    and towards the end we get the line:
    
        11:31:36.276 | INFO    | Flow run 'sparkling-mamba' - Total rows added: 14851920
    
    &#x2013;> 14,851,920

-   Question 4
    
    I create a github block (`github-de-zoomcamp-block`) pointing to my repository:
    <https://github.com/angel-devicente/de_zoomcamp_own>
    
    I create the deployment based on the file `etl_web_to_gcs_Q4.py` (which is
    almost the same as `etl_web_to_gcs.py`, but modifying two things:
    
    -   the file to download is November'20 (green taxi trips)
    -   I have to create the directory `data/green` in write<sub>local</sub> (because
        deployments run by default in a temporary directory).
    
    I create the deployment with `python github_deploy.py`
    
    Alternatively, we could also create the deployment from the command line (from
    the main repo directory): 
    
        prefect deployment build ./Week2/Homework/etl_web_to_gcs_Q4.py:etl_web_to_gcs
        -n github-example -sb github/github-de-zoomcamp-block -q default -o
        github-deployment.yaml 
    
    Start the agent with `prefect agent start -q 'default'`
    
    And run the deployment with `prefect deployment run
      etl-web-to-gcs/github-example` 
    
    The agent runs the deployment and towards the end writes in the log:
    
        21:34:55.581 | INFO    | Task run 'clean-2c6af9f6-0' - rows: 88605                                 
        21:34:55.622 | INFO    | Task run 'clean-2c6af9f6-0' - Finished in state Completed()
    
    &#x2013;> 88605

-   Question 5
    
    I use `app.prefect.cloud`. I recreate the blocks: GitHub, GCP Credentials, GCS
    Bucket. This last one I cannot create with the UI (it doesn't offer the
    drop-down menu to add credentials, so I create it programatically with the
    file `create_bucket_prefect_cloud.py`
    
    I create the deployment by running `python github_deploy_Q5.py` (which will use
    the flow in `etl_web_to_gcs_Q5.py`, modified to use data from April 2019)
    
    I create an E-mail block to my mail address, and with it an automation for the
    `etl-web-to-gcs` flow when completed.
    
    I start the agent `prefect agent start -q 'default'`
    
    and run it with `prefect deployment run etl-web-to-gcs/github-example`
    
    And I get the e-mail just fine:
    
        Prefect <no-reply@prefect.io>
        
        to angel.de.vicente
        Flow run etl-web-to-gcs/mature-tuatara entered state `Completed` at 2023-02-02T10:08:56.827824+00:00.
        Flow ID: fd2282f8-63f7-451c-8f38-28c9b206a87f
        Flow run ID: 874acc65-49bd-4b90-b3f5-3095eb71bf62
    
    and the log says that 514392 rows were processed.
    
    &#x2013;> 514,392

-   Question 6
    
    This one is trivial. Go to `Blocks -> Secret`, give it a name, introduce a
    10-digit number and the block page shows:
    
        Value
        ********
    
    &#x2013;> 8

