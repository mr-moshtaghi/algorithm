def rotate(text: str, key: int) -> str:
    key = key % len(text)
    for i in range(key):
        c = text[i]
        text = text.replace(c, "", 1)
        text += c

    return text


print(rotate("ahmad", 7))
