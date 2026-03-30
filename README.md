# 🚦 Smart Traffic Light Control System

## 📌 Overview
This project presents a smart traffic light control system that dynamically adjusts signal timings based on real-time traffic density. It uses computer vision techniques (OpenCV & YOLO) for vehicle detection and an Arduino microcontroller to control traffic signals.

---

## 🎯 Features
- Real-time vehicle detection using camera
- AI-based detection using YOLOv8
- Dynamic traffic signal control
- Arduino-based LED traffic system
- Traffic density comparison (Road A vs Road B)
- Stable signal switching using smoothing

---

## 🏗️ System Architecture
- Camera (Video Input)
- Image Processing (OpenCV / YOLO)
- Vehicle Detection & Counting
- Decision-Making Logic
- Arduino Controller
- Traffic Light LEDs

---

## ⚙️ Tech Stack
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- Arduino
- Serial Communication

---

## 📁 Project Structure
traffic-light-project/
│
├── arduino/ # Arduino code
├── detection/ # OpenCV detection
├── yolo_detection/ # YOLO-based detection
├── camera_test/ # Camera testing scripts
├── requirements.txt # Python dependencies
├── README.md
## 🔌 Arduino Setup
- Road A LEDs → Pins 8, 9, 10  
- Road B LEDs → Pins 5, 6, 7  
- Upload Arduino code before running Python  
- Set correct COM port in Python code  

---

## 🧠 Working Logic
- Detect vehicles using camera
- Count vehicles on Road A and Road B
- Compare traffic density:
  - A > B → A GREEN, B RED
  - B > A → B GREEN, A RED
  - Equal → BOTH YELLOW
- Send signal to Arduino via serial communication

---

## 📊 Results
- Accurate vehicle detection using OpenCV and YOLO
- Stable and smooth traffic signal switching
- Real-time system performance achieved
- Efficient traffic flow management

---

## ⚠️ Limitations
- YOLO may misclassify toy vehicles
- Lighting conditions affect detection accuracy
- Requires proper camera positioning

---

## 🔮 Future Improvements
- Train custom YOLO model
- Improve detection accuracy
- Add IoT/cloud integration
- Expand to multi-lane traffic system

---

## 👥 Contributors
- Arnav Singh  
- Ayush Kumar Bariyar  
- Aditi Prajapati  
- Ananya Kumari  

---

## 📚 References
1. Smart Traffic Signal Control Using Computer Vision (IEEE, 2019)  
2. Traffic Density Estimation Using Image Processing (IEEE, 2018)  
3. Real-Time Vehicle Detection Using Deep Learning (IEEE, 2020)  
4. IoT-Based Adaptive Traffic Signal Control (2020)  
5. Environmental Benefits of Adaptive Traffic Systems (2020)  

---

## ⭐ Final Note
This project demonstrates how AI and embedded systems can be combined to create intelligent traffic management solutions.
