# Tennis Recovery Robot

An autonomous robot that finds tennis balls on a court and collects them. It runs on a Raspberry Pi with a mecanum-wheel chassis (Hiwonder), uses computer vision to detect balls, and uses ultrasonic sonar to avoid obstacles.

This repository has the robot-side code from my computer vision and robotics research at Cal Poly Pomona's SoftCom Lab.

## What's here

| File | What it does |
|---|---|
| `RaspberryPi/roboflow_cameratest.py` | Reads the live camera feed and runs a trained tennis-ball detection model on frames in a background thread, so the video doesn't freeze while the model runs. It draws a bounding box around each ball and saves the annotated frames. |
| `RaspberryPi/main.py` | Sets up the mecanum chassis and sonar, then runs a control loop that stops the robot when an obstacle comes within the safety distance. |

## Status

Work in progress. Detection and obstacle avoidance work as separate modules. Next I'll combine them so the robot steers toward the nearest detected ball, then add the collection mechanism.

## Running

On the Raspberry Pi, with the Hiwonder SDK installed:

```bash
export ROBOFLOW_API_KEY=...   # your own key
python3 RaspberryPi/roboflow_cameratest.py   # camera + detection
python3 RaspberryPi/main.py                  # chassis + sonar
```

## Built with

Python · OpenCV · Roboflow Inference · Raspberry Pi · Hiwonder SDK
