import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "C:/Users/jbaca/OneDrive/Documents/2. Ph.D. in Economics/Courses/Semester 7 - Fall 2025/ECON 220 - Data Science for Economists - Lab/Lectures/Week 3"

url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
flights = pd.read_csv(url)
flights_sample = flights.sample(n=1000, random_state=42)
flights_sample = flights_sample[["year", "month", "day", "dep_time", "sched_dep_time", "arr_time", "sched_arr_time", "distance", "origin", "dest"]]
flights_sample.to_csv(f"{path}/flights.csv", index=False)