import asyncio

async def mycoro(n):
    print("Starting :" +str(n))
    await asyncio.sleep(1)
    print("Finishing: "+str(n))

    return str(n)


async def print_when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print("\nResult is "+ await res)



# Example 1: run one task
f1 = asyncio.ensure_future(mycoro(1))
loop = asyncio.get_event_loop()
results = loop.run_until_complete(f1)
print(results)
loop.close()


# Example 2: run multiple tasks
# tasks = [mycoro(1),mycoro(10),mycoro(100), mycoro(2), mycoro(200)]
# futures = asyncio.gather(mycoro(1),mycoro(10),mycoro(100), mycoro(2), mycoro(200))
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(futures)
# print(results)
# loop.close()

# Example 3: run multiple tasks and print results right after each task is done.
# print("Example 3")
# tasks = [mycoro(1),mycoro(10),mycoro(100), mycoro(2), mycoro(200)]
# loop = asyncio.new_event_loop()
# results = loop.run_until_complete(print_when_done(tasks))
# print(results)
# loop.close()