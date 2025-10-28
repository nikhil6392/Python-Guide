"""I/O bound tasks"""

import asyncio

async def coroutine1():
    print("Coroutine Started")
    await asyncio.sleep(1)
    print("Coroutine resumed")

asyncio.run(coroutine1())


"""
    Output : Coroutine Started
             Coroutine resumed
"""