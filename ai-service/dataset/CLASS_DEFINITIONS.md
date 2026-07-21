# Custom Civic Issue Class Definitions

This document defines the official complaint classes used for custom YOLOv8 model training in the Smart Public Grievance Management System.

## Class Mapping Summary

| Class ID | Class Name | Description |
| :---: | :--- | :--- |
| **0** | Pothole | Visible damage, depression, or hole in a road surface. |
| **1** | Electricity | Visible problems related to electrical infrastructure. |
| **2** | Water Leakage | Visible water leakage from pipes, water supply infrastructure, or other public water systems. |

---

## Detailed Class Definitions & Labeling Guidelines

### **Class ID 0: Pothole**

*   **Definition**: Visible damage, depression, or hole in a road surface.
*   **What should be labeled**: Only the visible pothole or damaged road area.
*   **What should not be labeled**:
    *   Normal road cracks that are not potholes
    *   Normal roads
    *   Vehicles
    *   People
    *   Buildings
*   **Examples**:
    *   Small pothole
    *   Large pothole
    *   Multiple potholes
    *   Road surface depression causing danger to vehicles

---

### **Class ID 1: Electricity**

*   **Definition**: Visible problems related to electrical infrastructure.
*   **What should be labeled**: The visible damaged electrical infrastructure.
*   **What should not be labeled**:
    *   Normal working streetlights
    *   Normal electric poles
    *   People
    *   Vehicles
    *   Buildings
*   **Examples**:
    *   Damaged streetlight
    *   Fallen electric pole
    *   Broken electrical pole
    *   Damaged electrical infrastructure
    *   Exposed or visibly damaged electrical wires

---

### **Class ID 2: Water Leakage**

*   **Definition**: Visible water leakage from pipes, water supply infrastructure, or other public water systems.
*   **What should be labeled**: The visible water leakage area or the damaged infrastructure causing the leakage.
*   **What should not be labeled**:
    *   Normal rivers
    *   Lakes
    *   Rainwater
    *   Normal puddles
    *   Swimming pools
    *   Clean water containers
*   **Examples**:
    *   Water leaking from a broken pipe
    *   Burst water pipeline
    *   Water flowing from damaged public infrastructure
    *   Visible public water leakage
