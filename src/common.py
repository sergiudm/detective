import cv2
import mediapipe as mp
import math

mpPose = mp.solutions.pose
pose = mpPose.Pose()


def is_sitting(landmarks):
    left_hip = landmarks[mpPose.PoseLandmark.LEFT_HIP.value]
    left_knee = landmarks[mpPose.PoseLandmark.LEFT_KNEE.value]
    left_ankle = landmarks[mpPose.PoseLandmark.LEFT_ANKLE.value]

    # Calculate angle at the left knee
    angle = calculate_angle(left_hip, left_knee, left_ankle)

    return angle < 140


def calculate_angle(a, b, c):
    a = [a.x, a.y]
    b = [b.x, b.y]
    c = [c.x, c.y]

    ab = [a[0] - b[0], a[1] - b[1]]
    cb = [c[0] - b[0], c[1] - b[1]]

    dot_product = ab[0] * cb[0] + ab[1] * cb[1]
    ab_magnitude = math.hypot(ab[0], ab[1])
    cb_magnitude = math.hypot(cb[0], cb[1])

    angle = math.acos(dot_product / (ab_magnitude * cb_magnitude))
    return math.degrees(angle)
