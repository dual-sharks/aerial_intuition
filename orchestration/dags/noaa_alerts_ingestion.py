from __future__ import annotations

import json
from datetime import datetime
from typing import Optional

import requests
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


BUCKET_NAME = "noaa-prototype"          # TODO: set this
S3_PREFIX = "noaa/alerts"                 # base prefix in the bucket
# We rely on the local/runner AWS profile (e.g. AWS_PROFILE=sharks), not an Airflow connection.
AWS_CONN_ID = None


@dag(
    schedule="*/15 * * * *",              # every 15 minutes
    start_date=days_ago(1),
    catchup=False,
    tags=["noaa", "alerts"],
)
def noaa_alerts_ingestion():
    """
    Fetch NOAA alerts every 15 minutes and land raw JSON in S3.
    """

    @task
    def fetch_alerts_to_s3(
        data_interval_start: Optional[datetime] = None,
        data_interval_end: Optional[datetime] = None,
    ) -> str:
        # Airflow passes these when using the TaskFlow API
        start = data_interval_start.isoformat() if data_interval_start else None
        end = data_interval_end.isoformat() if data_interval_end else None

        params = {}
        if start and end:
            params["start"] = start
            params["end"] = end

        resp = requests.get(
            "https://api.weather.gov/alerts",
            params=params,
            headers={
                "User-Agent": "your-org-noaa-alerts/1.0 (you@example.com)",
                "Accept": "application/geo+json",
            },
            timeout=30,
        )
        resp.raise_for_status()
        payload = resp.json()

        ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        key = f"{S3_PREFIX}/ingest_date={ts[:8]}/ingest_hour={ts[9:11]}/alerts-{ts}.json"

        s3 = S3Hook(aws_conn_id=AWS_CONN_ID)
        s3.load_bytes(
            bytes(json.dumps(payload), "utf-8"),
            key=key,
            bucket_name=BUCKET_NAME,
            replace=False,
        )
        return key

    # Trigger the S3 write on each DAG run; no downstream DB work yet.
    fetch_alerts_to_s3()


dag = noaa_alerts_ingestion()