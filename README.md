
# Azure IoT Hub + Stream Analytics Pipeline

---

## Summary of Work

This project documents the complete setup of an Azure IoT telemetry pipeline. The goal was to configure an IoT Hub, register a virtual device, simulate telemetry using Python, and process that data in real time using Azure Stream Analytics, with results stored in Azure Blob Storage.

---

## Key Components Implemented

1. **Azure IoT Hub Creation**  
   Configured a secure cloud gateway using Azure IoT Hub.

2. **Device Provisioning**  
   Registered a virtual device with symmetric key authentication for telemetry transmission.

3. **Python-Based Telemetry Simulation**  
   Used a Python script to publish simulated temperature and humidity values to IoT Hub.

4. **Azure Stream Analytics Job**  
   Built a real-time data stream pipeline to process telemetry data from the IoT Hub.

5. **Azure Blob Storage Output**  
   Routed processed data into Blob Storage for persistence and analysis.

6. **Validation and Monitoring**  
   Verified end-to-end data flow using Azure Portal dashboards, logs, and metrics.

---

## Screenshots (See Report.pdf)

* IoT Hub Overview  
* Device Registration with Connection String  
* Python Script Console Output (Telemetry Sent)  
* Stream Analytics Job Configuration  
* Job Running Status  
* Blob Storage Output Validation  
* Live Message Monitoring Console  

---

## Reflection

> Completing this project offered hands-on experience with Azure IoT architecture. It deepened my understanding of cloud-based telemetry processing, secure device provisioning, and real-time data stream management. The debugging process and system integration provided valuable practical insight into scalable IoT solutions.

---

## Disclaimer

This is a **documentation-only project** with no hardware simulation.  
All telemetry was simulated in Python, and validation was done via screenshots and dashboard verification.

---

## Repo Contents

      azure-iot-pipeline/
      ├── iot_sender.py           — Python script to publish simulated telemetry
      ├── Report.pdf              — Full report with screenshots and workflow
      ├── README.md               — Project documentation and summary
      └── .gitignore              — Excludes keys, envs, and build artifacts

---

## Security Notice

Do not share or commit any real connection strings, keys, or credentials publicly.  
All values used in this project are academic placeholders for demonstration only.

---

## Technologies Used

- Azure IoT Hub  
- Azure Stream Analytics  
- Azure Blob Storage  
- Python 3.x  
- Azure IoT Device SDK

---
