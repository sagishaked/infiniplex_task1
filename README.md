# infiniplex_task1


# Application Setup Guide

## Overview
This repository contains a Flask-based web application that allows users to upload CSV files containing patient data. The application processes the data, keeps track of the latest records, and provides sorting functionalities.

##  Setup
Follow these exact instructions to set up and run the application on an **Ubuntu** machine.

### 1. Prerequisites
Ensure that the following dependencies are installed on the system:

- Python 3.8 or later
- pip (Python package manager)
- Flask
- pandas
- A web browser

If these are not installed, you can install them using:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 2. Clone the Repository
Fetch the latest code from the Git repository:
```bash
git clone <repository_url>
cd <repository_folder>
```
Replace `<repository_url>` with the actual Git repository URL and `<repository_folder>` with the directory name of the cloned repository.

### 3. Install Python Dependencies
Run the following command inside the project folder:
```bash
pip install -r requirements.txt
```
If the `requirements.txt` file does not exist, manually install the required libraries:
```bash
pip install flask pandas
```

### 4. Run the Flask Application
Start the application by running:
```bash
python3 app.py
```

### 5. Accessing the Application from Another Computer
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

### 6. Stopping the Application
To stop the application, press `Ctrl + C` in the terminal where it is running.

---
This completes the setup. The application should now be accessible from any computer on the network using the correct server IP and port 5000. 🚀

