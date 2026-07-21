# Annotation Correction Manifest

This manifest documents the 12 files undergoing boundary tightening, label addition, or frame deduplication.

| Image Path | Class | Problem Type | Required Correction | Status |
| :--- | :--- | :--- | :--- | :--- |
| `dataset_improvement/source/corrections/electricity_035.jpg` | Electricity | LOW_CONFIDENCE / FALSE_POSITIVE | Add missing wire annotation and adjust background box | Completed |
| `dataset_improvement/source/corrections/pothole_008.jpg` | Pothole | MISSED_OBJECT | Add missing far-distance pothole annotation | Completed |
| `dataset_improvement/source/corrections/pothole_016.jpg` | Pothole | MISSED_OBJECT | Add missing pothole under tree shadow lines | Completed |
| `dataset_improvement/source/corrections/pothole_018.jpg` | Pothole | LOW_CONFIDENCE | Re-annotate small pothole with tighter centering | Completed |
| `dataset_improvement/source/corrections/pothole_041.jpg` | Pothole | MISSED_OBJECT | Add missing pothole on border line | Completed |
| `dataset_improvement/source/corrections/water_leakage_014.jpg` | Water Leakage | MISSED_OBJECT / FALSE_POSITIVE | Add missing thin specular fluid runoff strip, suppress shadow box | Completed |
| `dataset_improvement/source/corrections/water_leakage_046.jpg` | Water Leakage | FALSE_POSITIVE | Remove false general wet gloss detection line | Completed |
| `dataset_improvement/source/corrections/pothole_024.jpg` | Pothole | Compound Bounding Box | Split large composite pothole crack box into 2 tight boxes | Completed |
| `dataset_improvement/source/corrections/water_leakage_006.jpg` | Water Leakage | Loose Boundary | Crop bounding borders tightly along visual shiny wet sheen | Completed |
| `dataset_improvement/source/corrections/water_leakage_038.jpg` | Water Leakage | Loose Boundary | Tighten bounding box edges to dry concrete line | Completed |
| `dataset_improvement/source/corrections/electricity_022.jpg` | Electricity | Near-Duplicate Frame | Identify as duplicate frame sequence (marked for removal in merge) | Pending Merge |
| `dataset_improvement/source/corrections/electricity_023.jpg` | Electricity | Near-Duplicate Frame | Identify as duplicate frame sequence (marked for retention) | Retained |
