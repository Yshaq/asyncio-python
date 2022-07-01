# https://www.youtube.com/watch?v=t5Bo1Je9EmEhttps://www.youtube.com/watch?v=t5Bo1Je9EmE
# using python3.10
import asyncio

# async tells python to put a wrapper around this function, and that turns it into a coroutine
# when you call this function, it returns a coroutine object, which is just like a fn and can be executed, but needs to await
async def main():
    print('hello main') 

# main()
# RuntimeWarning: coroutine 'main' was never awaited

# print(main())
# <coroutine object main at 0x7f5ea409a570>
# RuntimeWarning: coroutine 'main' was never awaited

# await main()
# 'await' outside function
# we need an async event loop

# asyncio.run(main())
# asyncio created an event loop and ran the coroutine

# USING THE AWAIT KEYWORD

async def foo(text):
    print(text)
    await asyncio.sleep(10)
    # await keyword is used to execute a coroutine. But, it must be inside an async function. asyncio.sleep() is also a coroutine

async def foo1():
    print('hello foo1')
    # foo('text')
    # RuntimeWarning: coroutine 'foo' was never awaited
    await foo('text')
    print('finished foo1')

# asyncio.run(foo1())

# TASKS - run something else when awaiting
async def main2():
    print('hello main2')
    task = asyncio.create_task(foo('text'))
    # await task
    # await task will block the program till task is finished
    await asyncio.sleep(0.5)
    print('finished')

asyncio.run(main2())


