path = "/Users/yordanstrahinov/Documents/GitHub/Learn-Python-the-Hard-Way-3rd-Edition/ex16-writing_file/output.txt"
text = """An original elvish‑style verse,
soft steps by moonlit trees,
winds that sing of olden paths,
and rivers calling home."""
with open(path, "w", encoding="utf-8") as f:
    f.write(text)
f.close()