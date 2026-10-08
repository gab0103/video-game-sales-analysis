\\# Analisi delle vendite di videogiochi







Analisi di un dataset di 16.598 videogiochi con pandas e matplotlib: quali regioni vendono di più, quali console dominano, quali publisher pubblicano più titoli e qual è il gioco più venduto per ogni anno.







\\## Domanda







Quali sono le regioni, le console e i publisher più importanti nel mercato dei videogiochi, e come sono cambiate le vendite nel tempo?







\\## Dataset







\\- \\\*\\\*Fonte:\\\*\\\* \\\[Kaggle — Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)



\\- \\\*\\\*Dimensioni:\\\*\\\* 16.598 righe, 11 colonne



\\- \\\*\\\*Periodo coperto:\\\*\\\* 1980–2020 (con pochi dati dopo il 2016)



\\- \\\*\\\*Colonne principali:\\\*\\\* `Rank`, `Name`, `Platform`, `Year`, `Genre`, `Publisher`, vendite per regione (`NA\\\_Sales`, `EU\\\_Sales`, `JP\\\_Sales`, `Other\\\_Sales`, `Global\\\_Sales`)







\\## Cosa ho fatto







1\\. \\\*\\\*Caricamento\\\*\\\* del CSV con `pd.read\\\_csv`



2\\. \\\*\\\*Esplorazione\\\*\\\* con `head()`, `info()`, `shape`



3\\. \\\*\\\*Pulizia\\\*\\\*: individuati 271 valori mancanti in `Year` e 58 in `Publisher`



4\\. \\\*\\\*Analisi\\\*\\\* con `groupby`, `value\\\_counts` e `sum`



5\\. \\\*\\\*Visualizzazione\\\*\\\* con matplotlib (4 grafici salvati in `output`)







\\## Risultati principali







1\\. \\\*\\\*Regioni:\\\*\\\* il Nord America domina le vendite con \\\~4.393 milioni di copie, più del doppio dell'Europa (\\\~2.434).



2\\. \\\*\\\*Console:\\\*\\\* \\\[inserisci la console con più vendite]



3\\. \\\*\\\*Publisher:\\\*\\\* Electronic Arts è il publisher con più titoli (1.351), davanti ad Activision (975).



4\\. \\\*\\\*Gioco più venduto in assoluto:\\\*\\\* Wii Sports (2006) con 82,74 milioni di copie, il più alto del dataset.







\\## Grafici







!\\\[Vendite per regione](output/vendite\\\_regioni.png)







!\\\[Console più vendute](output/console\\\_top.png)







!\\\[Top 10 publisher](output/top\\\_publisher.png)







!\\\[Gioco più venduto per anno](output/best\\\_per\\\_year.png)







\\## Limiti







Il dataset copre bene il periodo 1980–2010 ma ha pochissimi dati dopo il 2016, quindi i risultati degli anni recenti non sono rappresentativi.







\\## Strumenti







\\- Python 3.14



\\- pandas



\\- matplotlib







\\## Come eseguirlo







```bash



python script/analisi.py







Due note:







\\- Per la \\\*\\\*console più venduta\\\*\\\* (punto 2 dei risultati), esegui questo e sostituisci il segnaposto con quello che esce:



\&#x20; ```python



\&#x20; print(vgs.groupby("Platform")\\\["Global\\\_Sales"].sum().sort\\\_values(ascending=False).head(1))

















