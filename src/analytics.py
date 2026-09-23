import cv2


def calculate_occupancy_metrics(occupancy_results):
    """
    Calculates summary statistics from occupancy detection results.

    Args:
        occupancy_results (list of dict): List containing status of each space.

    Returns:
        dict: Summary statistics containing total, occupied, available, and occupancy percentage.
    """
    total_spaces = len(occupancy_results)
    occupied_count = sum(1 for item in occupancy_results if item.get("status") == "Occupied")
    available_count = total_spaces - occupied_count
    occupancy_percentage = (occupied_count / total_spaces * 100.0) if total_spaces > 0 else 0.0

    return {
        "total_spaces": total_spaces,
        "occupied_count": occupied_count,
        "available_count": available_count,
        "occupancy_percentage": round(occupancy_percentage, 1),
    }


def draw_analytics_dashboard(image, metrics):
    """
    Draws an overlay dashboard banner at the top of the image summarizing parking stats.

    Args:
        image (numpy.ndarray): Input image.
        metrics (dict): Summary metrics dictionary from calculate_occupancy_metrics.

    Returns:
        numpy.ndarray: Image with top dashboard banner overlay.
    """
    annotated = image.copy()
    h, w = annotated.shape[:2]

    # Create top dark banner rectangle (height: 50px)
    banner_height = 50
    overlay = annotated.copy()
    cv2.rectangle(overlay, (0, 0), (w, banner_height), (20, 20, 20), -1)

    # Blend overlay with original image (semi-transparent background)
    alpha = 0.75
    cv2.addWeighted(overlay, alpha, annotated, 1 - alpha, 0, annotated)

    # Prepare summary text line
    total = metrics["total_spaces"]
    occupied = metrics["occupied_count"]
    available = metrics["available_count"]
    pct = metrics["occupancy_percentage"]

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
