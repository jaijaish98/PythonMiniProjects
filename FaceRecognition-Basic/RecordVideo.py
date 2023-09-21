import cv2

cap = cv2.VideoCapture(0)

# Automatically grab width and height from video feed
# (returns float which we need to convert to integer for later on!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# MACOS AND LINUX: *'XVID' (macOS users may want to try VIDX as well just in case)
# WINDOWS *'VIDX'
writer = cv2.VideoWriter('/Users/jayendrans/jaijaish98/Work/Programming/Python/Python Mini '
                         'Projects/FaceRecognition-Basic/Videos/WebCamRecordings/jai_capture.mp4',
                         cv2.VideoWriter_fourcc(*'XVID'), 25, (width, height))

# This loop keeps recording until you hit Q or escape the window
# You may want to instead use some sort of timer, like from time import sleep and then just record for 5 seconds.

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Write the video
    writer.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
