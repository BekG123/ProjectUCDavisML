import gpxpy
import csv
import os

#Define the file path
file_path = 'GraphHopper-Track-2024-08-23-2km.gpx'

# Open the GPX file
with open(file_path, 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)
# Create a CSV file
with open('UCDavisSegundoSocialSciMillerHall.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['latitude', 'longitude', 'elevation', 'time'])

    # Write data to CSV
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                writer.writerow([point.latitude, point.longitude, point.elevation, point.time])
