import pandas as pd

df = pd.read_csv("clean_dialog.csv")
main_chars = ["Twilight Sparkle", "Rarity", "Fluttershy", "Pinkie Pie", "Rainbow Dash"]
lines_spoken = [0, 0, 0, 0, 0]

total_lines = len(df)
pony_counts = df['pony'].value_counts()

for i, pony in enumerate(main_chars):
    if pony in pony_counts:
        lines_spoken[i] = pony_counts[pony]

final_counts = pd.DataFrame(columns=["pony_name", "total_line_count", "percent_all_lines"])

for i, pony in enumerate(main_chars):
    percent = (lines_spoken[i] / total_lines) * 100
    final_counts.loc[i] = [pony, lines_spoken[i], round(percent, 2)]

final_counts.to_csv("Line_percentages.csv", index=False)    