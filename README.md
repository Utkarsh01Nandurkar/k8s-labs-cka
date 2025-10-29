# Kubernetes Labs (CKA) – Auto-Heal System

This project demonstrates a **Kubernetes self-healing mechanism** using **Python** and **Kubernetes API**.

## 🚀 Features
- Detects non-running pods across namespaces.
- Automatically deletes and restarts failed pods.
- Sends alerts to Slack via webhook integration.
- Includes sample deployment and health-check CronJob.

## ⚙️ Tech Stack
- Kubernetes (EKS / Minikube)
- Python 3
- Slack API
- kubernetes-client (Python SDK)

## ▶️ Run Locally
```bash
git clone https://github.com/Utkarsh01Nandurkar/kubernetes-labs-cka.git
cd kubernetes-labs-cka/autoheal
pip install -r requirements.txt
export SLACK_WEBHOOK="https://hooks.slack.com/services/XXXX/YYYY/ZZZZ"
python heal_pods.py

- Cost optimization

### Tech Stack
AWS | Terraform | Docker | Kubernetes | Python | Prometheus | Grafana

### Author
**Utkarsh Nandurkar**  
[LinkedIn](https://linkedin.com/in/utkarsh-nandurkar-1533821b0) • [Portfolio](https://utkarsh01nandurkar.github.io)
