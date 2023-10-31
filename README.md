# Parkplatzprognose

Projekt für die Vorlesung Big Data Programming

## Web Scraping
Karlsruhe bietet auf https://web1.karlsruhe.de/service/Parken/ eine Übersicht über die freien Parkplätze in der Stadt. Allerdings nur jeweils den aktuellen Stand. Um die Daten zu sammeln, wird ein Web Scraper verwendet, der die Daten in eine CSV-Datei schreibt.

### robots.txt
https://web1.karlsruhe.de/robots.txt verbietet nicht das Crawlen der Seite.

### Implementierung
1. [`scrape_karlsruhe.py`](scrape_karlsruhe.py): Liest beim einmaligen Aufrufen die freien Parkplätze von jedem Parkplatz auf https://web1.karlsruhe.de/service/Parken und scheibt einen neuen Datensatz in die jeweilige Tabelle im Ordner [data](data).
    - TODO: Daten für Parkplatztyp sammeln?
2. Dieses Skript wird alle 5 Minuten von einem Cronjob auf einem EC2 Server ausgeführt. 
    - TODO: Daten von EC2 mit Github synchronisieren?
