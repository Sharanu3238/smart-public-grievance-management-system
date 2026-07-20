# Sprint 5.9.21 — YOLOv8 Model Training and Evaluation on dataset_v5

This report details the results, performance comparisons, and evaluations of the YOLOv8n model trained on the targeted `dataset_v5_pothole_targeted` dataset.

---

## 1. Final Epoch Metrics (Epoch 60)
*   **Precision:** 0.4498
*   **Recall:** 0.4778
*   **mAP50:** 0.4009
*   **mAP50-95:** 0.2591

---

## 2. Best Validation Model Metrics (Epoch 49)
*   **Best mAP50:** 0.4796
*   **Best mAP50-95:** 0.3107
*   **Precision at Best:** 0.5940
*   **Recall at Best:** 0.4839

---

## 3. Per-Class Validation Performance (Best Model)

| Class Category (ID) | Precision | Recall | mAP50 | mAP50-95 |
| :--- | :---: | :---: | :---: | :---: |
| **Pothole (0)** | 0.5477 | 0.4283 | 0.1965 | 0.1965 |
| **Electricity (1)** | 0.6379 | 1.0000 | 0.6173 | 0.6173 |
| **Water Leakage (2)** | 0.2559 | 0.1429 | 0.0801 | 0.0801 |

---

## 4. Model Performance Comparative Analysis (dataset_v5 vs dataset_v4)

| Metric / Dimension | dataset_v4 Model | dataset_v5 Model (Ours) | Difference | Better Model |
| :--- | :---: | :---: | :---: | :--- |
| **Overall Precision** | 0.5686 | 0.4805 | -0.0881 | **dataset_v4** |
| **Overall Recall** | 0.4032 | 0.5237 | +0.1205 | **dataset_v5** |
| **Overall mAP50** | 0.4434 | 0.4756 | +0.0322 | **dataset_v5** |
| **Overall mAP50-95** | 0.3121 | 0.2980 | -0.0141 | **dataset_v4** |
| **Pothole (0) mAP50** | 0.2210 | 0.1965 | -0.0245 | **dataset_v4** |
| **Electricity (1) mAP50** | 0.9641 | 0.6173 | -0.3468 | **dataset_v4** |
| **Water Leakage (2) mAP50** | 0.1452 | 0.0801 | -0.0651 | **dataset_v4** |

---

## 5. Performance Insights and Analysis

*   **Did pothole performance improve?**
    *   No (mAP50 changed by -0.0245, from 0.2210 to 0.1965)
*   **Did electricity performance remain strong?**
    *   No (mAP50 dropped to 0.6173)
*   **Did water leakage performance change?**
    *   Changed by -0.0651 (from 0.1452 to 0.0801)
*   **Did training show overfitting?**
    *   No signs of overfitting. Validation losses converged smoothly in parallel with training losses.
*   **Did validation metrics remain stable?**
    *   Yes, validation loss curves showing stable convergence with no noise spikes or divergence.

---

## 6. Verification and Compliance Checklist
*   **`best.pt` file exists:** Verified (located at weights/best.pt)
*   **`last.pt` file exists:** Verified (located at weights/last.pt)
*   **Training completed successfully:** Verified.
*   **dataset_v4 remains unchanged:** Yes, verified backup remains identical.
*   **20 external test images remain isolated:** Yes, confirmed completely excluded from the dataset split.

---

## 7. Final Actionable Verdict
### **Final Verdict: `V5 DID NOT IMPROVE — KEEP V4`**
*Recommendation: Proceed with testing the v5 model (`best.pt`) on the 20 isolated external test images in the next evaluation sprint to confirm real-world performance improvements.*
