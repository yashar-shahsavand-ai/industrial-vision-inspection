# Industrial Vision Inspection System

## Problem

Manufacturing production lines require continuous quality inspection. Manual inspection is slow, inconsistent, and expensive, especially for small factories without dedicated automation systems.

## Solution

This project demonstrates a deployable computer vision inspection pipeline capable of detecting products using a standard camera and classifying them in real time.

The system simulates a production-line inspection setup and outputs a PASS/FAIL decision for each item.

## Features

* Real-time webcam inspection
* Object detection pipeline
* Continuous processing loop
* Simple decision logic for quality control
* Designed for edge or local hardware

## How to Run

Install dependencies:
pip install -r requirements.txt

Run the inspection:
python app/camera_inspection.py

Press Q to exit.

## Notes

This is a clean-room demonstration project built using public models and synthetic testing scenarios to illustrate a real-world industrial inspection architecture.
