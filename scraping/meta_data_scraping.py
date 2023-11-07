from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_meta_data(parking_lot):
    BASE_URL = "https://web1.karlsruhe.de/service/Parken/detail.php?id="

    try:
        res = requests.get(f"{BASE_URL}{parking_lot}")
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")

            print(f"Scraping {parking_lot}...")

            title = soup.find("h1").text

            height = soup.find(string="Durchfahrtshöhe").find_next("td").text.split()[0]

            elevator = soup.find(string="Aufzug").find_next("td").text
            elevator = True if elevator == "ja" else False

            charging_station = soup.find(string="Ladestation").find_next("td").text
            charging_station = True if charging_station == "ja" else False

            total_spots = soup.find(string="Gesamtzahl der Stellplätze").find_next("td").text

            disabled_spots = soup.find(string="Behinderten-Stellplätze").find_next("td").text

            df.loc[len(df)] = [
                parking_lot,
                title,
                height,
                elevator,
                charging_station,
                total_spots,
                disabled_spots,
            ]

        else:
            print("Error: ", res.status_code)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    df = pd.DataFrame(
        columns=[
            "Parkhauskuerzel",
            "Parkhausname",
            "Durchfahrtshoehe",
            "Aufzug",
            "Ladestation",
            "Gesamtanzahl",
            "Behindertenstellplaetze",
        ]
    )
    parking_lots = [
        "K01",
        "K02",
        "K03",
        "K04",
        "N02",
        "N03",
        "N05",
        "N06",
        "N07",
        "S01",
        "S02",
        "S03",
        "S04",
        "S05",
        "S06",
        "S07",
        "W01",
        "W02",
        "W03",
        "W04",
    ]

    for p in parking_lots:
        scrape_meta_data(p)

    df.to_csv("../data/meta_data.csv", index=False)
