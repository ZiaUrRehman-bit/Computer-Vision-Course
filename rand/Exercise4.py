import cv2 
import numpy as np
from Module import MyDetectionMethods

# #######################Image########################################
#size configuration is in class-defcanny
#  aruco Dictionry ,size and dimension
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
#reading the image
img = cv2.imread(r"C:\Users\Dr.Phone\Desktop\Msc Robotics &Automation\1.png")
#if the size change, then the detected areahas to be changed accordingly
img = cv2.resize(img, (400, 600))

# get aruco markers
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict)
#converting the varible corners from a tuple to a numpy array as polylines doent take tuple.
corners = np.int0(corners)
#Drawing corners around aruco
cv2.polylines(img, corners, True, (255,0,255), 3)

#  Aruco perimeter: below comment refered from the Demo
#next we need to find the lenght between the corners, referd to as our perimimter. 
#The pixel perimeter data is stored in the first position of our corners array. 
#beacuse we only have one marker to detect we have hardcoded to look at index [0] 
perimeter = cv2.arcLength(corners[0], True)
#Calculating ratio
pixelCmRatio = perimeter/20
#printing the ratio
print(pixelCmRatio)

contours = MyDetectionMethods.detectionUsingCanny('self',img)
print(len(contours))

cv2.drawContours(img, contours, -1, (255,0,255), 3)

for cont in contours:
    
    rect = cv2.minAreaRect(cont)
    (x, y), (w, h), angle = rect
    objectWidth = w / pixelCmRatio
    objectHeight = h / pixelCmRatio
    cv2.circle(img, (int(x),int(y)),2, (0,0,255),2)
    if objectWidth < objectHeight:
            use = objectWidth
            objectWidth = objectHeight
            objectHeight = use
    if 4.2 < objectWidth < 4.8 and 0.9 < objectHeight < 1.2:
            print("AAA Battery")
            boundingbox = cv2.boxPoints(rect)
            boundingbox = np.int0(boundingbox)
            cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(img, [boundingbox], True, (255, 0, 0), 2)
            cv2.putText(img, "objectWidth {} cm".format(round(objectWidth, 1)), (int(x - 100), int(y - 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 100, 0), 2)
            cv2.putText(img, "objectHeight {} cm".format(round(objectHeight, 1)), (int(x - 100), int(y + 15)),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 100, 0), 2)
            
    elif 8 < objectWidth < 8.7 and 4.9 < objectHeight < 5.5:
            print("Card")
            boundingbox = cv2.boxPoints(rect)
            boundingbox = np.int0(boundingbox)
            cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(img, [boundingbox], True, (255, 0, 0), 2)
            cv2.putText(img, f'objectWidth: {round(objectWidth, 2)} cm', (int(x-90),int(y-60)),
                cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
            cv2.putText(img, f'objectHeight: {round(objectHeight, 2)} cm', (int(x-90),int(y-40)),
                 cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)        
    # boundingbounding = cv2.boundingPoints(rect)
    # # #convert to integer
    # boundingbounding = np.int0(boundingbounding)
    
    #### Below command will draw a corners but not accurate
    # cv2.polylines(img,[boundingbounding],True,(255,0,0),3)
    
    # # drawing rectangle around object
    # # cv2.line(img, (boundingbounding[0][0], boundingbounding[0][1]), (boundingbounding[1][0],boundingbounding[1][1]), (0,0,255),2)
    # # cv2.line(img, (boundingbounding[0][0], boundingbounding[0][1]), (boundingbounding[3][0],boundingbounding[3][1]), (0,0,255),2)
    # # cv2.line(img, (boundingbounding[1][0],boundingbounding[1][1]), (boundingbounding[2][0],boundingbounding[2][1]), (0,0,255),2)
    # # cv2.line(img, (boundingbounding[3][0],boundingbounding[3][1]), (boundingbounding[2][0],boundingbounding[2][1]), (0,0,255),2)
    
   
    # cv2.putText(img, f'objectWidth: {round(objectobjectWidth, 2)} cm', (int(x-90),int(y-60)),
    #             cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
    # cv2.putText(img, f'objectHeight: {round(objectobjectHeight, 2)} cm', (int(x-90),int(y-40)),
    #             cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
# cv2.imwrite('detected Image.png',img)
cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()


########################### Camera detection ##############################
# param = cv2.aruco.DetectorParameters_create()
# #  aruco Dictionry ,size and dimension
# aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
# #reading the image
# cam=cv2.VideoCapture(0)

# # Check if the video was opened successfully
# if not cam.isOpened():
#     print("Error")




# # Read and process each frame of the video
# while cam.isOpened():
#     # Read the next frame , return two things 1. frame, 2. boolean value(True or False)---> True when frame is 
#     # successfully read, False when frame is not successfully read
#     _, frame = cam.read()

   
# # get aruco markers
#     corners, _, _ = cv2.aruco.detectMarkers(cam,aruco_dict,parameters=param)
# #converting the varible corners from a tuple to a numpy array as polylines doent take tuple.
#     corners = np.int0(corners)
# #Drawing corners around aruco
#     cv2.polylines(cam, corners, True, (255,0,255), 3)

# #  Aruco perimeter: below comment refered from the Demo
# #next we need to find the lenght between the corners, referd to as our perimimter. 
# #The pixel perimeter data is stored in the first position of our corners array. 
# #beacuse we only have one marker to detect we have hardcoded to look at index [0] 
#     perimeter = cv2.arcLength(corners[0], True)
# #Calculating ratio
#     pixelCmRatio = perimeter/17
# #printing the ratio
#     print(pixelCmRatio)

#     contours = MyDetectionMethods.detectionUsingCanny(cam)
#     print(len(contours))

#     # cv2.drawContours(cam, contours, -1, (255,0,255), 3)

#     for cont in contours:
    
#         rect = cv2.minAreaRect(cont)
#         (x, y), (w, h), angle = rect
#         objectobjectWidth = w / pixelCmRatio
#         objectobjectHeight = h / pixelCmRatio
#         cv2.circle(cam, (int(x),int(y)),2, (0,0,255),2)

#         boundingbounding = cv2.boundingPoints(rect)
#     # #convert to integer
#         boundingbounding = np.int0(boundingbounding)
    
#     #### Below command will draw a corners but not accurate
#         cv2.polylines(cam,[boundingbounding],True,(255,0,0),3)
    
#     # drawing rectangle around object
#     # cv2.line(img, (boundingbounding[0][0], boundingbounding[0][1]), (boundingbounding[1][0],boundingbounding[1][1]), (0,0,255),2)
#     # cv2.line(img, (boundingbounding[0][0], boundingbounding[0][1]), (boundingbounding[3][0],boundingbounding[3][1]), (0,0,255),2)
#     # cv2.line(img, (boundingbounding[1][0],boundingbounding[1][1]), (boundingbounding[2][0],boundingbounding[2][1]), (0,0,255),2)
#     # cv2.line(img, (boundingbounding[3][0],boundingbounding[3][1]), (boundingbounding[2][0],boundingbounding[2][1]), (0,0,255),2)
    
   
#         cv2.putText(cam, f'objectWidth: {round(objectobjectWidth, 2)} cm', (int(x-90),int(y-60)),
#                 cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
#         cv2.putText(cam, f'objectHeight: {round(objectobjectHeight, 2)} cm', (int(x-90),int(y-40)),
#                 cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
        
#     cv2.imshow(" FRAME", cam)
#     cv2.waitKey(8000)
# cam.release()
# cv2.destroyAllWindows()