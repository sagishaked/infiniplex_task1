# infiniplex_task1

## Application Setup Guide

### Overview
This repository contains a Flask-based web application that allows users to upload CSV files containing patient data. The application processes the data, keeps track of the latest records, and provides sorting functionalities. It ensures that previous patient outcomes are archived while maintaining a clean and accessible interface.

---

## Setup
Follow these exact instructions to set up and run the application on an Ubuntu machine.

### 1. Prerequisites
Ensure that the following dependencies are installed on the system:

- Python 3.8 or later
- `pip` (Python package manager)
- `venv` for virtual environment management
- A web browser

If these are not installed, you can install them using:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### 2. Clone the Repository
Fetch the latest code from the Git repository:

```bash
git clone https://github.com/sagishaked/infiniplex_task1
cd infiniplex_task1
```

### 3. Set Up a Virtual Environment
It is recommended to use a virtual environment to install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Python Dependencies
Ensure the required dependencies are installed:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist, manually install the necessary packages:

```bash
pip install flask pandas
```

### 5. Run the Flask Application
Start the application by running:

```bash
flask run --host=0.0.0.0 --port=5000
```

If this command does not work, ensure that `FLASK_APP` is set:

```bash
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```

### 6. Accessing the Application from Another Computer
Once the application starts, it will be accessible from other computers in the same network.

#### 1. Find the Ubuntu Machine’s IP Address
Run the following command on the Ubuntu machine:

```bash
hostname -I | awk '{print $1}'
```

This will return an IP address such as `192.168.1.100`. Use this IP to access the application from another computer.

#### 2. Access the Application
On another computer connected to the same network, open a web browser and enter:

```
http://<server_ip>:5000/
```

Replace `<server_ip>` with the actual IP address obtained in the previous step.

### 7. Stopping the Application
To stop the application, press `Ctrl + C` in the terminal where it is running. If you are using a virtual environment, deactivate it with:

```bash
deactivate
```

---
