"""
    Asyncio is a Python library that is used to write concurrent code in a simple and efficient way. Traditionally, asyncio was mainly used for IO-bound tasks, but it can also be used for CPU -bound tasks.
    In this note, we will discuss how to use asyncio for CPU-bound tasks.

    When we talk about CPU-bound tasks, we refer to tasks that involve significant computation and are CPU-intensive. These tasks can block the even loop and make the program unresponsive. To avoid this, we can use asyncio to run these tasks in a separate thread or process.

    To use asyncio for CPU-bound tasks, we need to create a custom event loop and run our tasks in a separate executor. Here is an example of how to do this:
"""

import asyncio
import concurrent.futures

async def cpu_bound_task(num):
    return sum(range(num))

async def main():
    loop = asyncio.get_running_loop()
    executor = concurrent.futures.ThreadPoolExecutor()
    result = await loop.run_in_executor(executor, cpu_bound_task, 1000000)
    print(f'The result is {result}')

    asyncio.run(main())