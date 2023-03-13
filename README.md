# Pricing Module

A web application with a configurable pricing module that supports differential pricing.

The Web application has been made using DJANGO. The database used is the dbSQLite.

Functionalities for creating pricing_configs, creating base price system (for any particular config), creating addition price system, and creating time based multiplier system.

Admin can create various pricing configs, as well as enable and disable them as per their need.

## Installation
* Clone the repo
* Make sure Django is installed / or run the below command
```bash
pip install -r requirements.txt
```
* run the below commands
```bash
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```

## Admin interface and custom forms
Go to http://localhost:8000/admin
and type in the credentials as
```
username: daksh
password: Admin@123
```
To launch the admin portal of the application and from there you can access the models and insert values from there only instead of hitting the APIs mentioned below

## cURL

Here is the cURL that can be used to create pricing configs. User can create/list/delete/update pricing configs

```
curl --location 'localhost:8000/pricing-config' \
--header 'Content-Type: application/json' \
--data '{
    "name":"config 1",
    "is_enabled":true
}'
```

cURL to create base price system
```
curl --location 'localhost:8000/distance-base-price/' \
--header 'Content-Type: application/json' \
--data '{
    "pricing_config": 1,
    "distance_in_km": 3.0,
    "base_price": 80.0
}'
```

cURL to create distance additional price system
```
curl --location 'localhost:8000/distance-additional-price/' \
--header 'Content-Type: application/json' \
--data '{
    "pricing_config":1,
    "price_per_km":30
}'
```

cURL to create tmf
```
curl --location 'localhost:8000/time-multiplier-factor/' \
--header 'Content-Type: application/json' \
--data '{
    "pricing_config": 1,
    "time_in_minutes": 180,
    "multiplier_factor": 2.25
}'
```

cURL to calculate the price
```
curl --location 'localhost:8000/calculate-pricing/' \
--header 'Content-Type: application/json' \
--data '{
    "distance":10.00,
    "time":3
}'
```
** note that distance and time needs to be given while calculating the price in the request body

IDs of object of DAP/DBP/TMF/Pricing_configs can be appended after the url as path param to perform certain functions on them individually.
