"""Coroutines"""

"""They are powerful feature in Python that allow for asynchronous programming"""

import asyncio

async def coroutine1():
    print("It begins")
    await asyncio.sleep(1)
    print('It resumed')
    return 'Coroutine Finished'

asyncio.run(coroutine1())


"""
    Output : It begins
             It resumed
"""