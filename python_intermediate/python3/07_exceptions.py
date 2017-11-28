try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))
