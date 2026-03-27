try:
    print("A")
    raise Exception("boom")
    print("B")   # ❌ never runs
except Exception:
    print("C",Exception)