import cv2
from IPython.display import Video, display

# Read the captured video
video = cv2.VideoCapture("video.mp4")

if not video.isOpened():
    print("Error: Video not found")
else:
    print("Video opened successfully")
    video.release()

# Display normal video
print("Normal Motion")
display(Video("video.mp4", embed=True))

# Display slow motion
print("Slow Motion")
display(Video("video.mp4", rate=0.5, embed=True))

# Display fast motion
print("Fast Motion")
display(Video("video.mp4", rate=2.0, embed=True))