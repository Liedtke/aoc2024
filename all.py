import importlib
import time

for i in range(1, 26):
    try:
        start = time.time()
        print(f"=== Day {i} ===")
        importlib.__import__(f"day{i:02d}")
        print(f"Elapsed time: {int(1000 * (time.time() - start))} ms")
    except ModuleNotFoundError:
        print("Not solved, yet!")
        break
