# AzureIoT + Stream Analytics Pipeline

--------------------------------------------------------------------------------------

 Summary of Work
 This project documents the end-to-end setup of an Azure IoT telemetry pipeline. The objective was to configure an IoT Hub, register a virtual device, simulate telemetry data using Python, and process this data using Azure Stream Analytics with storage output.
 
--------------------------------------------------------------------------------------

Key Components Implemented

1. Azure IoT Hub Creation
Configured a new IoT Hub instance to serve as a secure cloud gateway.

2. Device Provisioning
Registered an IoT device with symmetric key authentication to securely transmit telemetry.

3. Python-Based Telemetry Simulation
Used a Python script to generate and publish random temperature and humidity readings to the IoT Hub.

4. Azure Stream Analytics Job
Set up a Stream Analytics pipeline to consume IoT telemetry in real time and route it to an output.

5. Azure Blob Storage Output
Configured Azure Blob Storage as the data sink for processed telemetry data.

6. Validation and Monitoring
All steps were verified using Azure Portal metrics, console outputs, and screenshots, ensuring reliable data flow.

--------------------------------------------------------------------------------------
Screenshots (Included in PDF Report)

  IoT Hub Overview
  Device Registration with Connection String
  Python Script Console Output (Telemetry Sent)
  Stream Analytics Job Configuration
  Job Running Status
  Blob Storage Output Validation
  Live Message Monitoring Console
  
--------------------------------------------------------------------------------------
Reflection

Completing this project gave me practical exposure to building cloud-based IoT pipelines. I learned how various Azure components — from device provisioning to real-time analytics — integrate to form a scalable solution. Debugging connection issues and understanding how telemetry flows between services gave me a deeper appreciation for cloud infrastructure and IoT development.

--------------------------------------------------------------------------------------

Disclaimer

This project does not include hardware simulation. All telemetry was generated via Python scripts, and all results are demonstrated through configuration and monitoring screenshots provided in the  report.

--------------------------------------------------------------------------------------

Repo Contents

azure-iot-pipeline/
iot_sender.py — Python script to publish simulated telemetry
InClass_10_Report.pdf — Full report with screenshots and workflow
README.md — Project overview
.gitignore — Excludes keys, envs, and build artifacts 

-------------------------------------------------------------------------------------- 

Security Notice

Do not share or commit connection strings, keys, or credentials publicly.
The connection string in the report is for academic demonstration only.

--------------------------------------------------------------------------------------

Technologies Used

Azure IoT Hub
Azure Stream Analytics
Azure Blob Storage
Python 3.x
Azure IoT Device SDK
