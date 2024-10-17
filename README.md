# Label Studio ML Backend for Bacteria Detection

This project provides a Label Studio ML backend using a pre-trained YOLO model to assist in annotating microscopy images of bacteria.

## Setup Instructions

### Prerequisites
- Python 3.9+
- Docker (optional, for containerized deployment)

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the ML Backend
```bash
docker build -t bacteria-backend .
docker run -p 9090:9090 bacteria-backend
```

### Using Docker
```bash
docker build -t bacteria-backend .
docker run -p 9090:9090 bacteria-backend
```

### Connecting to Label Studio
1. Start Label Studio.
2. Go to the Machine Learning settings in your project.
3. Add a new model and provide the ML backend URL: http://localhost:9090.

### File Structure
* backend/: Code for the ML backend
* tests/: Unit tests
* config/: Configuration files
* Dockerfile: For containerizing the project
