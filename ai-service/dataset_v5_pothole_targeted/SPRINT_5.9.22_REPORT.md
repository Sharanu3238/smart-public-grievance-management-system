# Sprint 5.9.22 — Controlled External Comparison: dataset_v4 vs dataset_v5

This report details the comparison evaluation between **Model A (dataset_v4)** and **Model B (dataset_v5)** over the exact same 20 isolated external pothole test images (containing 47 ground-truth potholes) located in `external_pothole_split/external_test/`.

---

## 1. Executive Summary & Final Actionable Verdict

### **Final Verdict:** `DATASET_V5 IS BETTER — CONTINUE WITH V5`

#### **Rationale for the Project Goal:**
The primary workflow is:  
`USER UPLOADS IMAGE → MODEL DETECTS CIVIC ISSUE → SYSTEM ROUTES IT TO THE CORRECT DEPARTMENT.`

For this system to work reliably in the real world:
1. **Recall is the critical gateway:** If the model misses a pothole entirely (False Negative), the system cannot route the issue, leaving the road hazard unreported and unfixed. Model B (dataset_v5) successfully detected **24 out of 47 potholes (51.06% recall)**, compared to Model A (dataset_v4) which only detected **16 out of 47 (34.04% recall)**.
2. **F1 and Accuracy Improvements:** Despite a trade-off in precision due to a higher false-positive rate at low confidence thresholds (17 FPs for v5 vs 5 FPs for v4), Model B achieves a higher overall **F1 Score (54.55% vs 47.06%)** and **Detection Accuracy (37.50% vs 30.77%)** at confidence threshold 0.25. 
3. **Generalization to Hard Cases:** Model B successfully resolved **5 out of 8 previously blind-spot test images** (e.g. img-107, img-161, img-390, img-394, img-634) that were completely missed by both Model v3 and v4. This includes detecting small, distant, and dense clusters of potholes, which proves the targeted dataset enrichment strategy was highly effective.

---

## 2. Summary Metrics at All Confidence Thresholds (IoU = 0.50)

### Model A — dataset_v4 (`best.pt`)
*   **Threshold 0.25:** TP: 16 | FP: 5 | FN: 31 | Precision: 0.7619 | Recall: 0.3404 | F1 Score: 0.4706 | Detection Accuracy: 0.3077
*   **Threshold 0.50:** TP: 14 | FP: 1 | FN: 33 | Precision: 0.9333 | Recall: 0.2979 | F1 Score: 0.4516 | Detection Accuracy: 0.2917
*   **Threshold 0.75:** TP: 4  | FP: 0 | FN: 43 | Precision: 1.0000 | Recall: 0.0851 | F1 Score: 0.1569 | Detection Accuracy: 0.0851

### Model B — dataset_v5 (`best.pt` - Ours)
*   **Threshold 0.25:** TP: 24 | FP: 17 | FN: 23 | Precision: 0.5854 | Recall: 0.5106 | F1 Score: 0.5455 | Detection Accuracy: 0.3750
*   **Threshold 0.50:** TP: 18 | FP: 7  | FN: 29 | Precision: 0.7200 | Recall: 0.3830 | F1 Score: 0.5000 | Detection Accuracy: 0.3333
*   **Threshold 0.75:** TP: 12 | FP: 2  | FN: 35 | Precision: 0.8571 | Recall: 0.2553 | F1 Score: 0.3934 | Detection Accuracy: 0.2449

---

## 3. Direct Metrics Comparison Table (Threshold = 0.25)

| Metric | dataset_v4 (Model A) | dataset_v5 (Model B) | Better Model |
| :--- | :---: | :---: | :---: |
| **Precision** | **0.7619** | 0.5854 | **dataset_v4** (Fewer False Positives) |
| **Recall** | 0.3404 | **0.5106** | **dataset_v5** (+17.02% gain) |
| **F1 Score** | 0.4706 | **0.5455** | **dataset_v5** (+7.49% gain) |
| **Detection Accuracy** | 0.3077 | **0.3750** | **dataset_v5** (+6.73% gain) |

---

## 4. Per-Image Detection Breakdown (Conf = 0.25, NMS IoU = 0.45)

| Image Filename | Ground Truth Potholes | Model A (v4)tp/fp | Model B (v5)tp/fp | Winner | Description |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `img-107_jpg.rf.2e40485785f6e5e2efec404301b235c2.jpg` | 1 | 0 / 0 | 1 / 2 | **Model B (v5)** | Resolves blind spot; V5 detects the pothole. |
| `img-146_jpg.rf.61be25b3053a51f622a244980545df2b.jpg` | 1 | 0 / 0 | 0 / 0 | **Tie** | Missed by both models. |
| `img-161_jpg.rf.211541e7178a4a93ec0680f26b905427.jpg` | 1 | 0 / 1 | 1 / 1 | **Model B (v5)** | Resolves blind spot; V5 matches GT. |
| `img-179_jpg.rf.8632eb0d9b75fefe144829e67b75015a.jpg` | 5 | 3 / 0 | 4 / 2 | **Model B (v5)** | V5 has higher recall (+1 TP). |
| `img-195_jpg.rf.f77a8f4d432a9a89235168ff8e09a650.jpg` | 2 | 2 / 0 | 2 / 0 | **Tie** | Perfect matching by both models. |
| `img-217_jpg.rf.20e267cdb167c43140e67ec9f5328040.jpg` | 2 | 1 / 1 | 2 / 4 | **Model B (v5)** | V5 detects all GTs (+1 TP), but registers FGs. |
| `img-269_jpg.rf.f51d9eb8d02a34ac01d4a486cbfbdd4f.jpg` | 2 | 1 / 1 | 1 / 0 | **Model B (v5)** | V5 has fewer false positives. |
| `img-276_jpg.rf.acc167b63d79ab3b99fd64b4109f86d4.jpg` | 1 | 1 / 0 | 1 / 2 | **Model A (v4)** | V4 has fewer false positives. |
| `img-364_jpg.rf.e385283baa4507e9b6a79c9e92c4b453.jpg` | 1 | 1 / 0 | 1 / 0 | **Tie** | Both models matched successfully. |
| `img-390_jpg.rf.3eeb4356ab769c112edf7f482110f8ee.jpg` | 1 | 0 / 0 | 1 / 0 | **Model B (v5)** | Resolves blind spot; V5 detects successfully. |
| `img-394_jpg.rf.2182e193f33ed5bcce45df7df27032f7.jpg` | 2 | 0 / 0 | 1 / 0 | **Model B (v5)** | Resolves blind spot; V5 locates distant pothole. |
| `img-398_jpg.rf.0c484369fdb23fdec1b9250477fc5d1d.jpg` | 1 | 0 / 0 | 0 / 0 | **Tie** | Missed by both models. |
| `img-410_jpg.rf.5f10f2bbde7900b5348aeaed6116b901.jpg` | 1 | 0 / 1 | 0 / 2 | **Model A (v4)** | V4 has fewer false positives. |
| `img-42_jpg.rf.532fb8eb05b1efc570c5e4165e614201.jpg` | 2 | 1 / 0 | 1 / 2 | **Model A (v4)** | V4 has fewer false positives. |
| `img-44_jpg.rf.c0be863d6030f5d0cb241331c14ee532.jpg` | 2 | 1 / 0 | 2 / 0 | **Model B (v5)** | V5 has perfect double detection. |
| `img-472_jpg.rf.d71e2cae627685f2ad46e4182bbfb68a.jpg` | 1 | 1 / 0 | 1 / 0 | **Tie** | Both models matching. |
| `img-576_jpg.rf.f6cd32a51b0c518b58ff750ecab687d1.jpg` | 2 | 1 / 0 | 1 / 0 | **Tie** | Identical results. |
| `img-634_jpg.rf.42d6e4ebdda859ab935130b75ae5808f.jpg` | 13 | 0 / 0 | 2 / 0 | **Model B (v5)** | Resolves blind spot; V5 detects 2 heavy potholes. |
| `img-68_jpg.rf.c8886ded10d01454f789376e4234ae74.jpg` | 2 | 2 / 0 | 2 / 0 | **Tie** | Perfect match on both. |
| `img-98_jpg.rf.667209472947ff4d519f65c6e206a7c3.jpg` | 4 | 1 / 1 | 0 / 2 | **Model A (v4)** | V4 has higher recall and fewer FPs. |

---

## 5. Direct Model Comparison Detailed Analytics

1.  **Total potholes detected by each model:**
    *   Model A (dataset_v4): **16**
    *   Model B (dataset_v5): **24**
2.  **Total potholes missed by each model:**
    *   Model A (dataset_v4): **31**
    *   Model B (dataset_v5): **23**
3.  **Total false positives:**
    *   Model A (dataset_v4): **5**
    *   Model B (dataset_v5): **17**
4.  **Number of test images where v4 performed better:** **4**
5.  **Number of test images where v5 performed better:** **9**
6.  **Number of ties:** **7**
7.  **Images missed by both models:** **3**
    *   `img-146_jpg.rf.61be25b3053a51f622a244980545df2b.jpg`
    *   `img-398_jpg.rf.0c484369fdb23fdec1b9250477fc5d1d.jpg`
    *   `img-410_jpg.rf.5f10f2bbde7900b5348aeaed6116b901.jpg`
8.  **Images detected only by v4:** **1**
    *   `img-98_jpg.rf.667209472947ff4d519f65c6e206a7c3.jpg`
9.  **Images detected only by v5:** **5**
    *   `img-107_jpg.rf.2e40485785f6e5e2efec404301b235c2.jpg`
    *   `img-161_jpg.rf.211541e7178a4a93ec0680f26b905427.jpg`
    *   `img-390_jpg.rf.3eeb4356ab769c112edf7f482110f8ee.jpg`
    *   `img-394_jpg.rf.2182e193f33ed5bcce45df7df27032f7.jpg`
    *   `img-634_jpg.rf.42d6e4ebdda859ab935130b75ae5808f.jpg`
10. **Which model performs better on difficult external potholes:**
    *   **Model B (dataset_v5)** performs significantly better. V5 successfully resolves 5 of the 8 previously completely missed images, demonstrating its capability to detect small/distant pothole clusters (e.g. `img-634`) and highly shadowed/obscured patterns that were completely invisible to the v4 model.

---

## 6. Actionable Recommendation and Operational Settings

*   **Production Deployment Confidence Threshold Suggestion:**  
    For production, we recommend running Model B (dataset_v5) at a confidence threshold of **0.50** (or a dual-routing pipeline: self-clearing routing at threshold 0.50, and human-in-the-loop manual auditing for detections between 0.25 and 0.50).  
    Running v5 at **0.50** achieves:
    *   Recall of **38.30%** (still better than v4's best recall of 34.04% at 0.25).
    *   Precision of **72.00%** (mitigating the false alarm rate).
    *   F1 Score of **50.00%** and Detection Accuracy of **33.33%**.
*   **Production-Ready Status:**  
    Neither model should be declared fully production-ready without a human-in-the-loop verification step, as the external test recall (51.06% maximum at 0.25) leaves around 49% of out-of-domain potholes undetected. However, `dataset_v5` is a major step forward, and using it as a routing trigger under the suggested dual confidence pipeline will yield the highest routing accuracy.
