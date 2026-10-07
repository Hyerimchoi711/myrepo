f = open("scores.csv", "r", 
        encoding="utf-8")

lines = f.readlines() 
f.close()

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count, totals, counts = 0, {}, {}
for lines in lines[1:]:
    parts = lines.strip().split(",")
    raw = parts[score_idx].strip()

    try:
        score = float(raw)
    except ValueError:
        continue

    count += 1

    category = parts[cat_idx]
    
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0

    totals[category] += score
    counts[category] += 1

for c in sorted(totals.keys()):
    avg = totals[c] / counts[c]
    print(c, round(avg, 2))