import time


def cpu_intensive_task(n):
    count = 0
    for i in range(n):
        count += i
    return count


def run_sequential():
    tasks = [10000000] * 10  # 重い計算タスクを示す
    results = [cpu_intensive_task(n) for n in tasks]
    return results


start_time = time.time()
results = run_sequential()
end_time = time.time()

print("Results:", results)
print("Time taken:", end_time - start_time)
