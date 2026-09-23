import cv2

# Parking space coordinate definitions for Image 1 (parking.jpg)
PARKING1_SPACES = [
    {"id": "Space 1", "x": 50, "y": 120, "w": 90, "h": 160},
    {"id": "Space 2", "x": 160, "y": 120, "w": 90, "h": 160},
    {"id": "Space 3", "x": 270, "y": 120, "w": 90, "h": 160},
    {"id": "Space 4", "x": 380, "y": 120, "w": 90, "h": 160},
    {"id": "Space 5", "x": 490, "y": 120, "w": 90, "h": 160},
    {"id": "Space 6", "x": 600, "y": 120, "w": 90, "h": 160},
]

# Parking space coordinate definitions for Image 2 (parking2.jpg)
PARKING2_SPACES = [
    {"id": "Space 1", "x": 50, "y": 120, "w": 90, "h": 160},
    {"id": "Space 2", "x": 160, "y": 120, "w": 90, "h": 160},
    {"id": "Space 3", "x": 270, "y": 120, "w": 90, "h": 160},
    {"id": "Space 4", "x": 380, "y": 120, "w": 90, "h": 160},
    {"id": "Space 5", "x": 490, "y": 120, "w": 90, "h": 160},
    {"id": "Space 6", "x": 600, "y": 120, "w": 90, "h": 160},
]

SPACES_CONFIG_MAP = {
    "parking1": PARKING1_SPACES,
    "parking2": PARKING2_SPACES,
}


def get_parking_spaces(image_key="parking1"):
    """
    Returns the list of defined parking space coordinates for the specified image key.

    Args:
        image_key (str): 'parking1' or 'parking2'. Defaults to 'parking1'.

    Returns:
        list of dict: Parking space coordinate definitions.
    """
    key = str(image_key).lower()
    return SPACES_CONFIG_MAP.get(key, PARKING1_SPACES)


def extract_parking_space_crops(image, parking_spaces=None):
    """
    Extracts individual rectangular parking space regions (crops) from the input image.

    Args:
        image (numpy.ndarray): Source image.
        parking_spaces (list, optional): List of space coordinate dicts.

    Returns:
        list of dict: Extracted space crops and bounding box coordinates.
    """
    if parking_spaces is None:
        parking_spaces = get_parking_spaces()

    extracted_regions = []
    img_height, img_width = image.shape[:2]

    for space in parking_spaces:
        x, y, w, h = space["x"], space["y"], space["w"], space["h"]

        x_end = min(x + w, img_width)
        y_end = min(y + h, img_height)

        crop = image[y:y_end, x:x_end]

        extracted_regions.append({
            "id": space["id"],
            "crop": crop,
            "box": (x, y, w, h)
        })

    return extracted_regions


def draw_parking_spaces(image, parking_spaces=None, occupancy_results=None, thickness=2):
    """
    Draws rectangular boundaries, Space IDs, and Occupancy Statuses on a copy of the image.

    Args:
        image (numpy.ndarray): Input image.
        parking_spaces (list, optional): List of space definitions.
        occupancy_results (list, optional): Occupancy result list.
        thickness (int): Rectangle line thickness.

    Returns:
        numpy.ndarray: Annotated image.
    """
    if parking_spaces is None:
        parking_spaces = get_parking_spaces()

    status_map = {}
    if occupancy_results:
        for res in occupancy_results:
            status_map[res["id"]] = res.get("status", "Unknown")

    annotated_image = image.copy()

    for space in parking_spaces:
        space_id = space["id"]
        x, y, w, h = space["x"], space["y"], space["w"], space["h"]
        status = status_map.get(space_id, None)

        if status == "Empty":
            color = (0, 255, 0)      # Green
        elif status == "Occupied":
            color = (0, 0, 255)      # Red
        else:
            color = (0, 255, 0)      # Default Green

        cv2.rectangle(annotated_image, (x, y), (x + w, y + h), color, thickness)

        label = f"{space_id}: {status}" if status else space_id

        cv2.putText(
            annotated_image,
            label,
            (x + 5, y + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )
        cv2.putText(
            annotated_image,
            label,
            (x + 5, y + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            1,
            cv2.LINE_AA
        )

    return annotated_image
