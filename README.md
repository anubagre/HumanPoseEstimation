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

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/your-repo/Human-Pose-Detection.git
cd Human-Pose-Detection
🔹 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 3. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📷 How It Works
🔹 BlazePose is used for real-time pose detection.
🔹 OpenCV processes frames from images/videos/webcam.
🔹 Streamlit provides an interactive UI for users.

📁 Usage
🖼️ Pose Detection on Images
bash
Copy
Edit
python HME_onimage.py --image_path "Images/sample.jpg"
🎥 Pose Detection on Videos
bash
Copy
Edit
python HME_onvid.py --video_path "Videos/sample.mp4"
📷 Pose Detection in Real-Time (Webcam)
bash
Copy
Edit
python HME_live.py
🔧 Requirements
Python 3.7+
Streamlit
OpenCV
MediaPipe
NumPy

🛠️ Future Enhancements
🚀 Add pose classification for exercises (e.g., Yoga, Workouts)
🚀 Deploy as a Web App
🚀 Integrate gesture recognition