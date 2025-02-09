# OpenCV
## Methods:
cv2.==imread==(_filename_)

- _filename_: the path to the file

cv2.==imshow==(_winname_, _mat_) # displays the image as a new window

- _winname_: name of the window (str)
- _mat_: MatLike | GpuMat | UMat (actual matrix of pixcels)

cv2. ==waitKey==(_delay_) -> int

- _delay_: time in miliseconds for delay (in case of 0 it will be infinit)

cv2.==VideoCapture==(_filenameOrIndex_) -> VideoCapture

- _filenameOrIndex_: an index for the device video capturing (from 0) or a file path to the file

cv2.==destroyAllWindows==()

cv2.==resize==(src, dsize, interpolation = cv.INTER_AREA)
- src: the frame object
- dsize: dimensions to resize ()
- interpolation


## Objects:
### VideoCapture

videoCapture.==read==() -> bool\[bool, MatLike\] # reading a frame from a VideoCapture object

- capture: object of type **_VideoCapture_**

VideoCapture.==release==()

VideoCapture.==set==(propId, value) # for example for scaling and changing resulution of LIVE videos!
- propId: 3 for width and 4 for height and 10 for brightness
- the value to set to



### MatLike (frame image)

frame.==shape==[ ]  # 1 for width, 0 for height


---

# Numpy
## Methods:
numpy.==zeros==(shape, dtype = 'unit'8) 
- shape: something like (500, 500)
- dtype: data type



