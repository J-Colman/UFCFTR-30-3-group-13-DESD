import asyncio
import uuid

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    MessagePublicationRequest,
    MessagePublicationRequestVariables,
    WorkerConfig,
)


def get_vars(job: ConnectedJobContext) -> dict:
    return job.variables.to_dict()


# Authenticate Customer Sub-Process

async def check_credentials(job: ConnectedJobContext) -> dict[str, object]:
    return {}

async def create_account(job: ConnectedJobContext) -> dict[str, object]:
    return {}


# F1: Stock and Producers

async def check_stock(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def show_unavailable_items(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def identify_producers(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def determine_delivery_options(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def prepare_order_summary(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def reserve_stock(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def create_order(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def split_by_producer(job: ConnectedJobContext) -> dict[str, object]:
    return {}


async def publish_order_ready(job: ConnectedJobContext) -> dict[str, object]:
    return {}


WORKERS = {
    "job-check-credentials": check_credentials,
    "job-create-account": create_account,
    "job-check-stock": check_stock,
    "job-show-unavailable-items": show_unavailable_items,
    "job-identify-producers": identify_producers,
    "job-prepare-order-summary": prepare_order_summary,
    "job-reserve-stock": reserve_stock,
    "job-create-order": create_order,
    "job-split-by-producer": split_by_producer,
    "job-publish-order-ready": publish_order_ready,
}


def register_workers(client: CamundaAsyncClient) -> None:
    for job_type, callback in WORKERS.items():
        client.create_job_worker(
            config=WorkerConfig(
                job_type=job_type,
                job_timeout_milliseconds=10_000,
                max_concurrent_jobs=5,
                worker_name=f"{job_type}-worker",
            ),
            callback=callback,
        )
