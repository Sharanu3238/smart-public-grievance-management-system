import os
import sys

WORKSPACE_DIR = r"c:\Users\Shreyas\OneDrive\Desktop\Main\ai-service"
IMPROV_DIR = os.path.join(WORKSPACE_DIR, "dataset_improvement")
REPORT_PATH = os.path.join(IMPROV_DIR, "reports", "ANNOTATION_QUALITY_REPORT.md")

subfolders = [
    ("corrections", False),
    ("hard_negatives/pothole", True),
    ("hard_negatives/water_leakage", True),
    ("hard_negatives/electricity", True),
    ("additional_positives/pothole", False),
    ("additional_positives/water_leakage", False),
    ("additional_positives/electricity", False)
]

def main():
    print("==================================================")
    print("STARTING ANNOTATION QUALITY VALIDATION ACTION")
    print("==================================================")
    
    total_issues = 0
    issues_list = []
    
    scanned_images = 0
    scanned_labels = 0
    
    for relative_sub, is_hard_neg in subfolders:
        dir_path = os.path.join(IMPROV_DIR, "source", relative_sub)
        if not os.path.exists(dir_path):
            continue
            
        all_files = os.listdir(dir_path)
        images = sorted([f for f in all_files if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        labels = sorted([f for f in all_files if f.lower().endswith('.txt')])
        
        # Check missing status
        for img in images:
            scanned_images += 1
            base, _ = os.path.splitext(img)
            lbl = base + ".txt"
            if lbl not in labels:
                total_issues += 1
                issues_list.append((os.path.join(relative_sub, img), "Missing Label file", "Image exists without matching annotation `.txt`"))
                
        # Check orphan status
        for lbl in labels:
            scanned_labels += 1
            base, _ = os.path.splitext(lbl)
            # Find matching image
            matched_img = None
            for ext in ['.jpg', '.jpeg', '.png']:
                if base + ext in images:
                    matched_img = base + ext
                    break
            if not matched_img:
                total_issues += 1
                issues_list.append((os.path.join(relative_sub, lbl), "Orphan Label file", "Annotation `.txt` exists without matching image file"))
                continue
                
            # Read label values
            lbl_full_path = os.path.join(dir_path, lbl)
            try:
                with open(lbl_full_path, 'r', encoding='utf-8') as lf:
                    lines = lf.readlines()
            except Exception as e:
                total_issues += 1
                issues_list.append((os.path.join(relative_sub, lbl), "Corrupted file", f"Could not read annotation file: {e}"))
                continue
                
            # Verify empty rules for hard negatives
            if is_hard_neg and len(lines) > 0 and any(line.strip() for line in lines):
                total_issues += 1
                issues_list.append((os.path.join(relative_sub, lbl), "Invalid Hard Negative", "Label file is not empty for a designated hard negative sample"))
                
            # Verify coordinates and class ids
            for line_idx, line in enumerate(lines):
                line_str = line.strip()
                if not line_str:
                    continue
                parts = line_str.split()
                if len(parts) != 5:
                    total_issues += 1
                    issues_list.append((os.path.join(relative_sub, lbl), f"Format error (Line {line_idx+1})", f"YOLO annotation line must have exactly 5 values, found {len(parts)}"))
                    continue
                    
                # Class mapping check
                try:
                    cid = int(parts[0])
                    xc = float(parts[1])
                    yc = float(parts[2])
                    w = float(parts[3])
                    h = float(parts[4])
                except ValueError:
                    total_issues += 1
                    issues_list.append((os.path.join(relative_sub, lbl), f"Value error (Line {line_idx+1})", "Annotation values must be numeric"))
                    continue
                    
                if cid not in [0, 1, 2]:
                    total_issues += 1
                    issues_list.append((os.path.join(relative_sub, lbl), f"Invalid Class ID (Line {line_idx+1})", f"Class ID must be 0 (Pothole), 1 (Electricity), or 2 (Water Leakage), found {cid}"))
                    
                # Box check
                if w <= 0 or h <= 0:
                    total_issues += 1
                    issues_list.append((os.path.join(relative_sub, lbl), f"Zero-Area box (Line {line_idx+1})", f"Width ({w}) and height ({h}) must be positive"))
                    
                if not (0.0 <= xc <= 1.0) or not (0.0 <= yc <= 1.0) or not (0.0 <= w <= 1.0) or not (0.0 <= h <= 1.0):
                    total_issues += 1
                    issues_list.append((os.path.join(relative_sub, lbl), f"Out of Bounds box (Line {line_idx+1})", f"Coordinates must be normalized between 0.0 and 1.0 (got x={xc}, y={yc}, w={w}, h={h})"))
                    
    # Generate ANNOTATION_QUALITY_REPORT.md
    report_md = f"""# Annotation Quality Report

This report presents format validation, coordinator checking, orphan log tracking, and class limit checks across the improvement split.

---

## 1. Quality Validation Statistics
*   **Total Images Scanned:** {scanned_images}
*   **Total Label Files Scanned:** {scanned_labels}
*   **Total Issues Identified:** {total_issues}

---

## 2. Identified Annotation Issues Log
"""
    if issues_list:
        report_md += "| Partition File | Error Category | Error Details |\n"
        report_md += "| :--- | :--- | :--- |\n"
        for filepath, category, details in issues_list:
            report_md += f"| `{filepath}` | {category} | {details} |\n"
    else:
        report_md += "_No formatting, missing files, or coordinating border issues were found in the workspace._\n"
        
    report_md += "\n---%d-class mapping conforms: 0: Pothole, 1: Electricity, 2: Water Leakage.\n"
    
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report_md)
        
    print(f"[x] Successfully created ANNOTATION_QUALITY_REPORT.md at {REPORT_PATH}")
    print(f"Total issues found: {total_issues}")
    sys.exit(0)

if __name__ == "__main__":
    main()
