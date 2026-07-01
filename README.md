# 🚀 EC2 Automation using FastAPI + AWS Lambda

Automate the startup and shutdown of an AWS EC2 instance using **FastAPI**, **AWS Lambda**, and **boto3**.

This project demonstrates how a FastAPI application can invoke AWS Lambda functions to start and stop an EC2 instance on demand, helping reduce AWS costs by running compute resources only when needed.

---

# 📌 Features

- ✅ Start an EC2 instance using AWS Lambda
- ✅ Stop an EC2 instance using AWS Lambda
- ✅ FastAPI REST API
- ✅ Beautiful HTML Dashboard
- ✅ IAM Role Authentication (No AWS Keys)
- ✅ Cost Optimization
- ✅ Easy Deployment on EC2

---

# 🏗️ Architecture

```text
                  User
                    │
                    ▼
          FastAPI Dashboard (EC2)
                    │
            boto3 Invoke Lambda
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   StartEC2 Lambda         StopEC2 Lambda
        │                       │
        ▼                       ▼
   EC2 Start API          EC2 Stop API
        │
        ▼
    Target EC2 Instance
```

---

# 📁 Project Structure

```
fastapi-ec2-demo/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── index.css
│   └── script.js
│
├── .env
├── aws_config.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

- Python 3.11+
- FastAPI
- boto3
- AWS Lambda
- Amazon EC2
- IAM
- HTML
- CSS
- JavaScript
- Uvicorn

---

# 🔑 Prerequisites

- AWS Account
- EC2 Instance
- AWS Lambda
- IAM Roles
- Python 3.11+

---

# AWS Setup

## 1. Create EC2 Instance

Launch an Ubuntu EC2 instance.

Example:

```
t3.micro
Ubuntu 24.04
```

Open Security Group Ports

```
22
80
443
8000
```

---

## 2. Create Lambda Functions

Create two Lambda functions.

```
startEC2
StopEC2
```

---

## Start Lambda

```python
import boto3

ec2 = boto3.client("ec2")

INSTANCE_ID = "YOUR_INSTANCE_ID"

def lambda_handler(event, context):

    ec2.start_instances(
        InstanceIds=[INSTANCE_ID]
    )

    return {
        "statusCode":200,
        "message":"EC2 Started"
    }
```

---

## Stop Lambda

```python
import boto3

ec2 = boto3.client("ec2")

INSTANCE_ID="YOUR_INSTANCE_ID"

def lambda_handler(event, context):

    ec2.stop_instances(
        InstanceIds=[INSTANCE_ID]
    )

    return{
        "statusCode":200,
        "message":"EC2 Stopped"
    }
```

---

# IAM Permissions

## Lambda Role

Allow

```
ec2:StartInstances

ec2:StopInstances
```

---

## FastAPI EC2 IAM Role

Allow

```
lambda:InvokeFunction
```

---

# Environment Variables

Create a `.env`

```
AWS_REGION=us-east-1

START_LAMBDA=startEC2

STOP_LAMBDA=StopEC2
```

---

# Install

Clone repository

```bash
git clone https://github.com/jothiprakash17042001/fastapi-ec2-demo.git

cd fastapi-ec2-demo
```

Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate

Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run

```bash
uvicorn backend.app:app --reload
```

or

```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

---

# API Endpoints

## Home

```
GET /
```

Returns the HTML Dashboard.

---

## Information

```
GET /info
```

---

## Start Server

```
POST /start-server
```

Invokes Lambda to start the EC2 instance.

---

## Stop Server

```
POST /stop-server
```

Invokes Lambda to stop the EC2 instance.

---

# Deployment on EC2

SSH

```bash
ssh -i "ec2-auto.pem" ubuntu@<PUBLIC-IP>
```

Clone

```bash
git clone https://github.com/jothiprakash17042001/fastapi-ec2-demo.git
```

Install

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Run

```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

Visit

```
http://<PUBLIC-IP>:8000
```

---

# Cost Optimization

Instead of keeping expensive EC2 instances running continuously:

1. FastAPI receives the request.
2. Lambda starts the EC2 instance.
3. Workload executes.
4. Lambda stops the EC2 instance.
5. You only pay while the instance is running.

---

# Future Improvements

- Execute Python jobs using AWS Systems Manager (SSM)
- CloudWatch logging
- Job queue support
- Authentication
- Docker deployment
- GitHub Actions CI/CD
- Automatic health checks
- Real-time EC2 status monitoring

---

# Author

**Prakash Shanmugam**

Junior AI/ML Engineer

GitHub: https://github.com/<your-username>

LinkedIn: https://linkedin.com/in/<your-profile>

---

# License

This project is licensed under the Viyona fintech private limited License.

<img width="1908" height="1032" alt="image" src="https://github.com/user-attachments/assets/d2f00ffa-b0c4-4864-8ead-e1a8e212a157" />

