from bs4 import BeautifulSoup
import requests
import pandas as pd

# get existing data
parking_data = pd.read_csv("parking_data.csv", index_col=0)
parking_data["timestamp"] = pd.to_datetime(parking_data["timestamp"])

try:
    res = requests.get("https://web1.karlsruhe.de/service/Parken/detail.php?id=K01")
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")

        # find h1 where the parking lot name is stored
        parking_lot = soup.find("h1")

        # find element with text "Gesamtzahl der freien Stellplätze"
        free_spots = soup.find(string="Gesamtzahl der freien Stellplätze").find_next(
            "td"
        )

        time_string = parking_lot.find_next("p").find_next("p")  # two after heading
        time_string = time_string.text.split("von")[1].split("Uhr")[0]
        time_string = time_string.split("-")
        time_string = time_string[0].strip() + " " + time_string[1].strip()

        timestamp = pd.to_datetime(time_string, format="%d.%m.%Y %H:%M")

        if timestamp not in parking_data['timestamp'].values:
        # append data to dataframe
            parking_data.loc[len(parking_data)] = [timestamp, free_spots.text]
            print("Data added: ", timestamp)
            print(f"   {free_spots.text} free spots")
        else:
            print("Data already exists: ", timestamp)

    else:
        print("Error: ", res.status_code)
except Exception as e:
    print("Error: ", e)

# save data to csv
parking_data.to_csv("parking_data.csv")
