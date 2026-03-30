import cv2
import numpy as np
import serial
import time

# -------- Arduino --------
arduino = serial.Serial('COM14', 9600, timeout=1)
time.sleep(2)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Camera not working")
    exit()

last_signal = ""
last_time = time.time()

while True:

    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]
    split = width // 2

    cv2.line(frame, (split, 0), (split, height), (0, 255, 0), 2)

    # -------- DETECTION --------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (13, 13), 0)

    _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

    kernel = np.ones((6, 6), np.uint8)

    thresh = cv2.erode(thresh, kernel, iterations=1)
    thresh = cv2.dilate(thresh, kernel, iterations=3)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # detection zone
    zone_y_min = int(height * 0.4)
    zone_y_max = int(height * 0.95)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    countA = 0
    countB = 0
    detected_centers = []

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if 1800 < area < 50000:

            x, y, w, h = cv2.boundingRect(cnt)

            if w < 30 or h < 30:
                continue

            cx = x + w // 2
            cy = y + h // 2

            if not (zone_y_min < cy < zone_y_max):
                continue

            too_close = False
            for (px, py) in detected_centers:
                if abs(px - cx) < 50 and abs(py - cy) < 50:
                    too_close = True
                    break

            if too_close:
                continue

            detected_centers.append((cx, cy))

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if cx < split:
                countA += 1
            else:
                countB += 1

    # -------- TRAFFIC LOGIC --------
    if countA > countB:
        signal = "A"
        text = "ROAD A GREEN"

    elif countB > countA:
        signal = "B"
        text = "ROAD B GREEN"

    else:
        signal = "N"
        text = "NORMAL MODE"

    # send only if changed or after delay
    if signal != last_signal or (time.time() - last_time > 30):
        arduino.write(signal.encode())
        last_signal = signal
        last_time = time.time()

    # -------- DISPLAY --------
    cv2.putText(frame, f"Road A: {countA}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Road B: {countB}", (split+20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, text, (width//2 - 150, height - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

    cv2.imshow("Traffic Detection", frame)
    cv2.imshow("Mask", thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()