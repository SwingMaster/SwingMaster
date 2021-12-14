import threading

import cv2
from math import sqrt
import mediapipe as mp
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.shortcuts import render, reverse
from django.views.decorators import gzip
from collections import defaultdict

off = 0
status_count = 0
score = 30

def home(request):
    context = {}
    return render(request, 'camera_home.html', context)

def base(request):
    return render(request, 'camera_base.html')

class VideoCamera(object):
    def __init__(self, request):
        self.video = cv2.VideoCapture(0)
        self.cnt = 0
        self.step = 0
        self.total_landmarks = defaultdict(list)
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.total_landmarks = defaultdict(list)
        self.frame_size = (int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        (self.grabbed, self.frame) = self.video.read()

        threading.Thread(target=self.update, args=()).start()


    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    # def save_landmarks(self):
    #     try:
    #         self.left_shoulder = self.results.pose_landmarks.landmark[11]
    #         self.right_shoulder = self.results.pose_landmarks.landmark[12]
    #         self.left_elbow = self.results.pose_landmarks.landmark[13]
    #         self.right_elbow = self.results.pose_landmarks.landmark[14]
    #         self.left_wrist = self.results.pose_landmarks.landmark[15]
    #         self.right_wrist = self.results.pose_landmarks.landmark[16]
    #         self.left_hip = self.results.pose_landmarks.landmark[23]
    #         self.right_hip = self.results.pose_landmarks.landmark[24]
    #         self.left_knee = self.results.pose_landmarks.landmark[25]
    #         self.right_knee = self.results.pose_landmarks.landmark[26]
    #
    #         self.total_landmarks['left_shoulder'].append([self.left_shoulder.x, self.left_shoulder.y])
    #         self.total_landmarks['right_shoulder'].append([self.right_shoulder.x, self.right_shoulder.y])
    #         self.total_landmarks['left_elbow'].append([self.left_elbow.x, self.left_elbow.y])
    #         self.total_landmarks['right_elbow'].append([self.right_elbow.x, self.right_elbow.y])
    #         self.total_landmarks['left_wrist'].append([self.left_wrist.x, self.left_wrist.y])
    #         self.total_landmarks['right_wrist'].append([self.right_wrist.x, self.right_wrist.y])
    #         self.total_landmarks['left_hip'].append([self.left_hip.x, self.left_hip.y])
    #         self.total_landmarks['right_hip'].append([self.right_hip.x, self.right_hip.y])
    #         self.total_landmarks['left_knee'].append([self.left_knee.x, self.left_knee.y])
    #         self.total_landmarks['right_knee'].append([self.right_knee.x, self.right_knee.y])
    #     except:
    #         pass

    def address(self):
        global status_count, score

        cv2.putText(self.frame, text='No start_trigger', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=2.5, color=(255, 255, 255), thickness=7)

        print('1. not address')
        try:
            self.left_hip = self.results.pose_landmarks.landmark[23]
            self.right_hip = self.results.pose_landmarks.landmark[24]
            self.left_wrist = self.results.pose_landmarks.landmark[15]
            self.right_wrist = self.results.pose_landmarks.landmark[16]
            self.dist_hip = sqrt((self.left_hip.x - self.right_hip.x)**2 + (self.left_hip.y - self.right_hip.y)**2)
            self.dist_wrist = sqrt((self.left_wrist.x - self.right_wrist.x)**2 + (self.left_wrist.y - self.right_wrist.y)**2)

            if ((self.right_hip.x < self.right_wrist.x and self.left_hip.x > self.left_wrist.x) and (self.dist_hip > self.dist_wrist)) and status_count == 0:
                status_count += 1
                print('1. address')
                cv2.putText(self.frame, text='1. address', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=2.5, color=(255, 255, 255), thickness=7)
                score += 10
        except:
            pass

    def backSwing(self):
        global status_count, score

        print('2. not backSwing')

        try:
            self.right_hip = self.results.pose_landmarks.landmark[24]
            self.right_wrist = self.results.pose_landmarks.landmark[16]
            self.left_wrist = self.results.pose_landmarks.landmark[15]
            self.right_elbow = self.results.pose_landmarks.landmark[14]
            self.left_elbow = self.results.pose_landmarks.landmark[13]
            self.right_shoulder = self.results.pose_landmarks.landmark[12]
            self.left_shoulder = self.results.pose_landmarks.landmark[11]

            if (status_count == 1) and (self.right_hip.x > self.right_wrist.x) and (self.right_hip.x > self.left_wrist.x) and (self.right_elbow.x < self.right_shoulder.x) and (self.left_elbow.x < self.left_shoulder.x) and (self.right_elbow.y > self.right_shoulder.y) and (self.left_elbow.y > self.left_shoulder.y):
                status_count += 1
                print('2. backSwing')
                cv2.putText(self.frame, text='2. backSwing', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=2.5, color=(255, 255, 255), thickness=7)
                score += 10
        except:
            pass

    def topSwing(self):
        global status_count, score

        print('3. not topSwing')

        try:
            self.right_hip = self.results.pose_landmarks.landmark[24]
            self.right_wrist = self.results.pose_landmarks.landmark[16]
            self.left_wrist = self.results.pose_landmarks.landmark[15]
            self.right_elbow = self.results.pose_landmarks.landmark[14]
            self.left_elbow = self.results.pose_landmarks.landmark[13]
            self.right_shoulder = self.results.pose_landmarks.landmark[12]
            self.left_shoulder = self.results.pose_landmarks.landmark[11]

            if (status_count == 2) and (self.right_hip.x > self.right_wrist.x) and (self.right_hip.x > self.left_wrist.x) and (self.right_shoulder.y > self.right_wrist.y) and (self.right_shoulder.y > self.left_wrist.y) and (self.right_elbow.x < self.right_shoulder.x) and (self.left_elbow.x < self.left_shoulder.x):
                status_count += 1
                print('3. topSwing')
                cv2.putText(self.frame, text='3. topSwing', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=2.5, color=(255, 255, 255), thickness=7)
                score += 10
        except:
            pass

    def downSwing(self):
        global status_count, score

        print('4. not downSwing')

        try:
            self.right_hip = self.results.pose_landmarks.landmark[24]
            self.right_wrist = self.results.pose_landmarks.landmark[16]
            self.left_wrist = self.results.pose_landmarks.landmark[15]
            self.right_elbow = self.results.pose_landmarks.landmark[14]
            self.left_elbow = self.results.pose_landmarks.landmark[13]
            self.right_shoulder = self.results.pose_landmarks.landmark[12]
            self.left_shoulder = self.results.pose_landmarks.landmark[11]

            if (status_count == 3) and (self.right_hip.x > self.right_wrist.x) and (
                    self.right_hip.x > self.left_wrist.x) and (self.right_wrist.x < self.right_shoulder.x) and (
                    self.left_wrist.x < self.left_shoulder.x) and (self.right_wrist.y > self.right_shoulder.y) and (
                    self.left_wrist.y > self.left_shoulder.y):
                status_count += 1
                print('4. downSwing')
                cv2.putText(self.frame, text='4. downSwing', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=2.5, color=(255, 255, 255), thickness=7)
                score += 10
        except:
            pass

    def impact(self):
        global status_count, score

        print('5. not impact')

        try:
            self.left_hip = self.results.pose_landmarks.landmark[23]
            self.right_hip = self.results.pose_landmarks.landmark[24]
            self.left_wrist = self.results.pose_landmarks.landmark[15]
            self.right_wrist = self.results.pose_landmarks.landmark[16]
            self.left_ankle = self.results.pose_landmarks.landmark[27]
            self.right_ankle = self.results.pose_landmarks.landmark[28]

            self.dist_ankle = sqrt((self.left_ankle.x - self.right_ankle.x) ** 2 + (self.left_ankle.y - self.right_ankle.y) ** 2)
            self.dist_wrist = sqrt(
                (self.left_wrist.x - self.right_wrist.x) ** 2 + (self.left_wrist.y - self.right_wrist.y) ** 2)

            if ((self.right_ankle.x < self.right_wrist.x and self.left_ankle.x > self.left_wrist.x)) and (self.dist_ankle > self.dist_wrist) and (self.right_wrist.y > self.right_shoulder.y) and (
                    self.left_wrist.y > self.left_shoulder.y) and status_count == 4:
                status_count += 1
                print('5. impact')
                cv2.putText(self.frame, text='5. impact', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=2.5, color=(255, 255, 255), thickness=7)
                score += 10
        except:
            pass

    def followThrough(self):
        global status_count, score

        print('6. not followThrough')

        try:
            self.right_hip = self.results.pose_landmarks.landmark[24]
            self.right_wrist = self.results.pose_landmarks.landmark[16]
            self.left_wrist = self.results.pose_landmarks.landmark[15]
            self.right_elbow = self.results.pose_landmarks.landmark[14]
            self.left_elbow = self.results.pose_landmarks.landmark[13]
            self.right_shoulder = self.results.pose_landmarks.landmark[12]
            self.left_shoulder = self.results.pose_landmarks.landmark[11]

            if (status_count == 5) and (self.right_hip.x < self.right_wrist.x) and (
                    self.right_hip.x < self.left_wrist.x) and (self.right_elbow.x > self.right_shoulder.x) and (
                    self.left_elbow.x > self.left_shoulder.x) and (self.right_elbow.y > self.right_shoulder.y) and (
                    self.left_elbow.y > self.left_shoulder.y):
                status_count += 1
                print('6. followThrough')
                cv2.putText(self.frame, text='6. followThrough', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=2.5, color=(255, 255, 255), thickness=7)
                score += 10
        except:
            pass

    def finish(self):
        global status_count, score

        print('7. not finish')

        try:
            self.right_hip = self.results.pose_landmarks.landmark[24]
            self.right_wrist = self.results.pose_landmarks.landmark[16]
            self.left_wrist = self.results.pose_landmarks.landmark[15]
            self.right_elbow = self.results.pose_landmarks.landmark[14]
            self.left_elbow = self.results.pose_landmarks.landmark[13]
            self.right_shoulder = self.results.pose_landmarks.landmark[12]
            self.left_shoulder = self.results.pose_landmarks.landmark[11]

            if (status_count == 6) and (self.right_hip.x < self.right_wrist.x) and (
                    self.right_hip.x < self.left_wrist.x) and (self.right_shoulder.y > self.right_wrist.y) and (
                    self.left_shoulder.y > self.left_wrist.y) and (self.right_wrist.x > self.right_shoulder.x) and (
                    self.left_wrist.x > self.left_shoulder.x) and (self.right_wrist.y < self.right_shoulder.y) and (self.left_wrist.y < self.left_shoulder.y):
                status_count += 1
                print('7. finish')
                cv2.putText(self.frame, text='7. finish', org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=2.5, color=(255, 255, 255), thickness=7)
                score += 10
        except:
            pass

    def update(self):
        global off, status_count

        off = 0

        with self.mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as pose:

            while True:
                (self.ret, self.frame) = self.video.read()
                cv2.rectangle(self.frame, (150, 0), (490, 470), color=(255, 255, 255), thickness=3)

                self.results = pose.process(self.frame)

                if status_count == 0:
                    self.address()
                else:
                    if status_count == 1:
                        self.backSwing()
                    else:
                        if status_count == 2:
                            self.topSwing()
                        else:
                            if status_count == 3:
                                self.downSwing()
                            else:
                                if status_count == 4:
                                    self.impact()
                                else:
                                    if status_count == 5:
                                        self.followThrough()
                                    else:
                                        if status_count == 6:
                                            self.finish()
                                        else:
                                            continue

                if off == 1:
                    break

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def detect(request):
    try:
        cam = VideoCamera(request)
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass

def releaseCamera(request):
    global off
    if request.GET.get("Data") == "stop recording":
        off = 1
        return JsonResponse({
            'success': True,
            'url': reverse("analysisresultpage:result")
        })

def backPage(request):
    global off
    if request.GET.get("Data") == "back":
        off = 1
        return JsonResponse({
            'success': True,
            'url': reverse("analysispage:camera"),
        })