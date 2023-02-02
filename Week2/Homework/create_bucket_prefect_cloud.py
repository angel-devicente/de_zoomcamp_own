from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

gcp_credentials_block = GcpCredentials.load("de-zoomcamp-gcp-creds")

GcsBucket(bucket="de-zoomcamp-gcs",
          gcp_credentials=gcp_credentials_block
          ).save("de-zoomcamp-bucket")




