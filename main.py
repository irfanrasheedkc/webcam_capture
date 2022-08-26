import cv2 as cv

# Reading videos
capture = cv.VideoCapture(0)  # 0 denote primary cam. 1 denote secondary cam
# capture2 = cv.VideoCapture(1)
i=0
while True:
    isTrue, frame = capture.read()
    # Convert to blurred
    blur = cv.GaussianBlur(frame, (1,1), cv.BORDER_DEFAULT)

    # edge detection
    canny = cv.Canny(blur, 127, 175)
    frame = cv.putText(frame, str(i), (100, 100), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv.LINE_4)
    cv.imshow('Edge' , frame)
    cv.imshow('Blur' , blur )

    cv.imshow('Webcam 1', canny)

    # isTrue, frame1 = capture2.read()
    # cv.imshow('Webcam 2', frame1)

    if cv.waitKey(10) & 0xFF == ord('d'):
        break
    if cv.waitKey(1) & 0xFF == ord(' '):
        cv.imwrite('Smile'+str(i)+'.png' , canny, [cv.IMWRITE_JPEG_QUALITY, 100])

        i=i+1

# capture2.release()
capture.release()
cv.destroyAllWindows()
