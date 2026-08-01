from simple_eda import load_sample, bar
df = load_sample()
ax = bar(df, "region", "sales_2024",
         title="West leads 2024 sales", highlight="West")
ax.figure.savefig("test.png", dpi=150)  