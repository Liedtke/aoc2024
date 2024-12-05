import importlib

for i in range(1, 26):
    try:
        print(f"=== Day {i} ===")
        importlib.__import__(f"day{i:02d}")
    except ModuleNotFoundError:
        print("Not solved, yet!")
        break
