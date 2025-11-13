cd "C:\Users\jbaca\OneDrive\Documents\2. Ph.D. in Economics\Courses\Semester 7 - Fall 2025\ECON 220 - Data Science for Economists - Lab\Lectures\Week 6"

use "ipums_usa2023.dta", clear

set seed 2025

sample 10000, count

export delimited using "ipums_2023.csv", replace