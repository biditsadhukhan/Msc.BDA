import cv2

# Read input video file
cap = cv2.VideoCapture('input_video.mp4')

# Define the object tracker type
tracker = cv2.TrackerCSRT_create()

# Define the region of interest (ROI) around the object to track
success, frame = cap.read()
bbox = cv2.selectROI(frame, False)
tracker.init(frame, bbox)

# Define output video format and codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Loop through video frames
while True:
    # Read a frame from the input video
    success, frame = cap.read()
    if not success:
        break
    
    # Update the tracker with the current frame
    success, bbox = tracker.update(frame)
    
    # Draw a bounding box around the tracked object
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2, 1)
    
    # Write the frame with the bounding box to the output video
    out.write(frame)

    # Show the current frame with the bounding box
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources and close windows
cap.release()
out.release()
cv2.destroyAllWindows()
