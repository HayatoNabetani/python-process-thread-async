from concurrent.futures import ThreadPoolExecutor
import time


def cpu_intensive_task(n):
    # 例として、単純な計算処理を行う
    count = 0
    for i in range(n):
        count += i
    return count


def run_threadpool_executor():
    tasks = [10000000] * 10  # 重い計算タスクを示す
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(cpu_intensive_task, tasks))
    return results


start_time = time.time()
results = run_threadpool_executor()
end_time = time.time()

print("Results:", results)
print("Time taken:", end_time - start_time)
