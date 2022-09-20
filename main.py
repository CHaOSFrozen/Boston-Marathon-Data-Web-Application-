import streamlit as st
import csv, pathlib
from pathlib import Path

#----------- Reads the data ------------#
fp = Path.cwd()/"boston_data.csv"

# Reads the csv 
with fp.open("r", newline="") as file:
    data = csv.reader(file) 
    next(data) # Skips the header
    details = [] # Stores details of each runner
    all_name = [] # Stores just the name of runners 
    all_time = [] # Stores just the time of runners

    for line in data:
        details.append(line)
        all_name.append(line[1])
        all_time.append(int(line[5]))

#----------- Creates the title and header for dashboard ------------#

st.title("Boston Marathon Data 2018") # Creates a title for the dashboard
st.header("Runner's Finishing Time") # Creates a header 

#----------- Display runner's finishing time based on selection widget ------------#
# Allows user to select names to display finishing time
selection = st.multiselect("You may select more than one runner : ", all_name)

# Iterates based on the length of details 
for index in range(len(details)):
    # if runners name is found in selection
    if details[index][1] in selection:

        time = round(int(details[index][5])/60, 2) # store time and divide by 60 
        name = details[index][1] # store the name
        country = details[index][3] # store the country
        age = details[index][2] # store the age
       
        # Creates 3 column in the dashboard (Invisible to the Naked Eye)
        col1, col2, col3, = st.columns(3)
        # Use metric function to display each runner's (Labels) detail from the variables. (Values)
        col1.metric(label = "Participant", value = name)
        col2.metric("Age", age) 
        col3.metric("Finishing Time (Hours)", time)

#----------- Displays Runner's finishing time based on slider widget  ------------#

# Use select_slider function to allow user to select runners by finishing time
time_selection = st.select_slider("Select a range of finishing time", options=all_time, value=(min(all_time), max(all_time)))

# Select_slider return a tuple of min and max values 
time1 = time_selection[0] # store min value 
time2= time_selection[1] # store max value

# Creates 4 columns to display runner's details based min and max values
col5, col6, col7, col8 = st.columns(4)
# Iterates over details 
for line in details:
    # if finishing time is >= to min time and <= max time
    if int(line[5]) >= time1 and int(line[5]) <= time2:
        name = line[1] # store runner's name
        country = line[3] # store runner's country
        gender = line[4] # store runner's gender
        time = line[5] # store runner's completion time

        # Writes the data to each columns
        col5.write(name)
        col6.write(country)
        col7.write(gender)
        col8.write(time)
