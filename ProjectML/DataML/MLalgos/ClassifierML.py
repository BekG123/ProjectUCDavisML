# -*- coding: utf-8 -*-
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
#Path of the UC Davis bike usage file
ucdavis_bikes_file_path = r'C:\Users\bekhr\ProjectML\ProjectML\DataML\UCDavisbikedata.csv'
#Reading path of the file
ucdavis_bikes_data = pd.read_csv(ucdavis_bikes_file_path) #df = ucdavis_bikes_data
#Pulling data into a summary table
ucdavis_bikes_data.describe()
#Pulling out only top columns(Cuarto routes)
Cuarto_routes_data = ucdavis_bikes_data.iloc[3:6]
#Does not truncate resultant data matrix
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#Pulling out columns important for prediction 
ucdavis_newbike_data = Cuarto_routes_data[['Routes','Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking','Value']] #-> new dataframe aka df, excludes strings
#Plotting the UC davis bike route data

#Revised data used for .predict 
ucdavis_newbike_data_fixed = ucdavis_newbike_data[['Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking','Value']]
#Prediction Question: Which path is the best for a Cuarto resident?
#Setting the Prediction Target
y = ucdavis_newbike_data[['Routes']].values.ravel()
#Setting the inputs/features
ucdavis_bike_features = ['Starting Latitude','Starting Longtitude',
                                                'Waypoint 1(latitude)','Waypoint 1(longtitude)','Waypoint 2(latitude)','Waypoint 2(longtitude)','Waypoint 3(latitude)','Waypoint 3(longtitude)',
                                                    'Ending Latitude', 'Ending Longtitude',
                                                        'Distance','TimeBiking','Value']
X = ucdavis_newbike_data[ucdavis_bike_features]
#Using a random forest classifier to pick best route for Cuarto residents
ucdavis_model = RandomForestClassifier()
#Fitting the model
ucdavis_model.fit(X,y)
#Predicting the best route using average probability
y_best_route_prob = ucdavis_model.predict_proba(X)
average_prob = np.mean(y_best_route_prob, axis=0)
best_route_index = np.argmax(average_prob)
y_best_route = ucdavis_model.classes_[best_route_index]
#Result
print(f"The data we analyzed is {ucdavis_newbike_data_fixed}")
print(f"The best route(highest avg. probability) for a Tercero resident is {y_best_route}")
print(f"The probability matrix is {y_best_route_prob}")
print(f"The average probability for each route is: {average_prob}")
