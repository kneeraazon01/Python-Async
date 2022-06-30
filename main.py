print("tuck async")
import asyncio


async def main():
    print("main 1")
    await main2()
    print("world 1")


async def main2():
    print("main 2")
    await asyncio.sleep(5)
    print("world 2")


asyncio.run(main())
print("end")
