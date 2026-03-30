from ultralytics import YOLO
import cv2
import serial
import time

# -------- Arduino Setup --------
arduino = serial.Serial('COM14', 9600, timeout=1)  # CHANGE PORT
time.sleep(2)

# -------- Load YOLO Model --------
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Camera not working")
    exit()

last_signal = ""

# 🔥 HISTORY FOR SMOOTHING
historyA = []
historyB = []

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # 🔥 LIGHT FIX
    frame = cv2.convertScaleAbs(frame, alpha=1.1, beta=10)

    height, width = frame.shape[:2]
    split = width // 2

    # detection zone
    zone_y_min = int(height * 0.3)
    zone_y_max = int(height * 0.95)

    # YOLO detection
    results = model(frame, conf=0.1, imgsz=640)

    countA = 0
    countB = 0

    detected_centers = []

    for r in results:
        for box in r.boxes:

            # 🔥 IGNORE CLASS (fix fluctuation)
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            # zone filter
            if not (zone_y_min < cy < zone_y_max):
                continue

            # 🔥 REMOVE DUPLICATES
            too_close = False
            for (px, py) in detected_centers:
                if abs(px - cx) < 60 and abs(py - cy) < 60:
                    too_close = True
                    break

            if too_close:
                continue

            detected_centers.append((cx, cy))

            # draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # counting
            if cx < split:
                countA += 1
            else:
                countB += 1

    # 🔥 STORE HISTORY
    historyA.append(countA)
    historyB.append(countB)

    if len(historyA) > 10:
        historyA.pop(0)
        historyB.pop(0)

    # 🔥 AVERAGE (SMOOTHING)
    avgA = sum(historyA) // len(historyA)
    avgB = sum(historyB) // len(historyB)

    # -------- DECISION LOGIC --------
    if avgA > avgB:
        signal = 'A'
        text = "ROAD A GREEN"

    elif avgB > avgA:
        signal = 'B'
        text = "ROAD B GREEN"

    else:
        signal = 'N'
        text = "NORMAL MODE"

    # 🔥 STABLE ARDUINO OUTPUT
    if signal != last_signal:
        arduino.write(signal.encode())
        last_signal = signal
        time.sleep(1)  # prevent flicker

    # -------- DISPLAY --------
    cv2.line(frame, (split, 0), (split, height), (255, 0, 0), 2)

    cv2.putText(frame, f"Road A: {avgA}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame, f"Road B: {avgB}", (split+20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame, text, (width//2 - 150, height - 20),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

    cv2.imshow("FINAL YOLO TRAFFIC SYSTEM", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()