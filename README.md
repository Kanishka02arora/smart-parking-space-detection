
# Smart Parking Space Detection and Occupancy Monitoring Using Computer Vision

## 1. Project Overview

The **Smart Parking Space Detection and Occupancy Monitoring System** is a Python-based computer vision project developed using OpenCV and NumPy. The system analyzes a parking-lot image and determines whether predefined parking spaces are occupied or available.

The project performs image preprocessing, identifies predefined parking spaces, detects their occupancy status using image-processing techniques, calculates parking statistics, and generates a visualized output image.

The system is designed as an image-based parking analysis solution and can be executed through the command line.

## 2. Features

- Accepts a parking-lot image as input.
- Validates and loads the input image.
- Resizes the image for processing.
- Converts the image into grayscale.
- Applies Gaussian Blur for image preprocessing.
- Identifies predefined parking spaces.
- Extracts individual parking-space regions.
- Detects whether parking spaces are occupied or available.
- Calculates the total number of parking spaces.
- Calculates the number of occupied spaces.
- Calculates the number of available spaces.
- Calculates the overall parking occupancy rate.
- Displays the detected parking spaces and their occupancy status.
- Saves the processed images in the output directory.
- Displays processing results and parking statistics.

## 3. Technologies and Tools Used

- **Programming Language:** Python 3
- **Computer Vision Library:** OpenCV
- **Numerical Processing:** NumPy
- **Development Environment:** VS CODE
- **Version Control:** Git and GitHub

## 4. Project Structure

```text
smart-parking-space-detection/
│
├── data/
│   └── parking.jpg
│
├── output/
│   ├── parking_copy.jpg
│   ├── parking_preprocessed.jpg
│   ├── parking_spaces_visualized.jpg
│   ├── parking_occupancy_detected.jpg
│   └── final_parking_result.jpg
│
├── src/
│   ├── main.py
│   ├── input_handler.py
│   ├── preprocessing.py
│   ├── parking_space_detector.py
│   ├── occupancy_detector.py
│   ├── analytics.py
│   └── visualization.py
│
├── tests/
│
├── .gitignore
├── README.md
├── requirements.txt
└── statement.md
```

## 5. Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kanishka02arora/smart-parking-space-detection.git
cd smart-parking-space-detection
```

### Step 2: Create a Virtual Environment

On Windows:

```powershell
py -m venv venv
```

### Step 3: Activate the Virtual Environment

For PowerShell:

```powershell
venv\Scripts\activate
```

### Step 4: Install Dependencies

```powershell
py -m pip install -r requirements.txt
```

If the requirements file has not been created yet, install the dependencies manually:

```powershell
py -m pip install opencv-python numpy
```

## 6. Input Image Preparation

1. Use the `data` folder in the project root.
2. Add the parking-lot image to this folder.
3. Use the filename `parking.jpg`.
4. Make sure the image contains a visible parking area.

Example:

```text
data/parking.jpg
```

The provided parking-lot image is used as the input for the system.

## 7. How to Run the Project

Run the following command from the project root:

```powershell
python src/main.py
```

The program automatically loads the image from:

```text
data/parking.jpg
```

The image is then processed through the following stages:

```text
Input Image
     ↓
Image Preprocessing
     ↓
Parking Space Identification
     ↓
Occupancy Detection
     ↓
Parking Analytics
     ↓
Result Visualization
     ↓
Final Output
```

### Expected Terminal Output

The terminal displays processing information such as:

```text
Image loaded successfully
Image preprocessing completed
Parking spaces identified
Occupancy detection completed
Parking analytics calculated
Final result saved successfully
```

The processed images are saved in the `output` folder.

The final result is saved as:

```text
output/final_parking_result.jpg
```

## 8. Testing Instructions

### Test Case 1: Valid Parking-Lot Image

**Input:** A valid parking-lot image containing visible parking spaces.

**Command:**

```powershell
python src/main.py
```

**Expected Result:**

- The input image loads successfully.
- The image is preprocessed successfully.
- Predefined parking spaces are identified.
- Occupancy detection is performed.
- Parking statistics are calculated.
- The final processed image is generated.

### Test Case 2: Invalid or Missing Input Image

**Input:** Missing or invalid input image.

**Expected Result:**

```text
Invalid input
```

The program should stop processing if the input image cannot be loaded or processed correctly.

### Test Case 3: Parking Occupancy Analysis

**Input:** Parking-lot image containing occupied and/or available spaces.

**Expected Result:**

- Each predefined parking space is classified.
- Total parking spaces are calculated.
- Occupied spaces are calculated.
- Available spaces are calculated.
- Occupancy rate is calculated.

## 9. Computer Vision Techniques Used

| Technique | Purpose |
|---|---|
| Image Resizing | Standardizes the image size for processing |
| Grayscale Conversion | Converts the image into intensity values |
| Gaussian Blur | Reduces noise before occupancy analysis |
| Threshold-based Analysis | Helps determine the occupancy status of parking spaces |
| Region Extraction | Extracts individual predefined parking-space regions |
| Image Visualization | Displays parking-space boundaries and occupancy results |

## 10. Parking Analytics

The system calculates the following parking statistics:

- **Total Spaces:** Total number of predefined parking spaces.
- **Occupied Spaces:** Number of spaces detected as occupied.
- **Available Spaces:** Number of spaces detected as available.
- **Occupancy Rate:** Percentage of parking spaces that are occupied.

The occupancy rate is calculated using:

```text
Occupancy Rate = (Occupied Spaces / Total Spaces) × 100
```

## 11. Limitations

- Parking spaces are currently defined using predefined coordinates.
- The system is designed for image-based parking analysis.
- The occupancy detection uses basic image-processing and threshold-based analysis.
- Changes in camera position may affect the predefined parking-space coordinates.
- Changes in lighting conditions may affect occupancy detection.
- The current implementation is designed for a fixed parking-lot image.
- The system does not currently use a trained deep-learning vehicle detection model.

## 12. Future Enhancements

- Add automatic parking-space detection.
- Support different parking-lot layouts.
- Add real-time video-based parking detection.
- Add vehicle detection using deep learning.
- Improve detection under different lighting conditions.
- Add automatic camera perspective correction.
- Add a graphical user interface.
- Add real-time parking availability monitoring.
- Support larger parking areas with more parking spaces.

## 13. Author

**Name:** Kanishka Arora  
**Course:** Computer Vision  
**Institution:** VIT Bhopal University  
**Project Type:** Individual Project
