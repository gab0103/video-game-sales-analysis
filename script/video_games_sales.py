import pandas as pd
import matplotlib.pyplot as plt

# 1. Carica
vgs = pd.read_csv(r"D:\Python\Projects\Video_Game_Sales\data\video_games_sales.csv")

# 2. Esplora
print(vgs.head())
print(vgs.info())

# 3. Pulizia (controllo mancanti)
print(vgs.isna().sum())

# 4. Analisi: regioni con più vendite
region = vgs[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]]
region.sum().sort_values(ascending=False).plot(kind="bar", title="Vendite per regione")
plt.savefig(r"D:\Python\Projects\Video_Game_Sales\output\vendite_regioni.png", bbox_inches="tight")
plt.show()

# 5. Analisi: console con più vendite
vgs.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False).head(10)\
    .plot(kind="bar", title="Console più vendute")
plt.savefig(r"D:\Python\Projects\Video_Game_Sales\output\console_top.png", bbox_inches="tight")
plt.show()

# 6. Analisi: publisher con più giochi
vgs["Publisher"].value_counts().head(10).plot(kind="bar", title="Top 10 publisher")
plt.savefig(r"D:\Python\Projects\Video_Game_Sales\output\top_publisher.png", bbox_inches="tight")
plt.show()

# 7. Analisi: gioco più venduto per anno
migliori = vgs.loc[vgs.groupby("Year")["Global_Sales"].idxmax()]
migliori.sort_values("Year").plot(x="Year", y="Global_Sales", kind="line", marker="o", title="Gioco più venduto per anno")
plt.savefig(r"D:\Python\Projects\Video_Game_Sales\output\best_per_year.png", bbox_inches="tight")
plt.show()
