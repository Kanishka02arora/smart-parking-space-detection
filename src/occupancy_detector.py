import cv2

# Configurable default threshold for pixel counting
# If the number of non-zero (white) pixels after thresholding exceeds this value,
# the space is classified as "Occupied"; otherwise, it is classified as "Empty".
DEFAULT_PIXEL_THRESHOLD = 900


def process_crop_threshold(crop):
    """
    Converts a parking space image crop to grayscale and applies adaptive thresholding.

    Args:
        crop (numpy.ndarray): BGR or grayscale image crop of a single parking space.

    Returns:
        numpy.ndarray: Binary thresholded image (white pixels indicate edges/textures/objects).
    """
    # 1. Convert to grayscale if image is colored (3 channels)
    if len(crop.shape) == 3 and crop.shape[2] == 3:
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    else:
        gray = crop.copy()

    # 2. Apply Gaussian Blur to smooth out high-frequency noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. Apply Adaptive Thresholding
    # Binary inverse thresholding highlights cars, boundaries, and textures as white pixels
    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        25,
        16
    )

    # Median blur to clean up isolated noise spots
    thresh = cv2.medianBlur(thresh, 5)

    return thresh


def classify_space(crop, threshold=DEFAULT_PIXEL_THRESHOLD):
    """
    Classifies a single parking space crop as 'Occupied' or 'Empty' based on pixel count.

    Args:
        crop (numpy.ndarray): Parking space crop.
        threshold (int): Minimum non-zero pixel count to consider space occupied.

    Returns:
        tuple: (status_string, pixel_count, threshold_image)
    """
    thresh_img = process_crop_threshold(crop)

    # Count the number of non-zero (white) pixels
    pixel_count = cv2.countNonZero(thresh_img)

    # Determine occupancy status
    if pixel_count > threshold:
        status = "Occupied"
    else:
        status = "Empty"

    return status, pixel_count, thresh_img


def detect_occupancy(extracted_regions, threshold=DEFAULT_PIXEL_THRESHOLD):
    """
    Analyzes all extracted parking space crops and determines their occupancy status.

    Args:
        extracted_regions (list of dict): List containing parking space regions from parking_space_detector.
        threshold (int): Configurable pixel count threshold.

    Returns:
        list of dict: List of space results with 'id', 'status', 'pixel_count', and 'threshold'.
    """
    results = []

    for item in extracted_regions:
        space_id = item["id"]
        crop = item["crop"]

        status, count, thresh_img = classify_space(crop, threshold=threshold)

        results.append({
            "id": space_id,
            "status": status,
            "pixel_count": count,
            "threshold": threshold,
            "crop": crop,
            "threshold_image": thresh_img
        })

    return results
