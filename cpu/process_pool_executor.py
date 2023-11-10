from concurrent.futures import ProcessPoolExecutor
import time


def cpu_intensive_task(n):
    count = 0
    for i in range(n):
        count += i
    return count


def run_process_pool_executor():
    tasks = [10000000] * 10  # 重い計算タスクを示す
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_intensive_task, tasks))
        return results


if __name__ == '__main__':
    start_time = time.time()
    results = run_process_pool_executor()
    end_time = time.time()

    print("Results:", results)
    print("Time taken:", end_time - start_time)
