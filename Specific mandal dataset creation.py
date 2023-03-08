import pandas as pd
import os

# specify the folder containing the CSV files
folder = 'Telangana weather'

# specify the name of the new CSV file
new_file = 'adilabad.csv'

# list to hold the data frames from each CSV file
df_list = []

# list of month names in the correct order
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']

# loop through each month name
for month in months:
    # construct the file name for the CSV file for that month
    file = f"TS Weather data {month} 2022.csv"
    file_path = os.path.join(folder, file)
    # check if the file exists
    if os.path.exists(file_path):
        print("yes")
        # read the CSV file into a data frame
        df = pd.read_csv(file_path)
        # select only the rows where the district is 'Adilabad' and the mandal is 'Adilabad rural'
        df = df[(df['District'] == 'Adilabad') & (df['Mandal'] == 'Adilabad Rural')]
        # add the filtered data frame to the list
        df_list.append(df)

# concatenate all the data frames into a single data frame
result = pd.concat(df_list)

# write the result to a new CSV file
result.to_csv(new_file, index=False)
