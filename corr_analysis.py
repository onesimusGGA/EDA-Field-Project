import pandas as pd # type: ignore
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import the csv file
fieldwork_data = pd.read_csv("C:\GIS\Field Work Project\Fieldwork Data\Group_11_Data_01.csv")

# rename columns that have long characters
fieldwork_data = fieldwork_data.rename(columns={'_Get Coordinates of Feature_latitude':'lat',
                                               '_Get Coordinates of Feature_longitude':'long',
                                               '_Get Coordinates of Feature_altitude':'elevation',
                                               '_Get Coordinates of Feature_precision':'accuracy',
                                               'Feature to be mapped':'features',
                                               'What is the Environmental Hazard':'Env_Hazard',
                                               'Well_Water_Level___':'water_level'})

# confirm the new column names
print(fieldwork_data.columns)
print(fieldwork_data.shape)
print(fieldwork_data.head())

# subset the 'features' column into a new dataframe
# fieldwork_data_features = fieldwork_data['features']

# subset 'features' column with values of well using the .query() method and drop the 'Env_Hazard column'
well_water_data = fieldwork_data.query('features == "Well_Water_Level"').drop('Env_Hazard', axis=1)

# check the data
print(well_water_data.head())
print(well_water_data.shape)
print(well_water_data.describe())

# plot the elevation and water level data
#plt.scatter(well_water_data['elevation'], well_water_data['water_level'])
'''well_water_data.plot(x='elevation', y='water_level', kind='scatter')
plt.title('A Scatter Plot of Elevation Values Against Water Level Data')
plt.xlabel('Elevation')
plt.ylabel('Water Level')

# using seaborn to visualize the correlation and as well, plot the linear regression
sns.regplot(x='Elevation', y='water_level', data=well_water_data, fit_reg=True)
plt.title('Correlation and Linear Regression of Water Level Data Against DEM Values')
plt.show()

# print(well_water_data.head())
# print(well_water_data.corr())'''