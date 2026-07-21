# Sprint 5.9.23 — Full 3-Class Model Validation and Routing Decision Test

This report details the full 3-class validation results and routing simulation for the YOLOv8n model (`civic_dataset_v5_100ep`) evaluated on the untouched `dataset_v5_pothole_targeted` test split of 24 images.

---

## 1. Key Summary Metadata & Selection Parameters

*   **Pothole performance:** mAP50 = **0.4409**, mAP50-95 = **0.2924** | Detection Recall (threshold 0.50) = **37.50%**
*   **Electricity performance:** mAP50 = **0.8250**, mAP50-95 = **0.5529** | Detection Recall (threshold 0.50) = **46.15%**
*   **Water Leakage performance:** mAP50 = **0.3900**, mAP50-95 = **0.1861** | Detection Recall (threshold 0.50) = **28.57%**
*   **Best confidence threshold:** **0.50** (optimal balance between recall and false alarms)
*   **Recommended routing mode:** **MODE B — CONFIDENCE-BASED ROUTING**
*   **Current project readiness:** **Controlled Pilot / Internal Demo**

---

### **Final Validation Verdict:** `FULL 3-CLASS ROUTING VALIDATION PASSED WITH HUMAN REVIEW`

---

## 2. TASK 1 — Full Test Split Evaluation (Official YOLO Metrics)

Official mean Average Precision (mAP) results calculated by running the YOLO validation suite on the test split split (`images/test`):

| Class Category (ID) | mAP50 | mAP50-95 | Count | Status |
| :--- | :---: | :---: | :---: | :--- |
| **All Classes (Combined)** | **0.5520** | **0.3438** | 28 | Successful generalization |
| **Pothole (0)** | 0.4409 | 0.2924 | 8 | Satisfactory |
| **Electricity (1)** | 0.8250 | 0.5529 | 13 | Exceptionally Strong |
| **Water Leakage (2)** | 0.3900 | 0.1861 | 7 | Moderate (requires further data) |

---

## 3. TASK 2 — Confusion and Routing Analysis

Confusion matrix analysis across confidence thresholds. Rows indicate the actual Ground Truth class; Columns represent the model's predicted class.

### Confusion Matrix (Conf = 0.25)
*   **Pothole (0) → Electricity (1):** 0
*   **Pothole (0) → Water Leakage (2):** 0
*   **Electricity (1) → Pothole (0):** 0
*   **Electricity (1) → Water Leakage (2):** 0
*   **Water Leakage (2) → Pothole (0):** 0
*   **Water Leakage (2) → Electricity (1):** 0

| Actual \ Predicted | Pothole (0) | Electricity (1) | Water Leakage (2) | Background (FN) |
| :--- | :---: | :---: | :---: | :---: |
| **Pothole (0)** | 4 | 0 | 0 | 4 |
| **Electricity (1)** | 0 | 10 | 0 | 3 |
| **Water Leakage (2)** | 0 | 0 | 3 | 4 |
| **Background (FP)** | 9 | 2 | 5 | 0 |

### Confusion Matrix (Conf = 0.50)
| Actual \ Predicted | Pothole (0) | Electricity (1) | Water Leakage (2) | Background (FN) |
| :--- | :---: | :---: | :---: | :---: |
| **Pothole (0)** | 3 | 0 | 0 | 5 |
| **Electricity (1)** | 0 | 6 | 0 | 7 |
| **Water Leakage (2)** | 0 | 0 | 2 | 5 |
| **Background (FP)** | 3 | 0 | 1 | 0 |

### Confusion Matrix (Conf = 0.75)
| Actual \ Predicted | Pothole (0) | Electricity (1) | Water Leakage (2) | Background (FN) |
| :--- | :---: | :---: | :---: | :---: |
| **Pothole (0)** | 3 | 0 | 0 | 5 |
| **Electricity (1)** | 0 | 3 | 0 | 10 |
| **Water Leakage (2)** | 0 | 0 | 1 | 6 |
| **Background (FP)** | 0 | 0 | 0 | 0 |

> [!NOTE]
> **Zero Class Confusion:** Across all tested thresholds, the model registered exactly **0 cross-class classification errors** (e.g. diagnosing a Pothole as Electricity). Predictions were either correct or classified as Background.

---

## 4. TASK 3 — Routing Decision Simulation

Results of simulating the end-to-end application workflow over the 24 images (4 negative images, 20 positive images):

| Threshold | Correct Routing | Wrong Routing | Missed Issue | False Alarm | Clean Correct |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Conf = 0.25** | 17 (70.83%) | 0 (0.00%) | 1 (4.17%) | 6 (25.00%) | 4 |
| **Conf = 0.50** | 15 (62.50%) | 0 (0.00%) | 5 (20.83%) | 4 (16.67%) | 4 |
| **Conf = 0.75** | 11 (45.83%) | 0 (0.00%) | 13 (54.17%) | 0 (0.00%) | 4 |

---

## 5. TASK 4 — Class Safety Analysis (Threshold = 0.50)

Safety breakdown at operational threshold 0.50:

| Metric | Pothole (0) | Electricity (1) | Water Leakage (2) |
| :--- | :---: | :---: | :---: |
| **Detection Recall** | 37.50% | 46.15% | 28.57% |
| **Classification Accuracy (Precision)** | 50.00% | 100.00% | 66.67% |
| **Wrong-Class Rate** | 0.00% | 0.00% | 0.00% |
| **False-Positive Rate** | 50.00% | 0.00% | 33.33% |
| **Routing Success Rate** | 37.50% | 85.71% | 40.00% |

---

## 6. TASK 5 — Production Routing Recommendation

We recommend **MODE B — CONFIDENCE-BASED ROUTING** with a dual operational pipeline:
*   **High Confidence (Conf $\ge$ 0.75) $\rightarrow$ Full Automatic Routing:** Detections at this tier have a **0% false-positive rate** and **0% wrong-class rate** across all classes, meaning they can be dispatched immediately to correct departments without human bottlenecking.
*   **Medium Confidence (0.25 $\le$ Conf < 0.75) $\rightarrow$ Human Review:** Detections in this range are flagged and queued for manual manager confirmation to filter out the false alarms (**50.00%** for potholes, **33.33%** for water leaks) before routing.
*   **Low Confidence (Conf < 0.25) $\rightarrow$ Ignored:** Suppressed to prevent system cluttering.

---

## 7. TASK 6 — Final Project Readiness Recommendation

*   **Current Readiness:** **Controlled Pilot / Internal Demo**
*   **Barriers to Full Production:**
    1. **High Miss-Detection Rate:** The model misses up to 54.17% of issues overall at higher thresholds.
    2. **Low-Confidence Clutter:** Background noise false alarms are present at confidence thresholds below 0.50. 
*   **Strengths:** The routing classification system is exceptionally safe due to **zero cross-class confusion**.
