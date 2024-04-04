from fastapi import FastAPI, HTTPException
import boto3
import tempfile
from ultralytics import YOLO

from config import config
from s3_uri import S3Uri
from process_result import calculate_average_confidence

app = FastAPI()

model = YOLO("best.pt")
threshold = 0.5


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
async def predict(s3_uri: str):
    s = S3Uri(s3_uri)

    s3 = boto3.client(
        "s3",
        aws_access_key_id=config.AWSConfig["access_key_id"],
        aws_secret_access_key=config.AWSConfig["secret_access_key"],
        region_name=config.AWSConfig["region_name"],
    )

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
            # Download the file from S3
            s3.download_fileobj(s.bucket, s.key, temp)
            temp_path = temp.name

        result_arr = []

        results = model.predict(temp_path, stream=True, conf=threshold)
        result_arr = []
        name = model.names
        for result in results:
            boxes = result.boxes
            for box in boxes:
                result_arr.append(
                    {"class": name[int(box.cls)], "conf": float(box.conf)}
                )
        sorted = calculate_average_confidence(result_arr)[2]
        return {"results": {"raw": result_arr, "result": sorted}}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/healthz")
def health_check():
    return {"status": "healthy"}
