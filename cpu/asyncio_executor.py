import asyncio
import time


def cpu_intensive_task(n):
    count = 0
    for i in range(n):
        count += i
    return count


async def run_cpu_task_in_thread(n):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, cpu_intensive_task, n)


async def run_asyncio():
    tasks = [10000000] * 10  # 重い計算タスクを示す
    return await asyncio.gather(*[run_cpu_task_in_thread(n) for n in tasks])

start_time = time.time()
results = asyncio.run(run_asyncio())
end_time = time.time()

print("Results:", results)
print("Time taken:", end_time - start_time)
