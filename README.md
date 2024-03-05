# ETL-Spotify-Python
This is a ETL process using Spotify API.
### Extract

[spoti](https://developer.spotify.com/documentation/web-api)

<img height="350" src="images/spotify-logo.png"  />

### Overview
This project involves the Extract, Transform, and Load (ETL) process for data obtained from the Spotify Web API. The primary endpoint used is "user-recently-played-song." Additionally, Flask is employed to deploy the API.

### Data
The following fields are extracted and processed:

ID
user_name
songs
played_at
created_at
updated_at

### Database Configuration
Workbench: MySQL
Database Hosting: Amazon RDS

### Deployment
The Flask application is hosted on an Amazon EC2 instance, providing a scalable and reliable environment for the API.

### ETL Process
Extract:

Data is extracted from the Spotify Web API using the "user-recently-played-song" endpoint.
Transform:

Data is processed and transformed to include relevant information such as ID, user_name, songs, played_at, created_at, and updated_at.
Load:

The transformed data is loaded into the MySQL database hosted on Amazon RDS.

### Technologies Used
Flask: Used for deploying the API.
MySQL: Database management system employed for storing the extracted and transformed data.
Amazon RDS: Provides a scalable and managed relational database hosting solution.
Amazon EC2: Hosting environment for the Flask application, ensuring reliable deployment.
Usage
To use this application, you can follow these steps:

Set up a MySQL database on Amazon RDS.
Deploy the Flask application on an Amazon EC2 instance.
Configure the application to connect to the MySQL database.
Run the ETL process to extract, transform, and load data from the Spotify Web API.
Feel free to customize the application based on your specific requirements and preferences.