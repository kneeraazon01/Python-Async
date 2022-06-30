print("tuck async")
import asyncio


async def main():
    print("main 1")
    task = asyncio.create_task(main2())
    print("world 1")


async def main2():
    print("main 2")
    await asyncio.sleep(1)


asyncio.run(main())
print("end")
