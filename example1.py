# using python3.10
import asyncio

# simulate an http request
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'msg': 'this is the response msg'}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # value = task1
    # print(value)
    # <Task pending name='Task-2' coro=<fetch_data() running at /home/vysakh/python-my/async-tut/example1.py:4>>
    # This is a 'future' . kindof liek a Promise in JS.

    await task1
    value = task1
    # now we will wait for the coroutine to end, not the future
    print(task1.result())

    await task2
    # without this await, we will end the program even if task2 hasnt finished executing
    
asyncio.run(main())

