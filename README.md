#mozioChallenge - Providers and Service Areas
Rest API - for create, update, delete and list objects

##Features
Create, Update, Delete and List Providers and Service Areas

### Other
* API DOCS available for each endpoint
* Unittest for each feature
* Django routine to bootstrap the system
* Fully modular, possibility to raise up the sources and also database

## Setting up environment

Homologated to run over Ubuntu 18.04, in this step you should have installed in your system: MySQL and Redis Cache Server

$sudo apt-get install redis mysql-server python3
$sudo apt-get install python3-venv python3-pip
$sudo python3 -m venv moziovenv
$source tf-venv/bin/activate 

1. cd <directory containing this file>
2. edit the file mozioChallenge/config.py with the right information regarding db
3. $venv/bin/pip install -r requirements.txt
4. $venv/bin/python manage.py start

## Endpoints

/providers/    (we can use filter for name, email, currency, phone and language)
/provider/<ID>
/service_areas/
/service_areas/?lat=<LAT>&lng=<LNG> (Using lat and lng filters to match all the service areas containing those points on its polygons)
/service_area/<ID>

### /providers/

Class ProviderList - views - Django DRF - 
Mozio Challenge provides Provider list and creation a new provider object

Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

Returns: List containing all providers

SAMPLE RETURN:
```
[
    {
        "id": 1,
        "name": "teste1",
        "email": "teste@teste.com",
        "phone": "2312312",
        "language": "PT",
        "currency": "BRL"
    }
]
```

### /provider/<ID>

SAMPLE QUERY:
```
/provider/1
```

Class ProviderDetail - views - Django DRF - 
Mozio Challenge provides Provider object update, deletion and object overview

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

Returns: single provider object matching the ID

SAMPLE RETURN:
```
{
    "id": 1,
    "name": "teste1",
    "email": "teste@teste.com",
    "phone": "2312312",
    "language": "PT",
    "currency": "BRL"
}
```

### /service_areas/
or
### /service_areas/?lat=<LAT>&lng=<LNG>

Service Area List
Class ServiceAreaList - views - Django DRF - 
Mozio Challenge provides Service Area list and creation a new ServiceArea object

Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

Returns: list containing all the service area objects or matching Lat and Lng in GEOJSON polygon

SAMPLE RETURN:
```
[
    {
        "id": 1,
        "name": "teste",
        "price": 11111.0,
        "area": {
            "type": "Feature",
            "properties": {
                "name": "Flemish Diamond",
                "area": 2947
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            3.55,
                            51.08
                        ],
                        [
                            4.36,
                            50.73
                        ],
                        [
                            4.84,
                            50.85
                        ],
                        [
                            4.45,
                            51.3
                        ],
                        [
                            3.55,
                            51.08
                        ]
                    ]
                ]
            }
        },
        "provider": 1
    }
]
```

### /service_area/<ID>

SAMPLE QUERY:
```
/service_area/1
```

Class ServiceAreaDetail - views - Django DRF - 
Mozio Challenge provides Service Area object update, deletion and object overview

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

Returns: single Service Area object matching ID criteria

SAMPLE RETURN:
```
{
    "id": 1,
    "name": "teste",
    "price": 11111.0,
    "area": {
        "type": "Feature",
        "properties": {
            "name": "Flemish Diamond",
            "area": 2947
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        3.55,
                        51.08
                    ],
                    [
                        4.36,
                        50.73
                    ],
                    [
                        4.84,
                        50.85
                    ],
                    [
                        4.45,
                        51.3
                    ],
                    [
                        3.55,
                        51.08
                    ]
                ]
            ]
        }
    },
    "provider": 1
}
```
