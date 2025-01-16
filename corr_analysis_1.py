import pandas as pd # type: ignore
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import the csv file
fieldwork_data = pd.read_csv("C:\GIS\Field Work Project\Fieldwork Data\Group_11_Data_01.csv")

# rename columns that have Long characters and drop the 'start' and 'end' columns'
fieldwork_data = fieldwork_data.rename(columns={'_Get Coordinates of Feature_latitude':'Lat',
                                               '_Get Coordinates of Feature_longitude':'Long',
                                               '_Get Coordinates of Feature_altitude':'Elevation',
                                               '_Get Coordinates of Feature_precision':'Accuracy',
                                               'Feature to be mapped':'Features',
                                               'What is the Environmental Hazard':'Env_Hazard',
                                               'Well_Water_Level___':'Well_Water_Level'})
fieldwork_data.drop(['start', 'end'], axis=1, inplace=True)

# Drop unnecessary solumns and create unique dataframes for each features simultaneously
Dumpsite_data = fieldwork_data.query('Features == "Illegal Dumpsites"').drop(['Env_Hazard', 'Well_Water_Level'], axis=1)
Env_Hazard_Data = fieldwork_data.query('Features == "Environmental Hazards"').drop('Well_Water_Level', axis=1)
Telephone_Mast_Data = fieldwork_data.query('Features == "Telephone Masts"').drop(['Env_Hazard', 'Well_Water_Level'], axis=1)
Transformer_Data = fieldwork_data.query('Features == "Transformer"').drop(['Env_Hazard', 'Well_Water_Level'], axis=1)
Well_Water_Data = fieldwork_data.query('Features == "Well_Water_Level"').drop('Env_Hazard', axis=1)

'''print(fieldwork_data.head())
print(Dumpsite_data.columns)
print(Env_Hazard_Data.columns)
print(Telephone_Mast_Data.columns)
print(Transformer_Data.columns)
print(Well_Water_Data.columns)'''


# Calculate the basic statistical values for the numerical columns using the agg() function
functions = ['count', 'mean', 'median', 'std', 'var', 'min', 'max']
summary_stat_Env = Env_Hazard_Data.groupby('Env_Hazard')[['altitude', 'precision']].agg(functions)
summary_stat_Dump = Dumpsite_data[['altitude', 'precision']].agg(functions)
summary_stat_Mast = Telephone_Mast_Data[['altitude', 'precision']].agg(functions)
summary_stat_Trans = Transformer_Data[['altitude', 'precision']].agg(functions)
summary_stat_Well = Well_Water_Data[['altitude', 'precision', 'Well_Water_Level']].agg(functions)

'''print(summary_stat_Env)
print(summary_stat_Dump)
print(summary_stat_Mast)
print(summary_stat_Trans)
print(summary_stat_Well)'''


# Create a histogram graph to visualize the distribution of the numerical columns
'''Well_Water_Data[['altitude', 'Well_Water_Level']].hist(bins=15)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()
plt.show()'''

# Create a box plot to visualize the distribution of the numerical columns
'''plt.boxplot(Well_Water_Data['altitude'])
plt.title('Box Plot of Elevation Values')
plt.ylabel('Elevation')
plt.show()'''


# Sort the DataFrame by latitude or longitude to create a profile along a specific direction
Transformer_Data.sort_values(by='longitude')  # Or sort by longitude

# Plot the elevation profile
Transformer_Data.plot(x='longitude', y='altitude')
plt.xlabel('Longitude')
plt.ylabel('Elevation (m)')
plt.title('Elevation Profile')
plt.show()