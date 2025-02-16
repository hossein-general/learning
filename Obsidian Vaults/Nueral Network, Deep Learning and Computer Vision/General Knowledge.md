# Generic Concepts
object detection steps:
- ==localizing==
- ==classifying==

==one-stage methods==: Localization and classification are done in a single step
	The algorithm processes the entire image in one forward pass through a neural network.
	It predicts bounding boxes and class probabilities directly from the image.
e.g.
	YOLO (You Only Look Once): Processes the image in one pass and predicts bounding boxes and classes simultaneously.
	SSD (Single Shot Detector): Similar to YOLO but uses multiple feature maps for better accuracy.

==forward pass==: Forward propagation (or forward pass) refers to **the calculation and storage of intermediate variables (including outputs) for a neural network in order from the input layer to the output layer**.

==two-stage methods==: Localization and classification are done in two steps
	Region Proposal: Generate potential regions of interest (ROIs) that might contain objects.
	Classification and Refinement: Classify the ROIs and refine the bounding boxes.
e.g.
	Faster R-CNN: Uses a ==Region Proposal Network (RPN)== to generate ROIs, then classifies and refines them.
	Mask R-CNN: Extends Faster R-CNN to include pixel-level segmentation

==Region Proposal Network (RPN)==: A region proposal network (RPN) classification layer **classifies image regions as either object or background by using a cross entropy loss function**

==R-CNN==: Region-based Convolutional Neural Network (type of a deep learning architecture)


==Feature Extraction==: process of identifying and extracting meaningful patterns or features from raw data (reduces the complexity of the data and highlights the most important information)
	==Low-level== features: Edges, corners, textures.
	==Mid-level features==: Shapes, parts of objects.
	==High-level features==: Entire objects or complex patterns.

==backbone== examples: part of a neural network responsible for feature extraction (core of the object detection model)	
	***ResNet***: A deep CNN with residual connections.
	***VGG***: A simpler CNN with many layers.
	***MobileNet***: A lightweight CNN designed for mobile devices.
	***EfficientNet***: A scalable and efficient CNN.


summary:
==Feature Extraction==: Identifying meaningful patterns in images.
==Backbone==: The part of the model responsible for feature extraction (e.g., ResNet, VGG).
==Convolutional Layers==: Detect patterns in the input image.
==Max Pooling==: Downsamples feature maps to reduce complexity and retain important features.





==darknet 53==: feauture extractor or backbone 

-------------------------------------------------------------------------------------

==object detection== steps:
	==input image==
	==preprocessing==: resizing, normalization, or augmentation and converting it to a tensor format
	==feature extraction==: passed through a neural network (often a Convolutional Neural Network  or CNN) (edges, textures, and shapes) (e.g., ResNet, VGG, MobileNet)
 	A filter (or kernel) slides over the input image
 	Early layers detect low-level features (edges, textures).
    Deeper layers detect high-level features (object parts, entire objects).
	==region proposal==: to generate potential regions of interest (e.g., R-CNN, Faster R-CNN, not present in single-shot detectors)
	==object localization==: predicts the bounding boxes around the objects
	process of identifying the **location** of an object within an image
	==object classification==: predicts the class of the object 
	they are (localization and classification) often performed together in the same step by the ==detection head==
	==detection head==: a crucial component responsible for processing the features extracted by the backbone and generating predictions
	==**Bounding Box Regressor**==: This component predicts the coordinates of the bounding boxes around detected objects. It adjusts the proposed bounding boxes to accurately fit the objects.
	==**Classification Layer**==: This component assigns a probability score to each detected object, indicating the likelihood that the object belongs to a particular class.
	==**Anchor Boxes (in some architectures)**==: These are predefined boxes of various shapes and sizes used as references for predicting bounding boxes. [Anchor-free detectors](https://www.ultralytics.com/glossary/anchor-free-detectors) have emerged as a simpler alternative, eliminating the need for predefined anchors and directly predicting bounding boxes.
	==post processing==: e.g.:
		==Non-Maximum Suppression (NMS)==: remove overlapping bounding boxes and keep only the most confident predictions
		==Thresholding==: To filter out predictions with low confidence scores
	==output==: list of detected objects, bounding box, class label, and confidence score


==Anchor Boxes==: Predefined boxes of various aspect ratios and scales used to predict bounding boxes.
==IoU (Intersection over Union)==: A metric used to evaluate the overlap between predicted and ground-truth bounding boxes.
![[IoU for loss functions.png]]
==mAP (mean Average Precision)==: A common metric to evaluate the performance of object detection models.

Anchor Box vs Bounding Box
==bounding box==: A box that represents the exact location of an object in an image.

Anchor Boxes are used on top of feature maps, not on images
Anchor Boxes are used to generate bounding boxes, but they aren't the bounding boxes

==clustering algorithm==: Clustering algorithms group similar data together without labels (unsupervised learning) (like ==K-Means)==
Different algorithms have different strengths and use cases:
	***K-Means*** → Fast & Simple
	***Hierarchical*** → Tree-like structure
	***DBSCAN*** → Finds dense clusters & detects outliers
	***Mean-Shift*** → Moves towards high-density regions

==loss function==:
- ***==Localization Loss== (Bounding Box Loss)***
Measures how accurate the predicted bounding box is compared to the ground truth (actual box).
Uses Mean Squared Error (MSE) to compare coordinates (x, y, width, height).
If the box is slightly off, this part increases the loss!

- ***==Confidence Loss== (Objectness Loss)***
Determines if a box contains an object or not.
If YOLO predicts a box but there’s no object there, it penalizes the model.
Uses Binary Cross-Entropy Loss to compare the object confidence score.

- ==***Classification Loss***==
Used when multiple classes exist (e.g., cat, dog, car, person).
Measures how well the model classifies the detected object.
Uses Cross-Entropy Loss to compare the predicted class vs. the actual class.

*Total Loss = Localization Loss + Confidence Loss + Classification Loss*

==Feature Maps==:  generated through a process called convolution

==Batch Size==: specifies the number of samples that propagate through the neural network before updating the model parameters. Each batch of samples goes through one full forward and one full backward propagation

==Ground Truth==: information that is known to be real or true, provided by direct observation and measurement as opposed to information provided by inference.

==Object Annotation==: labelling objects of interest within images or videos, enabling AI models to learn to detect, classify, and understand visual data


