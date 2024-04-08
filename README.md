# Tiedo - Simple Telematics Service for Cars

## Overview

Tiedo is a simple telematics service designed to gather, store, and retrieve GPS or other vehicle data. 
The aim is to create a service, or a template for one, that is lightweight, easily deployable and can be expandable with future additional features.


### Key Features
- **Single Microservice:** A single service component for handling GPS data.
- **Easy Installation:** Bash script for Linux systems and Docker support for portability.
- **Secure Data Transmission:** Token-based authentication.
- **Basic Testing and Monitoring:** Unit tests, health check endpoint, and logging.

## Installation

### Requirements
- Python 3.x
- SQLite (for database)

### Step 1: Clone the Repository
```bash
git clone https://github.com/halldorstefans/tiedo.git
cd tiedo
```

### Step 2: Run Installation Script (For Linux)

Make sure the script is executable
```bash
chmod +x install_local.sh
```

Run the installation script
```bash
./install_local.sh
```

This script will set up the necessary environment, install dependencies, and configure the service.

### Step 3: Start the service

With Python installed and the configuration set up, you can now start the telematics service:

```bash
python3 app.py
```

### Step 4: Verify Installation

To verify that the service is running correctly, open a web browser or use curl to access the health check endpoint:

```bash
curl http://localhost:5000/health
```

You should receive a response indicating the status of the service.

### Step 5: Test the API

See [sample usage example](#sample-usage-scenarios).

## API Documentation

### Endpoints

#### 1. Create Token
- **Endpoint:** `/auth/register` (POST)
- **Description:** Register vehicle and get authentication token.
- **Request Body:**
  ```json
  {
    "vehicle_id": "12345"
  }
  ```
- **Response:** 201 Created
  ```json
  {
    "token": <YOUR_API_TOKEN>
  }
  ```

#### 2. Receive GPS Data
- **Endpoint:** `/api/gps` (POST)
- **Description:** Receives GPS data from vehicles.
- **Authentication:** Token-based authentication
- **Request Body:**
  ```json
  {
    "vehicle_id": "12345",
    "timestamp": "2024-03-26T12:00:00Z",
    "latitude": 37.7749,
    "longitude": -122.4194
  }
  ```
- **Response:** 201 Created
  ```json
  {
    "message": "GPS data received and saved"
  }
  ```

#### 3. Retrieve GPS Data
- **Endpoint:** `/api/gps/{vehicle_id}` (GET)
- **Description:** Retrieves GPS data for a specific vehicle.
- **Authentication:** Token-based authentication
- **Response:** 200 OK
  ```json
  "gps_data": [
    {
      "id": 1,
      "vehicle_id": "12345",
      "timestamp": "2024-03-26T12:00:00Z",
      "latitude": 37.7749,
      "longitude": -122.4194
    },
    {
      "id": 2,
      "vehicle_id": "12345",
      "timestamp": "2024-03-26T12:15:00Z",
      "latitude": 37.7749,
      "longitude": -122.4194
    }
  ]
  ```

## Sample Usage Scenarios

### Scenario 1: Create a authentication token
Create a auth token for a vehicle with ID "12345":
```bash
curl -X POST http://localhost:5000/auth/register \
     -H "Content-Type: application/json" \
     -d '{
           "vehicle_id": "12345"
         }'
```

### Scenario 2: Sending GPS Data
Send GPS data for a vehicle with ID "12345":
```bash
curl -X POST http://localhost:5000/api/gps \
     -H "Authorization: <YOUR_API_TOKEN>" \
     -H "Content-Type: application/json" \
     -d '{
           "vehicle_id": "12345",
           "timestamp": "2024-03-26T12:00:00Z",
           "latitude": 37.7749,
           "longitude": -122.4194
         }'
```

### Scenario 3: Retrieving GPS Data
Retrieve GPS data for the vehicle with ID "12345":
```bash
curl -X GET http://localhost:5000/api/gps/12345 \
     -H "Authorization: <YOUR_API_TOKEN>"
```

---

For more details, refer to the [GitHub repository](https://github.com/halldorstefans/tiedo) for issue tracking, contributions, and further discussions.
