import cv2 
import mediapipe as mp 
# Initialize Mediapipe Pose 
mp_pose = mp.solutions.pose 
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5) 
mp_drawing = mp.solutions.drawing_utils 

# Load an image 
image_path = "Images/pose.jpg"
image = cv2.imread(image_path) 
image_rgb = cv2.cvtColor (image, cv2.COLOR_BGR2RGB) 
# Perform pose estimation 
results = pose.process(image_rgb) 
# Draw landmarks only (no lines) 
if results.pose_landmarks: 
    print("Pose landmarks detected!") 
    # Extract landmark data 
    for idx, landmark in enumerate(results.pose_landmarks.landmark): 
        print(f"Landmark(idx): (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")
    for landmark in results.pose_landmarks.landmark: 
    # Get image dimensions 
        h,w,c= image.shape
        # Convert normalized coordinates to pixel coordinates 
        cx, cy = int (landmark.x * w), int (landmark.y * h) 
        # Draw the keypoints 
        cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1) 
        # Green color, filled c 
        # Optional: Draw landmarks on the image 
        annotated_image = image.copy() 
        mp_drawing.draw_landmarks(
        annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS) 
# Display the output image 
#cv2.imshow("Pose Landmarks", image) 
cv2.imshow("Pose drawing", annotated_image) 
cv2.waitKey (0) 
cv2.destroyAllWindows() 
#Release resources 
pose.close()