import json
import matplotlib.pyplot as plt

with open("opendata_covid19_test_county_all.json", "r") as file:
    data = json.load(file)

county = "Hiiu maakond"

daily_cases = {}
daily_tests = {}


# {"LastStatisticsDate":"2023-04-10",
#  "StatisticsDate":"2020-02-05",
#  "Country":"Eesti",
#  "CountryEHAK":"233",
#  "County":"Hiiu maakond",
#  "CountyEHAK":"0039",
#  "ResultValue":"N",
#  "DailyTests":0,
#  "TotalTests":0,
#  "DailyCases":0,
#  "TotalCases":0}

for entry in data:
    if entry["County"] == county:
        date = entry["StatisticsDate"]
        if entry["ResultValue"] == "P":
            daily_cases[date] = daily_cases.get(date, 0) + entry["DailyCases"]
            daily_tests[date] = daily_tests.get(date, 0) + entry["DailyTests"]
        elif entry["ResultValue"] == "N":
            daily_tests[date] = daily_tests.get(date, 0) + entry["DailyTests"]

dates = sorted(daily_cases.keys())
cases = [daily_cases[date] for date in dates]
tests = [daily_tests[date] for date in dates]

percent_positive = [cases[i] / tests[i] * 100 if tests[i] != 0 else 0 for i in range(len(cases))]

plt.figure(figsize=(12, 6))
plt.plot(dates, cases)
plt.title(f"Pos testis Tests in Hiiu maakond")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.ylabel("Positive Tests")
plt.tight_layout()
plt.show()
