# simple_clean.py

in_file = input("Входной файл: ").strip()
out_file = input("Выходной файл: ").strip()

with open(in_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

result = []
prev_blank = False

for line in lines:
    # 1) убираем строки-комментарии (после пробелов/табов начинается //)
    if line.lstrip().startswith("//"):
        continue

    # 2) обрезаем хвостовой комментарий //
    p = line.find("//")
    if p != -1:
        line = line[:p]

    # 3) сохраняем отступ, схлопываем пробелы в остальной части
    i = 0
    while i < len(line) and line[i] in (" ", "\t"):
        i += 1

    indent = line[:i].replace("\t", "    ")   # таб в отступе -> 4 пробела
    rest = line[i:].replace("\t", " ")
    rest = " ".join(rest.split())            # много пробелов -> один

    cleaned = (indent + rest).rstrip()

    # 4) контроль пустых строк
    if cleaned == "":
        if prev_blank:
            continue
        prev_blank = True
        result.append("")
    else:
        prev_blank = False
        result.append(cleaned)

with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n".join(result) + "\n")
