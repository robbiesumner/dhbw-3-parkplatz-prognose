# Parkplatzprognose

> Projekt für die Vorlesung Big Data Programming an der DHBW Karlsruhe

Karlsruhe bietet auf https://web1.karlsruhe.de/service/Parken/ eine Übersicht über die freien Parkplätze in der Stadt. Allerdings nur jeweils den aktuellen Stand. Um die Daten zu sammeln, wird ein Web Scraper verwendet, der die Daten in eine CSV-Datei schreibt. Die [robots.txt-Datei](https://web1.karlsruhe.de/robots.txt) verbietet nicht das Crawlen dieser Seite.

# [`free_spots_scraping.py`](scraping/free_spots_scraping.py)
Liest beim einmaligen Aufrufen die freien Parkplätze von jedem Parkplatz auf https://web1.karlsruhe.de/service/Parken und schreibt einen neuen Datensatz in die jeweilige Tabelle im Ordner data. Dieses Skript wird alle 5 Minuten von einem Cronjob auf einem EC2 Server ausgeführt. Die csv-Dateien werden manuell in dieses Repository geladen.

# [`meta_data_scraping.py`](scraping/meta_data_scraping.py)
Liest die Eigenschaften der Parkplätze aus und schreibt sie in einen Datensatz meta_data.csv, der dann zum Filtern genutzt werden kann. Dieses Skript muss nur einmal ausgeführt werden.

# [`forecast.py`](app/forecast.py)
Stellt die Konsolenapplikation dar, die Nutzer verwenden können, um Parkhäuser zu filtern und Prognosen für Uhrzeit und Wochentag zu erhalten.

# [data/](data/)
Hier werden die csv-Dateien gespeichert.

# Dokumentation
Eine genauere Dokumentation ist jeweils im zugehörigen Jupyter Notebook zu finden.