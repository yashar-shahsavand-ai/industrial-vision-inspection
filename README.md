# Industrial Vision Inspection System

Real-time computer vision inspection pipeline for automated quality control using a standard camera and local inference.

---

## Overview

Manufacturing production lines require continuous quality inspection. Manual inspection is slow, inconsistent, and costly, especially for small and medium factories that cannot afford specialized industrial inspection hardware.

This project demonstrates a deployable **edge-AI inspection prototype** capable of detecting products and issuing a PASS/FAIL decision in real time using a webcam and a local object detection model.

The goal is to illustrate how a low-cost camera combined with machine learning can be integrated into an industrial workflow.

---

## Key Features

* Real-time video inspection
* Local inference (no cloud dependency)
* Continuous processing pipeline
* Visual detection overlay
* PASS / FAIL classification output
* Modular architecture for future PLC or automation integration

---

## System Architecture

Camera → Frame Preprocessing → Object Detection Model → Decision Logic → Visual Output

The system continuously reads frames from a camera, preprocesses them, performs object detection, and classifies each inspected item.

---

## Project Structure

```
industrial-vision-inspection
│
├── app/                # runnable application scripts
├── src/                # detection and preprocessing modules
├── models/             # placeholder for trained weights
├── data_sample/        # example images
├── requirements.txt    # dependencies
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/industrial-vision-inspection.git
cd industrial-vision-inspection
```

### 2. Install dependencies

(Recommended: Python 3.10+)

```
pip install -r requirements.txt
```

---

## Running the Inspection System

Start the real-time inspection:

```
python app/camera_inspection.py
```

Optional parameters:

```
--model yolov8n.pt
--confidence 0.5
--camera 0
```

Press **Q** to stop the system.

---

## Example Output

The system displays the live camera feed with detection overlay and a decision indicator:

* **NO DEFECT – PASS**
* **DEFECT DETECTED – FAIL**

This simulates an industrial inspection station where defective products can be removed from the production line.

---

## Design Goals

This project focuses on engineering practicality rather than research benchmarking:

* Run on consumer hardware
* Minimal setup
* Offline operation
* Easy integration into existing systems
* Demonstrate real-world feasibility

---

## Notes on Data and Models

This is a clean-room demonstration project.
It uses public pre-trained models and synthetic testing scenarios. No proprietary datasets, confidential models, or industrial data are included.

In a production environment, the detection model would be trained on domain-specific images collected from the target production line.

---

## Possible Extensions

* Custom-trained defect classifier
* Integration with PLC/Arduino
* Automatic rejection actuator
* Edge deployment (Jetson / industrial PC)
* Logging and statistics dashboard

---

## Author

Yashar Shahsavand
Machine Learning Engineer – Applied AI Systems

Available for relocation and international opportunities.
