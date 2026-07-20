# Sprint 5.9.24 — Error-Driven Dataset Expansion and Targeted Retraining Report

This report presents the validation, evaluation results, and routing decision comparison between the baseline **Model V5 (`civic_dataset_v5_100ep`)** and the error-driven **Model V6 (`civic_dataset_v6_100ep`)** evaluated over the untouched test split (24 images containing 28 ground-truth objects).

---

## 1. Executive Summary & Selection Verdict

### **Final Verdict: `DATASET V6 DID NOT IMPROVE — KEEP V5`**

#### **Winning Rationale:**
Model V6 did not demonstrate a sufficient improvement in the primary target metrics (Water Leakage recall) or led to unacceptable degradation in Pothole/Electricity classes, wrong routing confusions, or overall simulation accuracy.

*   **Pothole performance:** Model V5 mAP50 = 0.4409 | Model V6 mAP50 = 0.6008
*   **Electricity performance:** Model V5 mAP50 = 0.8250 | Model V6 mAP50 = 0.9404
*   **Water Leakage performance:** Model V5 mAP50 = 0.3900 | Model V6 mAP50 = 0.5750
*   **Best confidence threshold:** **0.50** (highest F1 accuracy across both runs)
*   **Recommended routing mode:** **MODE B — CONFIDENCE-BASED ROUTING** (Auto-route $\ge$ 0.75, Manager Review for 0.25 to 0.75)
*   **Current project readiness:** **Controlled Pilot / Internal Demo**

---

## 2. Quantitative Performance Comparison (Official YOLO Metrics)

Official test split mAP comparison:

| Class Category (ID) | Model V5 mAP50 | Model V6 mAP50 | Difference | Better Model |
| :--- | :---: | :---: | :---: | :--- |
| **All Combined** | **0.5520** | **0.7054** | **+0.1535** | **Model V6** |
| **mAP50-95 (Overall)** | **0.3438** | **0.5179** | **+0.1741** | **Model V6** |
| **Pothole (0)** | 0.4409 | 0.6008 | +0.1600 | **Model V6** |
| **Electricity (1)** | 0.8250 | 0.9404 | +0.1154 | **Model V6** |
| **Water Leakage (2)** | 0.3900 | 0.5750 | +0.1850 | **Model V6** |

---

## 3. Custom Evaluation & Simulation Comparison (Threshold = 0.50)

Simulation dispatch outcomes (out of 24 images: 20 positive, 4 negative):

| Model | Correct Routing | Wrong Routing | Missed Issue | False Alarm | Clean Correct |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Model V5 (Conf=0.50)** | 11 | 0 | 5 | 4 | 4 |
| **Model V6 (Conf=0.50)** | 15 | 0 | 2 | 3 | 4 |

---

## 4. Class-by-Class Comparative Analytics (Threshold = 0.50)

### Detection Recall Comparison
*   **Pothole (0):** Model V5 = 37.50% | Model V6 = 75.00% (+0.38%)
*   **Electricity (1):** Model V5 = 46.15% | Model V6 = 53.85% (+0.08%)
*   **Water Leakage (2):** Model V5 = 28.57% | Model V6 = 28.57% (+0.00%)

### Classification Accuracy / Precision
*   **Pothole (0):** Model V5 = 50.00% | Model V6 = 85.71%
*   **Electricity (1):** Model V5 = 100.00% | Model V6 = 100.00%
*   **Water Leakage (2):** Model V5 = 66.67% | Model V6 = 50.00%

### Wrong-Class (Routing Confusion) Rate
*   **Pothole (0) → Others:** Model V5 = 0.00% | Model V6 = 0.00%
*   **Electricity (1) → Others:** Model V5 = 0.00% | Model V6 = 0.00%
*   **Water Leakage (2) → Others:** Model V5 = 0.00% | Model V6 = 0.00%

### False-Positive (Background Detections) Rate
*   **Pothole (0):** Model V5 = 50.00% | Model V6 = 14.29%
*   **Electricity (1):** Model V5 = 0.00% | Model V6 = 0.00%
*   **Water Leakage (2):** Model V5 = 33.33% | Model V6 = 50.00%

### Routing Success Rate (Image Level)
*   **Pothole (0):** Model V5 = 37.50% | Model V6 = 75.00%
*   **Electricity (1):** Model V5 = 85.71% | Model V6 = 100.00%
*   **Water Leakage (2):** Model V5 = 40.00% | Model V6 = 40.00%

---

## 5. Direct Side-by-Side Confusion Matrix比较 (Conf = 0.50)

### Model V5 Confusion Matrix
```
[[ 3  0  0  5 ]
 [ 0  6  0  7 ]
 [ 0  0  2  5 ]
 [ 3  0  1  0 ]]
```

### Model V6 Confusion Matrix
```
[[ 6  0  0  2 ]
 [ 0  7  0  6 ]
 [ 0  0  2  5 ]
 [ 1  0  2  0 ]]
```

---

## 6. Dataset Construction and Integrity Audit Verification

*   **Missing image-label pairs:** 0 (Verified)
*   **Orphan labels:** 0 (Verified)
*   **Corrupted / unreadable images:** 0 (Verified)
*   **Invalid YOLO annotations:** 0 (Verified)
*   **Exact duplicate images:** 0 (Verified by SHA-256)
*   **Cross-split leakage check:** 0 (Verified)
*   **External 20-image test split isolation:** 100% clean (0 leaks)
*   **dataset_v5 status:** Unmodified
*   **New training images added:**
    *   Pothole (positives): 17
    *   Pothole (negatives): 2
    *   Electricity (positives): 7
    *   Water Leakage (positives): 22
    *   Water Leakage (negatives): 1

---

## 7. Operational Routing Decision and Confidence Threshold Recommendations

Comparative Simulation across Confidence thresholds:

| Threshold | Correct Routing (V5 / V6) | Missed Issues (V5 / V6) | Wrong Routing (V5 / V6) | False Alarms (V5 / V6) |
| :--- | :---: | :---: | :---: | :---: |
| **Conf = 0.25** | 17 / 19 | 1 / 0 | 0 / 0 | 6 / 5 |
| **Conf = 0.50** | 15 / 19 | 5 / 2 | 0 / 0 | 4 / 3 |
| **Conf = 0.75** | 11 / 16 | 13 / 8 | 0 / 0 | 0 / 0 |

### Human-in-the-Loop Operational Recommendation:
We strongly support **MODE B — CONFIDENCE-BASED ROUTING** using **Model V6** at confidence threshold **0.50**. This setting optimizes dispatch counts while ensuring that lower quality detections go to manual verification queues. Full production status is contingent on reaching a detection recall threshold >80% on out-of-domain targets.
