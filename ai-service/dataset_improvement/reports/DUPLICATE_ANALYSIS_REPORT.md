# Duplicate Analysis Report

This status report logs SHA-256 exact binary hashes and Perceptual dHash verification comparisons across `dataset_v2` and `dataset_improvement` splits.

---

## 1. Exact SHA-256 Binary Duplicates
*   **Total Exact Duplicate Clusters Staged:** 12

### Cluster 1
*   `dataset_v2\images\test\electricity_035.jpg`
*   `dataset_improvement\source\corrections\electricity_035.jpg`

### Cluster 2
*   `dataset_v2\images\test\pothole_008.jpg`
*   `dataset_improvement\source\corrections\pothole_008.jpg`

### Cluster 3
*   `dataset_v2\images\test\pothole_016.jpg`
*   `dataset_improvement\source\corrections\pothole_016.jpg`

### Cluster 4
*   `dataset_v2\images\test\pothole_018.jpg`
*   `dataset_improvement\source\corrections\pothole_018.jpg`

### Cluster 5
*   `dataset_v2\images\test\pothole_041.jpg`
*   `dataset_improvement\source\corrections\pothole_041.jpg`

### Cluster 6
*   `dataset_v2\images\test\water_leakage_014.jpg`
*   `dataset_improvement\source\corrections\water_leakage_014.jpg`

### Cluster 7
*   `dataset_v2\images\test\water_leakage_046.jpg`
*   `dataset_improvement\source\corrections\water_leakage_046.jpg`

### Cluster 8
*   `dataset_v2\images\train\electricity_022.jpg`
*   `dataset_improvement\source\corrections\electricity_022.jpg`

### Cluster 9
*   `dataset_v2\images\train\electricity_023.jpg`
*   `dataset_improvement\source\corrections\electricity_023.jpg`

### Cluster 10
*   `dataset_v2\images\train\pothole_024.jpg`
*   `dataset_improvement\source\corrections\pothole_024.jpg`

### Cluster 11
*   `dataset_v2\images\train\water_leakage_006.jpg`
*   `dataset_improvement\source\corrections\water_leakage_006.jpg`

### Cluster 12
*   `dataset_v2\images\train\water_leakage_038.jpg`
*   `dataset_improvement\source\corrections\water_leakage_038.jpg`

---

## 2. Perceptual Similarity Near-Duplicates (Mismatch bits <= 2)
*   **Total Near-Duplicate Pairs Detected:** 167

| File 1 | File 2 | Distance (Bits Diff) | Evaluation Status |
| :--- | :--- | :---: | :--- |
| `dataset_v2\images\test\electricity_025.jpg` | `dataset_v2\images\train\electricity_028.jpg` | 2 | Needs review |
| `dataset_v2\images\test\electricity_025.jpg` | `dataset_v2\images\train\electricity_030.jpg` | 2 | Needs review |
| `dataset_v2\images\test\pothole_016.jpg` | `dataset_v2\images\test\pothole_018.jpg` | 2 | Needs review |
| `dataset_v2\images\test\pothole_016.jpg` | `dataset_v2\images\train\pothole_013.jpg` | 0 | Needs review |
| `dataset_v2\images\test\pothole_016.jpg` | `dataset_improvement\source\corrections\pothole_018.jpg` | 2 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\test\pothole_018.jpg` | `dataset_v2\images\train\pothole_013.jpg` | 2 | Needs review |
| `dataset_v2\images\test\pothole_018.jpg` | `dataset_improvement\source\corrections\pothole_016.jpg` | 2 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\test\water_leakage_021.jpg` | `dataset_v2\images\train\water_leakage_019.jpg` | 2 | Needs review |
| `dataset_v2\images\test\water_leakage_021.jpg` | `dataset_v2\images\train\water_leakage_024.jpg` | 1 | Needs review |
| `dataset_v2\images\test\water_leakage_037.jpg` | `dataset_v2\images\train\water_leakage_039.jpg` | 1 | Needs review |
| `dataset_v2\images\test\water_leakage_037.jpg` | `dataset_v2\images\train\water_leakage_040.jpg` | 2 | Needs review |
| `dataset_v2\images\test\water_leakage_037.jpg` | `dataset_v2\images\val\water_leakage_042.jpg` | 1 | Needs review |
| `dataset_v2\images\test\water_leakage_046.jpg` | `dataset_v2\images\train\water_leakage_043.jpg` | 1 | Needs review |
| `dataset_v2\images\test\water_leakage_046.jpg` | `dataset_v2\images\train\water_leakage_048.jpg` | 1 | Needs review |
| `dataset_v2\images\test\water_leakage_046.jpg` | `dataset_v2\images\val\water_leakage_045.jpg` | 1 | Needs review |
| `dataset_v2\images\train\electricity_001.jpg` | `dataset_v2\images\train\electricity_004.jpg` | 0 | Needs review |
| `dataset_v2\images\train\electricity_001.jpg` | `dataset_v2\images\val\electricity_003.jpg` | 1 | Needs review |
| `dataset_v2\images\train\electricity_004.jpg` | `dataset_v2\images\val\electricity_003.jpg` | 1 | Needs review |
| `dataset_v2\images\train\electricity_007.jpg` | `dataset_v2\images\train\electricity_010.jpg` | 1 | Needs review |
| `dataset_v2\images\train\electricity_007.jpg` | `dataset_v2\images\train\electricity_012.jpg` | 1 | Needs review |
| `dataset_v2\images\train\electricity_010.jpg` | `dataset_v2\images\train\electricity_012.jpg` | 0 | Needs review |
| `dataset_v2\images\train\electricity_016.jpg` | `dataset_v2\images\train\electricity_018.jpg` | 1 | Needs review |
| `dataset_v2\images\train\electricity_018.jpg` | `dataset_v2\images\val\electricity_013.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_021.jpg` | `dataset_v2\images\val\electricity_019.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_022.jpg` | `dataset_v2\images\val\electricity_019.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_027.jpg` | `dataset_v2\images\train\electricity_028.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_027.jpg` | `dataset_v2\images\train\electricity_030.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_028.jpg` | `dataset_v2\images\train\electricity_030.jpg` | 0 | Needs review |
| `dataset_v2\images\train\electricity_042.jpg` | `dataset_v2\images\val\electricity_037.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_042.jpg` | `dataset_v2\images\val\electricity_040.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_043.jpg` | `dataset_v2\images\train\electricity_046.jpg` | 1 | Needs review |
| `dataset_v2\images\train\electricity_043.jpg` | `dataset_v2\images\train\electricity_048.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_049.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_051.jpg` | 2 | Needs review |
| `dataset_v2\images\train\electricity_049.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_052.jpg` | 2 | Needs review |
| `dataset_v2\images\train\pothole_001.jpg` | `dataset_v2\images\val\pothole_006.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_012.jpg` | `dataset_v2\images\val\pothole_007.jpg` | 2 | Needs review |
| `dataset_v2\images\train\pothole_013.jpg` | `dataset_improvement\source\corrections\pothole_016.jpg` | 0 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\pothole_013.jpg` | `dataset_improvement\source\corrections\pothole_018.jpg` | 2 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\pothole_019.jpg` | `dataset_v2\images\train\pothole_021.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_019.jpg` | `dataset_v2\images\train\pothole_022.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_019.jpg` | `dataset_v2\images\train\pothole_024.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_019.jpg` | `dataset_improvement\source\corrections\pothole_024.jpg` | 0 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\pothole_021.jpg` | `dataset_v2\images\train\pothole_022.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_021.jpg` | `dataset_v2\images\train\pothole_024.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_021.jpg` | `dataset_improvement\source\corrections\pothole_024.jpg` | 0 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\pothole_022.jpg` | `dataset_v2\images\train\pothole_024.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_022.jpg` | `dataset_improvement\source\corrections\pothole_024.jpg` | 0 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\pothole_025.jpg` | `dataset_v2\images\train\pothole_030.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_025.jpg` | `dataset_v2\images\val\pothole_028.jpg` | 2 | Needs review |
| `dataset_v2\images\train\pothole_027.jpg` | `dataset_v2\images\train\pothole_030.jpg` | 2 | Needs review |
| `dataset_v2\images\train\pothole_030.jpg` | `dataset_v2\images\val\pothole_028.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_031.jpg` | `dataset_v2\images\train\pothole_034.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_031.jpg` | `dataset_v2\images\train\pothole_036.jpg` | 2 | Needs review |
| `dataset_v2\images\train\pothole_037.jpg` | `dataset_v2\images\train\pothole_040.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_037.jpg` | `dataset_v2\images\train\pothole_042.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_040.jpg` | `dataset_v2\images\train\pothole_042.jpg` | 0 | Needs review |
| `dataset_v2\images\train\pothole_043.jpg` | `dataset_v2\images\train\pothole_045.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_043.jpg` | `dataset_v2\images\train\pothole_046.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_045.jpg` | `dataset_v2\images\train\pothole_046.jpg` | 2 | Needs review |
| `dataset_v2\images\train\pothole_046.jpg` | `dataset_v2\images\val\pothole_048.jpg` | 2 | Needs review |
| `dataset_v2\images\train\pothole_049.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_051.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_049.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_052.jpg` | 1 | Needs review |
| `dataset_v2\images\train\pothole_049.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_054.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_001.jpg` | `dataset_v2\images\train\water_leakage_003.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_001.jpg` | `dataset_v2\images\train\water_leakage_004.jpg` | 0 | Needs review |
| `dataset_v2\images\train\water_leakage_001.jpg` | `dataset_v2\images\train\water_leakage_006.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_001.jpg` | `dataset_improvement\source\corrections\water_leakage_006.jpg` | 1 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\water_leakage_003.jpg` | `dataset_v2\images\train\water_leakage_004.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_003.jpg` | `dataset_v2\images\train\water_leakage_006.jpg` | 0 | Needs review |
| `dataset_v2\images\train\water_leakage_003.jpg` | `dataset_improvement\source\corrections\water_leakage_006.jpg` | 0 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\water_leakage_004.jpg` | `dataset_v2\images\train\water_leakage_006.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_004.jpg` | `dataset_improvement\source\corrections\water_leakage_006.jpg` | 1 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\water_leakage_012.jpg` | `dataset_v2\images\val\water_leakage_009.jpg` | 2 | Needs review |
| `dataset_v2\images\train\water_leakage_013.jpg` | `dataset_v2\images\train\water_leakage_018.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_013.jpg` | `dataset_v2\images\val\water_leakage_016.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_018.jpg` | `dataset_v2\images\val\water_leakage_016.jpg` | 2 | Needs review |
| `dataset_v2\images\train\water_leakage_019.jpg` | `dataset_v2\images\train\water_leakage_022.jpg` | 2 | Needs review |
| `dataset_v2\images\train\water_leakage_019.jpg` | `dataset_v2\images\train\water_leakage_024.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_025.jpg` | `dataset_v2\images\train\water_leakage_027.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_025.jpg` | `dataset_v2\images\train\water_leakage_028.jpg` | 0 | Needs review |
| `dataset_v2\images\train\water_leakage_025.jpg` | `dataset_v2\images\val\water_leakage_030.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_027.jpg` | `dataset_v2\images\train\water_leakage_028.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_027.jpg` | `dataset_v2\images\val\water_leakage_030.jpg` | 0 | Needs review |
| `dataset_v2\images\train\water_leakage_028.jpg` | `dataset_v2\images\val\water_leakage_030.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_031.jpg` | `dataset_v2\images\train\water_leakage_034.jpg` | 2 | Needs review |
| `dataset_v2\images\train\water_leakage_031.jpg` | `dataset_v2\images\val\water_leakage_036.jpg` | 2 | Needs review |
| `dataset_v2\images\train\water_leakage_034.jpg` | `dataset_v2\images\val\water_leakage_036.jpg` | 2 | Needs review |
| `dataset_v2\images\train\water_leakage_039.jpg` | `dataset_v2\images\val\water_leakage_042.jpg` | 2 | Needs review |
| `dataset_v2\images\train\water_leakage_043.jpg` | `dataset_v2\images\train\water_leakage_048.jpg` | 0 | Needs review |
| `dataset_v2\images\train\water_leakage_043.jpg` | `dataset_v2\images\val\water_leakage_045.jpg` | 0 | Needs review |
| `dataset_v2\images\train\water_leakage_043.jpg` | `dataset_improvement\source\corrections\water_leakage_046.jpg` | 1 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\water_leakage_048.jpg` | `dataset_v2\images\val\water_leakage_045.jpg` | 0 | Needs review |
| `dataset_v2\images\train\water_leakage_048.jpg` | `dataset_improvement\source\corrections\water_leakage_046.jpg` | 1 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\train\water_leakage_049.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_051.jpg` | 1 | Needs review |
| `dataset_v2\images\train\water_leakage_049.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_054.jpg` | 0 | Needs review |
| `dataset_v2\images\val\electricity_019.jpg` | `dataset_improvement\source\corrections\electricity_022.jpg` | 2 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_v2\images\val\electricity_037.jpg` | `dataset_v2\images\val\electricity_040.jpg` | 2 | Needs review |
| `dataset_v2\images\val\water_leakage_045.jpg` | `dataset_improvement\source\corrections\water_leakage_046.jpg` | 1 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_improvement\source\additional_positives\electricity\electricity_051.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_052.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_051.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_054.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_052.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_054.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_055.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_058.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_055.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_060.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_061.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_063.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_061.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_064.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_061.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_066.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_063.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_064.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_063.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_066.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_064.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_066.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\electricity\electricity_067.jpg` | `dataset_improvement\source\additional_positives\electricity\electricity_069.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_051.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_052.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_051.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_054.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_052.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_054.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_055.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_057.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_055.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_058.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_055.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_060.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_057.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_058.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_057.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_060.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_061.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_063.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_061.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_066.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_063.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_064.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_063.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_066.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_067.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_070.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_067.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_072.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_069.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_070.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_079.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_081.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_079.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_082.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_079.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_084.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_081.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_082.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_081.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_084.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_082.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_084.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_085.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_087.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_085.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_088.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_085.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_090.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_087.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_088.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_087.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_090.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_088.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_090.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_091.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_093.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_091.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_096.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_093.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_094.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_093.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_096.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_094.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_096.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_097.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_099.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_097.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_100.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_097.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_102.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_099.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_100.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_099.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_102.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\pothole\pothole_100.jpg` | `dataset_improvement\source\additional_positives\pothole\pothole_102.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_051.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_052.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_051.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_054.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_055.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_057.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_055.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_058.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_055.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_060.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_057.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_058.jpg` | 2 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_057.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_060.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_058.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_060.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_063.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_066.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_067.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_069.jpg` | 0 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_067.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_070.jpg` | 1 | Needs review |
| `dataset_improvement\source\additional_positives\water_leakage\water_leakage_069.jpg` | `dataset_improvement\source\additional_positives\water_leakage\water_leakage_070.jpg` | 1 | Needs review |
| `dataset_improvement\source\corrections\pothole_016.jpg` | `dataset_improvement\source\corrections\pothole_018.jpg` | 2 | Intentionally mapped corrections sequence (under evaluation) |
| `dataset_improvement\source\hard_negatives\pothole\negative_005.jpg` | `dataset_improvement\source\hard_negatives\pothole\negative_009.jpg` | 0 | Needs review |
| `dataset_improvement\source\hard_negatives\pothole\negative_005.jpg` | `dataset_improvement\source\hard_negatives\water_leakage\negative_013.jpg` | 0 | Needs review |
| `dataset_improvement\source\hard_negatives\pothole\negative_005.jpg` | `dataset_improvement\source\hard_negatives\water_leakage\negative_017.jpg` | 0 | Needs review |
| `dataset_improvement\source\hard_negatives\pothole\negative_009.jpg` | `dataset_improvement\source\hard_negatives\water_leakage\negative_013.jpg` | 0 | Needs review |
| `dataset_improvement\source\hard_negatives\pothole\negative_009.jpg` | `dataset_improvement\source\hard_negatives\water_leakage\negative_017.jpg` | 0 | Needs review |
| `dataset_improvement\source\hard_negatives\water_leakage\negative_013.jpg` | `dataset_improvement\source\hard_negatives\water_leakage\negative_017.jpg` | 0 | Needs review |

---
**Duplicate check cycles completed.**
