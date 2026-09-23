import cv2


def draw_space_boxes(image, parking_spaces, occupancy_results=None, thickness=2):
    """
    Draws rectangular boundaries, Space IDs, and Occupancy Statuses for each parking space.

    Args:
        image (numpy.ndarray): Base image to draw on.
        parking_spaces (list of dict): List of parking space definitions.
        occupancy_results (list of dict, optional): Results containing 'id' and 'status'.
        thickness (int): Rectangle line thickness.

    Returns:
        numpy.ndarray: Annotated copy of the image.
    """
    annotated = image.copy()

    # Map space IDs to status
    status_map = {}
    if occupancy_results:
        for res in occupancy_results:
            status_map[res["id"]] = res.get("status", "Unknown")

    for space in parking_spaces:
        space_id = space["id"]
        x, y, w, h = space["x"], space["y"], space["w"], space["h"]
        status = status_map.get(space_id, "Unknown")

        # Color coding: Green for Empty, Red for Occupied
        if status == "Empty":
            color = (0, 255, 0)      # Green (BGR)
        elif status == "Occupied":
            color = (0, 0, 255)      # Red (BGR)
        else:
            color = (255, 255, 0)    # Cyan/Yellow default

        # 1. Draw rectangular boundary
        cv2.rectangle(annotated, (x, y), (x + w, y + h), color, thickness)

        # 2. Prepare text label: "Space 1: Occupied"
        label = f"{space_id}: {status}"

        # 3. Draw text with dark background/outline for readability
        cv2.putText(
            annotated,
            label,
            (x + 5, y + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.48,
            (0, 0, 0),
            2,
            cv2.LINE_AA,
        )
        cv2.putText(
            annotated,
            label,
            (x + 5, y + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.48,
            color,
            1,
            cv2.LINE_AA,
        )

    return annotated


def draw_dashboard_summary(image, metrics):
    """
    Draws an analytics dashboard banner at the top of the image.

    Args:
        image (numpy.ndarray): Input image.
        metrics (dict): Summary metrics containing total_spaces, occupied_count, available_count, occupancy_percentage.

    Returns:
        numpy.ndarray: Image with top dashboard banner overlay.
    """
    annotated = image.copy()
    h, w = annotated.shape[:2]

    # Create top dark banner bar (height: 50px)
    banner_height = 50
    overlay = annotated.copy()
    cv2.rectangle(overlay, (0, 0), (w, banner_height), (15, 15, 15), -1)

    # Blend banner for semi-transparent dark background
    alpha = 0.80
    cv2.addWeighted(overlay, alpha, annotated, 1 - alpha, 0, annotated)

    # Dashboard summary string
    total = metrics.get("total_spaces", 0)
    occupied = metrics.get("occupied_count", 0)
    available = metrics.get("available_count", 0)
    pct = metrics.get("occupancy_percentage", 0.0)

    text = f"Total: {total} | Occupied: {occupied} | Available: {available} | Occupancy: {pct}%"

    # Draw dashboard text
    cv2.putText(
        annotated,
        text,
        (15, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    return annotated


def generate_final_visualization(image, parking_spaces, occupancy_results, metrics):
    """
    Generates the complete visualization output with space bounding boxes,
    status labels, and dashboard summary overlay.

    Args:
        image (numpy.ndarray): Input image.
        parking_spaces (list): List of space coordinate dicts.
        occupancy_results (list): List of occupancy detection result dicts.
        metrics (dict): Summary metrics dict.

    Returns:
        numpy.ndarray: Final annotated visualization image.
    """
    # 1. Draw parking space boxes and status labels
    spaces_drawn = draw_space_boxes(image, parking_spaces, occupancy_results)

    # 2. Draw top summary dashboard overlay
    final_output = draw_dashboard_summary(spaces_drawn, metrics)

    return final_output
