import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
#Path of the UC Davis bike usage file
ucdavis_bikes_file_path = r'C:\Users\bekhr\ProjectML\ProjectML\DataML\UCDavisbikedata.csv'
#Reading path of the file
ucdavis_bikes_data = pd.read_csv(ucdavis_bikes_file_path)
#Pulling data into a summary table
ucdavis_bikes_data.describe()
#Pulling out only top columns(Cuarto routes)
Cuarto_routes_data = ucdavis_bikes_data
#Does not truncate resultant data matrix
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#Pulling out columns important for predictions
ucdavis_newbike_data = Cuarto_routes_data[['Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking','Value']]
#Plotting the UC davis bike route data

#Revised data used for .predict 
ucdavis_newbike_data_fixed = ucdavis_newbike_data[['Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking']]
#Prediction Question: What is the likely number of students a Nerd will encounter as in 'traffic'?
#Setting the Prediction Target
y = ucdavis_newbike_data.Value 
#Setting the inputs/features
ucdavis_bike_features = ['Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking']
X = ucdavis_newbike_data[ucdavis_bike_features]
#Defining the model
ucdavis_model = DecisionTreeRegressor(random_state=1)
#Training the model based on the non-NaN and NaN values to prevent NaN errors
X_y_basednonNaN_values = X[y.notna()] #splitting y-based non-NaN values from ucdavis_newbike_data(ex. Values[300,NaN,700] -> [300,700])
y_x_basednonNaN_values = y[y.notna()] #splitting x-based non-NaN values or all data under defined features in the same data
X_y_basedNaN_values= X[y.isna()] #splitting y-based NaN values to predict them 
#Fitting the Model
ucdavis_model.fit(X_y_basednonNaN_values, y_x_basednonNaN_values)
#Predict the NaN values
y_nan_pred = ucdavis_model.predict(X_y_basedNaN_values)
print(f'Making prediction for {ucdavis_newbike_data_fixed}') 
#print(f"The likely number of students a Cuarto resident will encounter from path 2 to class is {y_nan_pred}") 
#Success! -> Model chose 704 instead of 1,544 since 704 resembles Cuarto3 most. The actual value is 789
print(f"For a Nerd who is Helping another Nerd to move a heavy package to Miller Hall, the number of bikes encountered is {y_nan_pred}")
#Correct value: 515(biased)
#Fail, needs more layers and reiterations -> Model chose 2184 instead of something close to 515 -> thinks only of initial encounter, not last.