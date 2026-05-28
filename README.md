# DecodeLabs AI Internship - Core Projects Milestone

This repository contains the official implementation of the three fundamental Artificial Intelligence projects completed during my industrial training at **DecodeLabs**. Each project demonstrates a core branch of AI development, ranging from deterministic rule-based systems to supervised machine learning and content-based filtering.

---

## 📂 Projects Overview

### 🤖 Project 1: Rule-Based AI Chatbot
* **Goal:** Create a continuous interaction loop that simulates human-to-machine dialogue using rigid control flow.
* **Key Implementations:**
  * Created a continuous `while True` logic loop.
  * Applied **Data Sanitization and Normalization** via text case flattening (`.lower()`) and whitespace stripping (`.strip()`) to process raw input without errors.
  * Implemented explicit `if-else` guard conditions to map deterministic responses for greetings, project queries, company info, and exit requests.

### 📊 Project 2: Data Classification Using AI
* **Goal:** Build a supervised learning classification pipeline to recognize mathematical patterns and categorize features.
* **Key Implementations:**
  * Structured an intrinsic dataset modeled after the famous **Iris Flower Dataset**.
  * Handcrafted a custom **Feature Scaling (StandardScaler)** algorithm to compute data mean and variance, balancing the matrix boundaries between `-2` and `+2`.
  * Built a **K-Nearest Neighbors (KNN)** logic algorithm using pure Euclidean Distance vector calculations.
  * Generated evaluation metrics including a **Confusion Matrix** and a **Classification Report** yielding a precise Macro F1-Score.

### 🎯 Project 3: AI Recommendation Logic
* **Goal:** Design a digital recommendation engine that maps explicit user interests to item profiles with absolute precision.
* **Key Implementations:**
  * Defined a structured relational item database containing course modules and descriptive tags.
  * Implemented **Pattern Alignment** by capturing user interest tags via input vectors.
  * Developed a text similarity engine that scores recommendations using a **Binary Overlap Counter** (Intersection Logic).
  * Programmed a **Top-N Tailored List Generator** that dynamically ranks and sorts the most relevant recommendations for the end-user.

---

## 💻 Tech Stack & Skills Demonstrated
* **Languages:** Pure Python 3
* **Concepts:** Control Flow, Data Normalization, Supervised Machine Learning, Feature Scaling, KNN Classifier, Content-Based Recommendation Systems, Pattern Matching.
* **Tools:** Git, GitHub, VS Code.

---
*Developed with absolute clarity and precision as part of the DecodeLabs AI Engineering Track.*
