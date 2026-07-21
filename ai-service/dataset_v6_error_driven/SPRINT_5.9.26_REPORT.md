# Sprint 5.9.26 — Model Freeze, V6 Inference API Integration, and End-to-End Routing Validation Report

This report presents the validation results, API schema adjustments, and integration test suite verification for the frozen **Model V6** under the dual-tier routing architecture.

---

## 1. Executive Summary & Selection Verdict

### **Final Sprint Verdict: PASS**

#### **Winning Rationale:**
- The frozen **Model V6** weights are successfully frozen and deployed.
- The dual-tier routing controller has been implemented in the processing service, routing detections to agencies according to confidence regions.
- The `/detect` FastAPI endpoint has been expanded to support the new response schema contract.
- The E2E integration test suite has been overhauled, validating all 12 target scenarios programmatically.
- The local server successfully launches, receives image payloads, performs YOLO predictions, and returns correct routing actions and department mappings.

---

## 2. Model Freeze Verification

*   **Model Path:** `c:\Users\Shreyas\OneDrive\Desktop\Main\ai-service\models\best.pt`
*   **Model Version:** `V6 (Error-Driven Optimization Release)`
*   **Weights Integrity Check:** 
    - File SHA-256 Hash: `701D121D3E15CCEAE111A8C66AF93FB35BF12A5DC9F02405414C28F86C21B79C`  
    - Verification: Matches training run validation weights in `ai-service/training/runs/detect/civic_dataset_v6_100ep/weights/best.pt` exactly.
*   **Model Class Mappings:**
    
    | Class Index | YOLO Class Name | Normalization Pattern | Category Name |
    | :---: | :--- | :---: | :--- |
    | **0** | `Pothole` | Case Insensitive | `pothole` |
    | **1** | `Electricity` | Case Insensitive | `electricity` |
    | **2** | `Water Leakage` | Case Insensitive | `water_leakage` |

---

## 3. Department Details & Routing Configuration

### Department Routing Mappings:
Detections are automatically assigned to public service departments based on the identified class:
- `pothole` $\rightarrow$ **`Public Works Department`**
- `electricity` $\rightarrow$ **`Electricity Department`**
- `water_leakage` $\rightarrow$ **`Water Supply Board`**
- `Unknown` (no detection/suppressed) $\rightarrow$ **`None`**

### Confidence Routing Rules (Dual-Tier Pipeline):
Detections undergo multi-tier routing logic to prevent system cluttering:

```
                  [ YOLO Inference ]
                           │
             Is Confidence >= 0.25?
             ├── No ───────────────> [ ACTION: SUPPRESS ]
             │                       - class: "Unknown"
             │                       - confidence: 0.00
             │                       - department: "None"
             └── Yes
                   │
            Is Confidence >= 0.75?
            ├── Yes ──────────────> [ ACTION: AUTO_ROUTE ]
            │                       - Directly dispatched
            └── No ───────────────> [ ACTION: HUMAN_REVIEW ]
                                    - Flagged for Manager Review Queue
```

---

## 4. API Contract & Response Schema Changes

### FastAPI Response Schema (`DetectResponse`):
```python
class DetectResponse(BaseModel):
    filename: str = Field(..., description="The unique name under which the file was saved")
    filepath: str = Field(..., description="The relative path to the saved file")
    issue: str = Field(..., description="The type of issue detected in the image (backwards compatible)")
    class_name: str = Field(..., description="The type of issue detected in the image")
    confidence: float = Field(..., description="Confidence score associated with the detected class/issue")
    routing_action: str = Field(..., description="The automatic or manual review action to take (AUTO_ROUTE, HUMAN_REVIEW, SUPPRESS)")
    department: str = Field(..., description="The agency to route the grievance to")
    model_version: str = Field(..., description="Semantic or major version of model used")
    message: str = Field(..., description="Status message of the upload and analysis confirmation")
```

> [!TIP]
> **API Integration Contract for Frontend:**
> Next-generation client interfaces should dispatch images via `POST http://localhost:8000/detect`.
> - If `routing_action == "AUTO_ROUTE"`, present a confirmation displaying the automatically matched department.
> - If `routing_action == "HUMAN_REVIEW"`, notify the user that their report is being audited.
> - If `routing_action == "SUPPRESS"`, inform the user that no civic issue could be parsed.

---

## 5. Files Changed

1.  **`ai-service\.env`**
    - Updated `YOLO_CONFIDENCE_THRESHOLD=0.25` to support medium-confidence review gates.
2.  **`ai-service\utils\config.py`**
    - Set default Pydantic setting configuration threshold to `0.25`.
3.  **`ai-service\services\detector.py`**
    - Implemented `determine_routing(best_class, best_conf)` to translate predictions into routing actions.
    - Updated `detect_image(image_path)` to incorporate custom mappings and ensure edge suppression overrides.
4.  **`ai-service\app.py`**
    - Modified response object structure and FastAPI Pydantic schema model (`DetectResponse`).
5.  **`ai-service\test_api.py`**
    - Rewrote the test suite to execute self-contained local server checks using the 3-class V6 model instead of the default COCO bus benchmark.

---

## 6. Test Cases Executed & Integration Results

A total of 12 test assertions were executed via the test suite `venv\Scripts\python test_api.py`:

| # | Test Scenario / Assertion | Input / Parameters | Expected Output | Status |
| :-: | :--- | :--- | :--- | :---: |
| 1 | Valid Pothole Detection | `pothole_006.jpg` | class: `pothole`, dept: `Public Works Department` | **PASS** |
| 2 | Valid Electricity Detection | `electricity_003.jpg` | class: `electricity`, dept: `Electricity Department` | **PASS** |
| 3 | Valid Water Leakage Detection | `water_leakage_014.jpg` | class: `water_leakage`, dept: `Water Supply Board` | **PASS** |
| 4 | Multiple Detections Processing | `water_leakage_036.jpg` | Processes and selects top classification. | **PASS** |
| 5 | Negative Image (No object) | `negative_014.jpg` | class: `Unknown`, routing: `SUPPRESS`, dept: `None` | **PASS** |
| 6 | Invalid Image Extension | `temp_test_text.txt` | HTTP 400 Bad Request error returned. | **PASS** |
| 7 | Corrupted Image Content | Garbage bytes | Handled via Pillow: routing: `SUPPRESS` | **PASS** |
| 8 | Boundary Value (0.2499) | `determine_routing(..., 0.2499)` | Action: `SUPPRESS`, class coerced to `Unknown` | **PASS** |
| 9 | Boundary Value (0.25) | `determine_routing(..., 0.25)` | Action: `HUMAN_REVIEW` (Review gate matches) | **PASS** |
| 10 | Boundary Value (0.7499) | `determine_routing(..., 0.7499)` | Action: `HUMAN_REVIEW` | **PASS** |
| 11 | Boundary Value (0.75) | `determine_routing(..., 0.75)` | Action: `AUTO_ROUTE` (Auto routing gate matches) | **PASS** |
| 12 | Department Cross-routing | `determine_routing(..., 0.80)` | No cross-class routing (Pothole $\rightarrow$ Roads, etc.) | **PASS** |

---

## 7. End-to-End Validation Sample Output

### **Valid Pothole Detection (`pothole_006.jpg`)**
```json
{
  "filename": "8d06cd4042e64943b74caf359eef4bc7_pothole_006.jpg",
  "filepath": "uploads\\8d06cd4042e64943b74caf359eef4bc7_pothole_006.jpg",
  "issue": "pothole",
  "class_name": "pothole",
  "confidence": 0.8183,
  "routing_action": "AUTO_ROUTE",
  "department": "Public Works Department",
  "model_version": "V6",
  "message": "Image uploaded and analyzed successfully"
}
```

### **Image with No Detections / Suppressed (`negative_014.jpg`)**
```json
{
  "filename": "2dd5d7828544492895dd7b2d7a623863_negative_014.jpg",
  "filepath": "uploads\\2dd5d7828544492895dd7b2d7a623863_negative_014.jpg",
  "issue": "Unknown",
  "class_name": "Unknown",
  "confidence": 0.0,
  "routing_action": "SUPPRESS",
  "department": "None",
  "model_version": "V6",
  "message": "No detectable object found"
}
```

---

## 8. Known Limitations
- **Object Resolution Ceiling:** While V6 significantly reduces blind spots for sub-resolution potholes, very distant pothole shapes can still result in low confidence scores ($< 0.25$) and trigger suppression.
- **Top Class Selection:** In instances containing multiple disparate classes (e.g. a broken lamppost next to a pothole), the pipeline selects only the single highest-confidence proposal for department routing.

---

## 9. Final Verdict

> [!IMPORTANT]
> **OVERALL VERDICT: PASS**
> The model inference boundary rules, department routing targets, and API schemas have been validated E2E. The API is ready to support integration with frontend components.
