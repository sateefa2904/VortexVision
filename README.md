# VortexVision: Real-Time Gesture-Controlled Image Spiral Using Computer Vision

**Creator:** Soli Ateefa
**Project Type:** Real-time multimedia interface, human-computer interaction, computer vision + graphics

---

## Project Overview

**VortexVision** simulates the nonlinear, fragmented way humans recall memories—through an interactive 3D vortex of images that swirls, collapses, and rotates based on your hand gestures in real time.

By combining **MediaPipe-based hand tracking** with **TouchDesigner’s real-time 3D rendering**, this system creates a futuristic photo interface reminiscent of AR/VR experiences and sci-fi memory visualizations. Our goal: to explore how intuitive body movements—like a swipe or pinch—can be used to dive into clusters of memories, simulating how thoughts spiral in and out of focus.

---

## Core Features

* **Real-Time Hand Tracking**: Uses [MediaPipe](https://google.github.io/mediapipe/) to detect 17 key landmarks per hand.
* **3D Vortex Rendering**: TouchDesigner displays a swirling image spiral where photos shift position and rotation based on gesture inputs.
* **Gesture Recognition**: Swipe left/right gestures classified using x-axis delta thresholds.
* **Live Python ↔ TouchDesigner Communication**: Open Sound Control (OSC) is used to send gesture data from Python scripts to TouchDesigner in real time.
* **Memory Simulation Design**: The vortex structure and gesture controls were intentionally chosen to mimic the hazy, non-linear feel of memory recall.

---

## Software and Tools

| Tool                     | Purpose                                                    |
| ------------------------ | ---------------------------------------------------------- |
| **Python**               | Frame processing, hand tracking, gesture classification    |
| **MediaPipe**            | Real-time landmark detection (joints, palms)               |
| **OpenCV**               | Video capture and frame manipulation                       |
| **TouchDesigner**        | 3D vortex rendering, interactive animation                 |
| **OSC Protocol**         | Real-time message passing between Python and TouchDesigner |
| **CHOPs/DATs/SOPs/TOPs** | Data + image handling within TouchDesigner                 |

---

## Architecture Overview

```mermaid
graph LR
    A[Webcam Capture] --> B[Python Processing]
    B --> C[MediaPipe Landmark Detection]
    C --> D[Gesture Classification]
    D --> E[OSC Messaging]
    E --> F[TouchDesigner]
    F --> G[Vortex Visualization Update]
```

* **Backend**: Python handles vision pipeline and transmits gesture data.
* **Frontend**: TouchDesigner receives OSC data and visualizes changes in real time.
* **Vortex Control**: Image spirals rotate or zoom based on gestures like swipe and pinch.

---

## Implemented Gestures

| Gesture                     | Effect                           |
| --------------------------- | -------------------------------- |
| **Swipe Left**              | Rotates vortex counter-clockwise |
| **Swipe Right**             | Rotates vortex clockwise         |
| *(Planned)* Pinch/Zoom      | Expand or collapse spiral        |
| *(Optional)* Face Detection | Filter images to only show faces |

Gesture logic was implemented using the x-delta between frames:

* Left swipe: Δx < -0.05
* Right swipe: Δx > 0.05

---

## Why a Vortex?

> "Memories aren’t linear—they’re messy, spiraling, interwoven."

* The vortex mimics how our brains surface images and thoughts during recall.
* Images buried deeper in the spiral symbolize older or less-accessed memories.
* Natural gestures like swiping feel more intuitive than keyboard or mouse input, emphasizing human-centered design.

---

## Challenges Faced

* **Full-stack complexity**: Bridging real-time vision, gesture logic, and 3D rendering.
* **TouchDesigner learning curve**: Custom CHOPs/DATs integration was tricky and required extensive documentation digging.
* **Integration hurdles**: While each component worked standalone, full gesture-to-vortex linkage required careful debugging.

---

## Future Improvements

* Enable **zoom/pinch gestures** for depth control
* Add **image filters** (e.g., only faces or scenes)
* Improve motion smoothing with Kalman or exponential filters
* Build a **TouchDesigner-native gesture classifier** for low-latency control

---

## How to Run (Basic Overview)

1. **Python Setup**:

   * Install dependencies: `pip install mediapipe opencv-python python-osc`
   * Run the hand gesture detection script (`gesture_tracker.py`)
2. **TouchDesigner**:

   * Open `photovortexcomponent.14.toe`
   * Make sure OSC In CHOP is listening on correct port
   * Watch the vortex respond in real time to gestures via webcam!

> Note: Ensure webcam access is granted and both Python and TouchDesigner are running simultaneously.

---

## Mockup Preview

> Imagine a spiral of floating photos in 3D space. Swipe your hand left and the images rotate like a Rolodex of memories. Swipe right and the spiral reverses. Pinch your fingers to zoom in on a memory—or collapse them to let it fade.

---

## Academic Relevance

This project showcases hands-on applications of:

* **Computer vision**
* **Human-computer interaction (HCI)**
* **3D rendering**
* **Signal processing and gesture classification**
* **Python ↔ multimedia software integration**

---

## Conclusion

**VortexVision** isn’t just a cool interface—it’s a statement on how we might one day access memories, art, and emotion through movement alone. We hope it inspires future explorations in AI-powered interaction design and immersive media storytelling.