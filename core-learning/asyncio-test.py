import asyncio

async def my_async_function():
    print("Running async function...")
    await asyncio.sleep(5)  # Simulate some asynchronous task
    print("Async function completed.")

async def task_manager():
    task1 = asyncio.create_task(my_async_function())
    task2 = asyncio.create_task(my_async_function())
    
    await task1
    await task2


asyncio.run(task_manager())