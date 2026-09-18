# **Project Statement**

## **1. Project Title**

**Smart Parking Space Detection and Occupancy Monitoring Using Computer Vision**

## **2. Problem Statement**

Finding an available parking space can be difficult in busy parking areas, especially when many vehicles are present. People usually have to check the parking spaces manually to find out which spaces are occupied and which are available. This can take time and can be inconvenient when the parking area is crowded.

The proposed project develops a computer vision-based parking monitoring system that analyzes a parking-lot image, identifies predefined parking spaces, determines their occupancy status, and calculates basic parking statistics. The system is implemented in Python using OpenCV and NumPy and can be executed through the command line.

## **3. Scope of the Project**

The scope of the project includes:

- Reading a parking-lot image from a local file.
- Validating and loading the input image.
- Resizing the image for processing.
- Converting the image to grayscale.
- Applying Gaussian blur to reduce noise.
- Identifying predefined parking-space regions.
- Extracting individual parking-space regions from the image.
- Analyzing each parking-space region using threshold-based image processing.
- Determining whether a predefined parking space is occupied or available.
- Counting the total number of parking spaces.
- Counting occupied and available spaces.
- Calculating the parking occupancy rate.
- Displaying parking-space boundaries and occupancy results.
- Saving the processed images in an output directory.
- Providing command-line execution and basic error handling.

The current project focuses on analyzing a single parking-lot image with predefined parking-space coordinates. Features such as live video processing, automatic parking-space detection, and deep-learning-based vehicle detection are outside the current scope and can be considered for future development.

## **4. Target Users**

The intended users of the system include:

- Parking lot operators who need basic occupancy information.
- Parking management staff.
- Colleges and universities managing campus parking areas.
- Office parking facilities.
- Shopping mall parking areas.
- Students learning practical applications of Computer Vision.
- Beginners who want to understand image-processing techniques through a real-world project.

## **5. High-Level Features**

1. **Image Input:** Accepts a parking-lot image from a local file.

2. **Image Preprocessing:** Resizes the image, converts it to grayscale, and applies Gaussian blur.

3. **Parking Space Identification:** Uses predefined coordinates to identify the selected parking-space regions.

4. **Parking Space Extraction:** Extracts individual regions corresponding to the selected parking spaces.

5. **Occupancy Detection:** Analyzes each parking-space region using threshold-based image processing to determine whether it is occupied or available.

6. **Parking Analytics:** Calculates the total number of spaces, occupied spaces, available spaces, and occupancy rate.

7. **Result Visualization:** Displays parking-space boundaries along with their occupancy status.

8. **Output Generation:** Saves the processed and final result images in the output directory.

9. **Error Handling:** Displays an error message when the input image cannot be loaded or processed correctly.

## **6. Expected Outcome**

The expected outcome is a command-line-based application that takes a photograph of a parking area and generates:

- A preprocessed parking-lot image.
- An image showing the identified parking spaces.
- An image showing the detected occupancy status.
- A final parking analysis image.
- The total number of parking spaces.
- The number of occupied spaces.
- The number of available spaces.
- The overall parking occupancy rate.

The project demonstrates the practical application of image preprocessing, grayscale conversion, Gaussian filtering, region extraction, threshold-based analysis, and image visualization techniques to solve a real-world parking occupancy problem.
