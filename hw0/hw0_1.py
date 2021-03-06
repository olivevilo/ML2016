import sys

col = int(sys.argv[1])
fileName = sys.argv[2]

# python garbage collection mechanism
with open(fileName) as f:
    contents = f.read().splitlines()

results = []

for content, i in zip(contents, range(len(contents))):
    df = content.split(" ")  # .remove(" ")
    # eliminate blank element
    for e in df:
        if(e == ''):
            df.remove(e)
    # from string to numeric style
    try:
        df[col] = int(df[col])
    except ValueError:
        df[col] = float(df[col])

    results.append(df[col])

results.sort()
# final output format
results = map(str, results)

final_result = ', '.join(results)

with open("ans1.txt", "w") as text_file:
    text_file.write(final_result)

# future work: rewrite by pandas?!
