import os
import sys
import hashlib
import cv2

WORKSPACE_DIR = r"c:\Users\Shreyas\OneDrive\Desktop\Main\ai-service"
V2_DIR = os.path.join(WORKSPACE_DIR, "dataset_v2")
IMPROV_DIR = os.path.join(WORKSPACE_DIR, "dataset_improvement")
REPORT_PATH = os.path.join(IMPROV_DIR, "reports", "DUPLICATE_ANALYSIS_REPORT.md")

def get_sha256(filepath):
    sha = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                sha.update(chunk)
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None
    return sha.hexdigest()

def get_dhash(image_path, hash_size=8):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return None
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (hash_size + 1, hash_size))
        diff = resized[:, 1:] > resized[:, :-1]
        return diff.flatten()
    except Exception:
        return None

def hamming_distance(h1, h2):
    return sum(a != b for a, b in zip(h1, h2))

def scan_images(root_dir):
    image_list = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                full_path = os.path.join(root, f)
                image_list.append(full_path)
    return image_list

def main():
    print("==================================================")
    print("STARTING DUPLICATE AND SIMILARITY PROTECTION SCAN")
    print("==================================================")
    
    # Locate all images
    v2_images = scan_images(V2_DIR)
    improv_images = scan_images(IMPROV_DIR)
    
    all_images = v2_images + improv_images
    print(f"Found {len(v2_images)} images under dataset_v2/")
    print(f"Found {len(improv_images)} images under dataset_improvement/")
    
    # Calculate hashes
    sha_records = {} # hash -> list of absolute paths
    dhash_records = {} # path -> dhash array
    
    for path in all_images:
        # SHA-256
        sha = get_sha256(path)
        if sha:
            sha_records.setdefault(sha, []).append(path)
            
        # Perceptual hash (dHash)
        dh = get_dhash(path)
        if dh is not None:
            dhash_records[path] = dh
            
    # Find exact duplicate matches
    exact_duplicates = []
    for sha, paths in sha_records.items():
        if len(paths) > 1:
            exact_duplicates.append(paths)
            
    # Find near duplicates (perceptual hashing similarity threshold <= 2 bits mismatch)
    near_duplicates = []
    checked_pairs = set()
    
    image_paths = list(dhash_records.keys())
    for i in range(len(image_paths)):
        for j in range(i + 1, len(image_paths)):
            path1 = image_paths[i]
            path2 = image_paths[j]
            
            # Avoid comparing files in the same SHA duplicate list
            sha1 = get_sha256(path1)
            sha2 = get_sha256(path2)
            if sha1 == sha2:
                continue
                
            dist = hamming_distance(dhash_records[path1], dhash_records[path2])
            if dist <= 2: # Very low hamming distance -> near duplicates
                # Use relative filenames for clean report display
                rel1 = os.path.relpath(path1, WORKSPACE_DIR)
                rel2 = os.path.relpath(path2, WORKSPACE_DIR)
                pair = tuple(sorted([rel1, rel2]))
                if pair not in checked_pairs:
                    checked_pairs.add(pair)
                    near_duplicates.append((rel1, rel2, dist))
                    
    # Generate DUPLICATE_ANALYSIS_REPORT.md
    report_md = f"""# Duplicate Analysis Report

This status report logs SHA-256 exact binary hashes and Perceptual dHash verification comparisons across `dataset_v2` and `dataset_improvement` splits.

---

## 1. Exact SHA-256 Binary Duplicates
*   **Total Exact Duplicate Clusters Staged:** {len(exact_duplicates)}

"""
    if exact_duplicates:
        for idx, cluster in enumerate(exact_duplicates):
            report_md += f"### Cluster {idx + 1}\n"
            for item in cluster:
                report_md += f"*   `{os.path.relpath(item, WORKSPACE_DIR)}`\n"
            report_md += "\n"
    else:
        report_md += "_No exact binary duplicates detected between the active improvement partitions and dataset_v2._\n\n"
        
    report_md += f"""---

## 2. Perceptual Similarity Near-Duplicates (Mismatch bits <= 2)
*   **Total Near-Duplicate Pairs Detected:** {len(near_duplicates)}

"""
    if near_duplicates:
        report_md += "| File 1 | File 2 | Distance (Bits Diff) | Evaluation Status |\n"
        report_md += "| :--- | :--- | :---: | :--- |\n"
        for rel1, rel2, dist in near_duplicates:
            # Check if this is the known border frame correction sequence
            status_desc = "Intentionally mapped corrections sequence (under evaluation)" if "corrections" in rel1 or "corrections" in rel2 else "Needs review"
            report_md += f"| `{rel1}` | `{rel2}` | {dist} | {status_desc} |\n"
    else:
        report_md += "_No near-duplicates detected across dataset subsets._\n"
        
    report_md += "\n---\n**Duplicate check cycles completed.**\n"
    
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report_md)
        
    print(f"[x] Successfully created DUPLICATE_ANALYSIS_REPORT.md at {REPORT_PATH}")
    print(f"Exact duplicates found: {len(exact_duplicates)}")
    print(f"Near duplicates found: {len(near_duplicates)}")
    sys.exit(0)

if __name__ == "__main__":
    main()
