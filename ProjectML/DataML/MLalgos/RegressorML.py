import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
# Path of the UC Davis bike usage file
ucdavis_bikes_file_path = r'C:\Users\bekhr\ProjectML\ProjectML\DataML\UCDavisbikedata.csv'
# Reading path of the file
ucdavis_bikes_data = pd.read_csv(ucdavis_bikes_file_path)
# Pulling data into a summary table
ucdavis_bikes_data.describe()
#Pulling out only top columns(Cuarto routes)
Cuarto_routes_data = ucdavis_bikes_data.iloc[0:3]
# Does not truncate resultant data matrix
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# Pulling out columns important for predictions
ucdavis_bike_data_compressed = Cuarto_routes_data[['Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking','Bikers']]
# Plotting the UC davis bike route data(on a mesh, to visualize the paths taken)

# Features for .predict
X = ucdavis_bike_data_compressed[['Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking']] 
# Prediction Question: What is the likely number of students a Nerd will encounter as in 'traffic'?
# Setting the Prediction Target 
y = ucdavis_bike_data_compressed['Bikers']
# Defining the model
ucdavis_model = DecisionTreeRegressor(random_state=1)
# Fitting the Model 
ucdavis_model.fit(X,y)
# Prediction based on feature X
ucdavis_model.predict(X)
# Splitting Data into Training and Validation Phases 

# Resulting prediction for traffic/bikers
print()

#Goal: to predict traffic levels based on factors such as past Traffic, Distance, Time, Classes(extra)

# Evaluating MAE on training data gives no error, which makes sense because no new data set is given, so the model achieves low in-sample error. 