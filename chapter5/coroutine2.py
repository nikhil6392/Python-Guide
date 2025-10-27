import asyncio

async def coroutine2(id):
    print(f'Coroutine {id} started')
    await asyncio.sleep(1)
    print(f'Coroutine {id} resumed')
    return f'Coroutine {id} started'

async def main():
    tasks = [asyncio.create_task(coroutine2(i)) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())


"""
    Output : Coroutine 0 started
             Coroutine 1 started
             Coroutine 2 started
             Coroutine 0 resumed
             Coroutine 1 resumed
             Coroutine 2 resumed
             ['Coroutine 0 started', 'Coroutine 1 started', 'Coroutine 2 started']
"""