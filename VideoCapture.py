import cv2,os, argparse


 class Facedetection:

    def__init__(self):

        #Assign  a variable to cv2.videocapture(0)
        self.videosource = cv2.VideoCapture(0)

    def CaptureFrames(self):
        while True:
            #Create a unique number for each frame
            framenumber = '%08d' % (self.count)

            #capture frame by frame

            ret,frame = self.videoSource.read()

            #Set the colour of the image to gray so it can be easy for HarCascade to  detect

            screenColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #Implement a cascade classifier,using detect MULTISCALE

            faces = self.faceCascade.detectMultiScale(
                screenColor
                scaleFactor= 1.1,
                minNeighbors= 5,
                minSize= (30,30)
                flags= cv2.CASCADE_SCALE_IMAGE)


            )

         #Set screen colour to gray so that cascade can easily detect edges and faces

