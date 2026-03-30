🚦 Smart Traffic Light Control System
📌 Overview
This project presents a smart traffic light control system that dynamically adjusts signal timings based on real-time traffic density. The system uses computer vision (OpenCV & YOLO) for vehicle detection and an Arduino microcontroller for controlling traffic signals.

🎯 Features
🚗 Real-time vehicle detection using camera

🧠 AI-based detection using YOLO

⚡ Dynamic traffic signal control

🔌 Arduino-based LED signal system

📊 Traffic density comparison (Road A vs Road B)

🔄 Stable signal switching with smoothing

🏗️ System Architecture
The system consists of:

Camera (video input)

Image processing (OpenCV / YOLO)

Vehicle detection & counting

Decision-making logic

Arduino controller

Traffic light LEDs

⚙️ Tech Stack
Python

OpenCV

YOLOv8 (Ultralytics)

Arduino

Serial Communication

📁 Project Structure
traffic-light-project/
│
├── arduino/              # Arduino code
├── detection/            # OpenCV detection
├── yolo_detection/       # YOLO-based detection
├── camera_test/          # Camera testing scripts
├── requirements.txt      # Python dependencies
├── README.md
🚀 How to Run
🔹 1. Clone Repository
git clone https://github.com/YOUR_USERNAME/traffic-light-yolo.git
cd traffic-light-yolo
🔹 2. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
🔹 3. Install Dependencies
pip install -r requirements.txt
🔹 4. Run Detection
python detection/vehicle_detection.py
OR (YOLO version):

python yolo_detection/yolo_test.py
🔌 Arduino Setup
Connect LEDs:

Road A → Pins 8, 9, 10

Road B → Pins 5, 6, 7

Upload Arduino code

Ensure correct COM port in Python

🧠 Working Logic
Detect vehicles on both roads

Count vehicles (A & B)

Compare traffic density:

A > B → A GREEN, B RED

B > A → B GREEN, A RED

Equal → BOTH YELLOW

Send signal to Arduino

📊 Results
Accurate vehicle detection using OpenCV and YOLO

Smooth traffic signal switching

Improved traffic flow efficiency

Stable real-time performance

⚠️ Limitations
YOLO may misclassify toy vehicles

Lighting conditions affect detection

Requires camera calibration

🔮 Future Improvements
Train custom YOLO model for higher accuracy

Deploy on real traffic datasets

Add IoT/cloud integration

Multi-lane expansion

👥 Contributors
Arnav Singh

Ayush Kumar Bariyar

Aditi Prajapati

Ananya Kumari

📚 References
Smart Traffic Signal Control Using Computer Vision (IEEE, 2019)

Traffic Density Estimation Using Image Processing (IEEE, 2018)

Real-Time Vehicle Detection Using Deep Learning (IEEE, 2020)

IoT-Based Adaptive Traffic Signal Control (2020)

Environmental Benefits of Adaptive Traffic Systems (2020)

⭐ Final Note
This project demonstrates how AI + Embedded Systems can be combined to build intelligent and efficient traffic management solutions.

🔥 DONE
👉 This README is:

Clean ✅

Professional ✅

Panel-impressive ✅

GitHub-ready ✅
