from django.shortcuts import render, redirect
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import time
import threading

def index(request):
    return render(request, 'camera_home.html')

def index2(request):
    return render(request, 'camera_base.html')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.start = time.time()
        self.count = 99
        self.fc = 20.0
        self.codec = cv2.VideoWriter_fourcc(*'XVID')
        (self.grabbed, self.frame) = self.video.read()

        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            if self.count != time.strftime('%H', time.localtime(time.time())):  # 시간이 바뀌면 영상파일을 새로 만든다. (시간으로 감지)
                self.count = time.strftime('%H', time.localtime(time.time()))

                self.path = "../"
                self.out = cv2.VideoWriter(self.path + time.strftime('%Y-%m-%d %Hh %Mm', time.localtime(time.time())) + '.avi', self.codec, self.fc, (int(self.video.get(3)), int(self.video.get(4))))

            (self.ret, self.frame) = self.video.read()
            self.now = time.time()
            self.diff = int(self.now - self.start)
            cv2.putText(self.frame, text='{}s'.format(30 - self.diff), org=(250, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2.5, color=(255, 255, 255), thickness=7)

            if 30 - self.diff == 0:
                break

            if self.ret == True:
                self.out.write(self.frame)
            else:
                break

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def detect(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass
