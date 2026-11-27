import asyncio

from camunda_orchestration_sdk import CamundaAsyncClient

from workers import register_workers

async def main() -> None:
    #read the cluster address & OAuth credentials from env
    #the async context manager closes the client when the program exits
    async with CamundaAsyncClient() as client:
        #register the job types and their handler functions from workers.py
        register_workers(client)
        print("Workers registered, waiting for camunda jobs...")
        #keep worker running so it can recieve and process jobs
        await client.run_workers()

if __name__ == "__main__":
    #start asyncio event loop when this file is run directly
    asyncio.run(main())