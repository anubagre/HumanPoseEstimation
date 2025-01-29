# Human Pose Detection using MediaPipe 

This project detects **human poses** in **images, videos, and live webcam streams** using **MediaPipe** that makes use of **Blaze Pose** detection method and is deployed with **Streamlit**.

---

## 📌 Features  
✅ Detects **33 body landmarks** using **BlazePose**  
✅ Works on **images, videos, and live webcam streams**  
✅ **Streamlit UI** for easy interaction  
✅ Real-time **pose tracking** with OpenCV  
✅ Simple deployment & lightweight inference  

---

## 🛠️ Files Structure  
📂 Human-Pose-Detection │── 📂 Images/ # Stores sample images │── 📂 Videos/ # Stores sample videos │── 📜 HME_live.py # Pose detection on live webcam feed │── 📜 HME_onimage.py # Pose detection on images │── 📜 HME_onvid.py # Pose detection on videos │── 📜 app.py # Streamlit app to run the project │── 📜 requirements.txt # Required dependencies │── 📜 README.md # Project documentation

---

## ⚙️ Installation & Setup  

🔹 **1. Clone the Repository**
git clone [https://github.com/your-repo/Human-Pose-Detection.git](https://github.com/anubagre/HumanPoseEstimation.git)

cd Human-Pose-Detection

🔹 **2. Install Dependencies**

pip install -r requirements.txt

🔹 **3. Run the Streamlit App**

streamlit run app.py

---

## 📷 How It Works

🔹 BlazePose is used for real-time pose detection.

🔹 OpenCV processes frames from images/videos/webcam.

🔹 Streamlit provides an interactive UI for users.

---

## 🛠️ Future Enhancements
🚀 Add pose classification for exercises (e.g., Yoga, Workouts)

🚀 Deploy as a Web App

🚀 Integrate gesture recognition
