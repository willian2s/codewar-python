def maskify(string: str) -> str:
    if len(string) <= 4:
        return string
    else:
        return "#" * (len(string) - 4) + string[-4:]
