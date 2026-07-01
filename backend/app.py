from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, Response
import boto3
import json
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
START_LAMBDA = os.getenv("START_LAMBDA")
STOP_LAMBDA = os.getenv("STOP_LAMBDA")

app = FastAPI(
    title="EC2 Automation API",
    version="1.0.0"
)

# AWS Lambda Client
lambda_client = boto3.client(
    "lambda",
    region_name=AWS_REGION
)


@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/index.css")
def get_css():
    with open("frontend/index.css", "r", encoding="utf-8") as f:
        return Response(content=f.read(), media_type="text/css")

@app.get("/script.js")
def get_js():
    with open("frontend/script.js", "r", encoding="utf-8") as f:
        return Response(content=f.read(), media_type="application/javascript")

@app.get("/info")
def info():
    return {
        "message": "FastAPI EC2 Automation API",
        "aws_region": AWS_REGION,
        "start_lambda": START_LAMBDA,
        "stop_lambda": STOP_LAMBDA
    }


@app.post("/start-server")
def start_server():
    try:

        print(f"Calling Lambda: {START_LAMBDA}")

        response = lambda_client.invoke(
            FunctionName=START_LAMBDA,
            InvocationType="RequestResponse"
        )

        payload = json.loads(response["Payload"].read())

        # Lambda executed but returned an error
        if "errorMessage" in payload:
            raise HTTPException(
                status_code=500,
                detail=payload["errorMessage"]
            )

        return {
            "status": "success",
            "lambda": START_LAMBDA,
            "response": payload
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/stop-server")
def stop_server():
    try:

        print(f"Calling Lambda: {STOP_LAMBDA}")

        response = lambda_client.invoke(
            FunctionName=STOP_LAMBDA,
            InvocationType="RequestResponse"
        )

        payload = json.loads(response["Payload"].read())

        if "errorMessage" in payload:
            raise HTTPException(
                status_code=500,
                detail=payload["errorMessage"]
            )

        return {
            "status": "success",
            "lambda": STOP_LAMBDA,
            "response": payload
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )