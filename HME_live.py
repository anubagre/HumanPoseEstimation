import cv2 
import mediapipe as mp 

# Initialize Mediapipe Pose 
mp_pose = mp.solutions.pose 
pose = mp_pose.Pose(static_image_mode=False, model_complexity=0, enable_segmentation=False, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils #for drawing landmarks

# Capture Video: Replace with 'path_to_video.mp4' for a file or 0 for webcam
#video_src="Videos\run.mov"
cap = cv2.VideoCapture(0)

# Set video resolution for webcam (optional, adjust as needed for your laptop) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize MediaPipe Pose 
with mp_pose.Pose(static_image_mode=False, model_complexity=0, enable_segmentation=False, min_detection_confidence=0.5):
    while cap.isOpened(): 
        ret, frame = cap.read() 
        if not ret: 
            print("Video capture ended.") 
            break 

        # Flip frame horizontally for a mirror-like effect (optional) 
        frame = cv2.flip(frame, 1)

        #convert to RGB
        frame_rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        # Process the frame with MediaPipe Pose 
        results = pose.process(frame_rgb) 
        # Draw landmarks on the frame 
        if results.pose_landmarks: 
            mp_drawing.draw_landmarks ( 
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
            mp_drawing.DrawingSpec (color=(0, 255, 0), thickness=2, circle_radius=2), 
            mp_drawing.DrawingSpec (color=(0, 0, 255), thickness=2, circle_radius=2) 
            )

        # Resize frame to fit the screen (optional) 
        display_frame = cv2.resize(frame, (960, 540)) 
        # Adjust width and height as per your screen 
        # Display the processed frame 
        cv2.imshow('Pose Estimation', display_frame) 
        # Break loop if 'q' is pressed 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

# Release resources 
cap.release () 
#cv2.destroyAllWindows ()
#pose.close()