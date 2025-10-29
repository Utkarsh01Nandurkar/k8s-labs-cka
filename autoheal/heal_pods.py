#!/usr/bin/env python3
import os
from kubernetes import client, config
import requests

# Load Slack webhook from environment
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_alert(message):
    if SLACK_WEBHOOK:
        requests.post(SLACK_WEBHOOK, json={"text": message})
        print(f"📢 Slack alert sent: {message}")

def main():
    config.load_kube_config()  # Reads local kubeconfig
    v1 = client.CoreV1Api()

    print("🔍 Checking pod statuses across all namespaces...")
    pods = v1.list_pod_for_all_namespaces(watch=False)

    for pod in pods.items:
        ns = pod.metadata.namespace
        name = pod.metadata.name
        phase = pod.status.phase

        if phase not in ["Running", "Succeeded"]:
            message = f"⚠️ Pod '{name}' in namespace '{ns}' is in {phase} state. Restarting..."
            print(message)
            send_alert(message)
            v1.delete_namespaced_pod(name=name, namespace=ns)
            send_alert(f"✅ Pod '{name}' restarted successfully.")

if __name__ == "__main__":
    main()
