# Dataset Split Report - Smart Public Grievance Management System

This report verifies the training and validation split details for the YOLOv8 custom grievance model dataset.

## Summary

*   **Total Images:** 315
*   **Training Images Count:** 252 (80.00%)
*   **Validation Images Count:** 63 (20.00%)
*   **Missing Image-Label Pairs:** 0
*   **Duplicate Files Found:** 0

---

## Dataset Class Distribution & Balance

| Class | Train | Validation | Total |
| :--- | :---: | :---: | :---: |
| **Pothole** (Class 0) | 84 | 21 | 105 |
| **Electricity** (Class 1) | 84 | 21 | 105 |
| **Water Leakage** (Class 2) | 84 | 21 | 105 |
| **TOTAL** | **252** | **63** | **315** |

---

## Split Verification Checklist

The split process has been verified against the following quality rules:
*   [x] **Bipartite Matching:** Verified that every image in `images/train` has a matching annotation file in `labels/train`.
*   [x] **Validation Bipartite Matching:** Verified that every image in `images/val` has a matching annotation file in `labels/val`.
*   [x] **Overlapping Check:** Checked that no image or annotation exists in both training and validation sets simultaneously (preventing data leakage).
*   [x] **Class Consistency:** Verified that all labels contain class IDs within the active range `[0, 1, 2]`.
*   [x] **Coordinate Range Check:** Verified that all YOLO bounding-box normalized coordinates `[x_center, y_center, width, height]` lie strictly between `0.0` and `1.0`.
