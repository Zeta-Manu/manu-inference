import os

AWSConfig = {
    "access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "secret_access_key": os.getenv("AWS_SECRET_KEY"),
    "region_name": os.getenv("AWS_REGION"),
}
