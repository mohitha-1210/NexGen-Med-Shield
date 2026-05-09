# NexGen Med-Shield 🛡️

**NexGen Med-shield** is an integrated IoT and software solution designed to automate the identification and safe disposal of expired medications. This project aims to reduce medical waste and prevent the accidental or intentional consumption of compromised drugs.
---
## 🚀 Overview
Traditional medicine disposal is manual and error-prone. This system uses a combination of hardware sensors and a web-based dashboard to verify medicine authenticity and expiration status before triggering an automated disposal mechanism.

## 🛠️ Technical Stack
### **Software**
* **Frontend:** `Streamlit` (Python-based interactive dashboard)
* **Backend:** `Flask` (API for sensor-to-cloud communication)
* **Language:** Python 3.x, C++ (Arduino)

### **Hardware (Prototype Phase 1)**
* **Microcontroller:** Arduino Uno.
* **Sensors:** * **RGB Color Sensor:** To detect packaging/pill color signatures.
* **Load Cell:** To verify weight consistency against known standards.
---
  
## 🔬 Future Evolution: NIR Spectroscopy
While the current prototype successfully utilizes visual color sensing for proof-of-concept, the next iteration is designed to integrate **Near-Infrared (NIR) Spectroscopy**.

**Why the transition?**
* **Chemical Fingerprinting:** NIR can identify specific molecular vibrations, allowing the system to distinguish between authentic active ingredients and high-quality counterfeits.
* **Non-Destructive Testing:** NIR can "see" through blister packs and plastic containers, allowing for verification without breaking sterile seals.
* **High Accuracy:** Provides a professional, lab-grade verification method suitable for industrial pharmaceutical waste management.
---
  
## 📂 Project Structure
* `flaskscript.py`: The backend API handling data processing.
* `stream.py`: The Streamlit web interface for real-time monitoring.
* `/Arduino`: Contains the `.ino` files for sensor integration.
---
  
## 🏆 Recognition
* Successfully presented as a technical project at the **International Conference (March 2026)**.
* Won in the project presentation at the  International conference PEC2k26 held at Panimalar Engineering college.
---
  
### 👩‍💻 Developed by
* **[MOHITHA I]** - First Year B.E. Computer Science and Engineering, Panimalar Engineering College.
