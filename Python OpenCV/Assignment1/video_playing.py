import cv2

# Open the video file
cap = cv2.VideoCapture('video_file.webm')

# Check if video file was opened successfully
if not cap.isOpened():
    print("Error opening video file.")
    exit()

# Read the first frame from the video
ret, frame = cap.read()

# Loop through the frames until the end of the video is reached
while ret:
    # Display the frame
    cv2.imshow('Frame', frame)

    # Wait for 25 milliseconds and check if the 'q' key was pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Read the next frame from the video
    ret, frame = cap.read()

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
