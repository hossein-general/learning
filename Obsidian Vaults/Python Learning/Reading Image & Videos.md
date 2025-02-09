
### Reading Images
cv2.==imread==(*filename*)
- *filename*: the path to the file

cv2.==imshow==(*winname*, *mat*) # displays the image as a new window
- *winname*: actual matrix of pixcels (str)
- *mat*: name of the window

cv2. ==waitKey==(*delay*) -> int
- *delay*: time in miliseconds for delay (in case of 0 it will be infinit)
---
### Reading Videos
cv2.==VideoCapture==(*filenameOrIndex*) -> VideoCapture
- *filenameOrIndex*: an index for the device video capturing (from 0) or a file path to the file

> [!IMPORTANT]
> Should be saved in a virable:
> ``` python 
capture = cv2.VideoCapture(filenameOrIndex)
> ```

capture.==read==() -> isTrue, frame # reading a frame from a VideoCapture object 
- capture: object of type ***VideoCapture***

capture.==release==()

cv2.==destroyAllWindows==()

> [!NOTE]
> to read video we should through frames
> ``` python
> capture = cv2.VideoCapture(filenameOrIndex)
> 
> while True: 
> 	isTrue, frame = capture.read()
> 	cv2.imshow("Video", frame)
> 	
> 	if cv2.waitKey(20) & 0xFF == ord('d'): # if letter d has been pressed
> 		break
> 	
> capture.release()
> cv2.destroyAllWindows()
>```
> - isTrue: a boolean showing if the image was successfully read in or not
> - frame: the frame that is taken

> [!note]
> error -215: opencv couldnt find a file in a location