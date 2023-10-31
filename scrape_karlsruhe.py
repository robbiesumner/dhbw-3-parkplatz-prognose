from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_to_csv(parking_lot):
    BASE_URL = "https://web1.karlsruhe.de/service/Parken/detail.php?id="

    # already scraped data
    parking_data = pd.read_csv(f"./data/{parking_lot}.csv", index_col=0)
    parking_data["timestamp"] = pd.to_datetime(parking_data["timestamp"])

    try:
        res = requests.get(f"{BASE_URL}{parking_lot}")
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")

            # find h1 where the parking lot name is stored
            title = soup.find("h1")

            # find element with text "Gesamtzahl der freien Stellplätze"
            free_spots = soup.find(
                string="Gesamtzahl der freien Stellplätze"
            ).find_next("td")

            time_string = title.find_next("p").find_next("p")  # two after heading

            # from ugly string to datetime
            time_string = time_string.text.split("von")[1].split("Uhr")[0]
            time_string = time_string.split("-")
            time_string = time_string[0].strip() + " " + time_string[1].strip()

            timestamp = pd.to_datetime(time_string, format="%d.%m.%Y %H:%M")

            if timestamp not in parking_data["timestamp"].values:
                # append data to dataframe
                parking_data.loc[len(parking_data)] = [timestamp, free_spots.text]
                print("Data added: ", timestamp)
                print(f"   {free_spots.text} free spots")

                # save data to csv
                parking_data.to_csv(f"./data/{parking_lot}.csv")
            else:
                print("Data already exists: ", timestamp)

        else:
            print("Error: ", res.status_code)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    # for now hardcoded, maybe also scrape this?
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

    for parking_lot in parking_lots:
        scrape_to_csv(parking_lot)
