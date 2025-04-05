
# 🚀 C&D Assist - AI-Powered Bug Detection & Fixing

C&D Assist (Code and Debug AI Assistent) is a AI tool that performs **automated bug detection and fixing**. Designed with a focus on **real-time assistance**, it integrates a **custom-built web-based IDE** to provide a seamless debugging experience for developers.

---

## ✅ Current Implementation

### 🔧 What It Does
- Takes **raw code** as input through a browser-based IDE interface.
- Automatically detects bugs and suggests **corrected code**.
- Allows users to view **error outputs**, compare **fixed code**, and make corrections directly inside the IDE.
- Supports **uploading Python files**, **language selection**, and **custom prompts** to control bug-fixing behavior.

### ⚙️ Key Components
- **Frontend**:  
  - Built using HTML, CSS, JavaScript, and PHP.  
  - Integrated with **ACE Code Editor** for a professional IDE feel.  
  - Real-time user interface for input, output, and error visualization.

- **Backend**:  
  - Written in Python.  
  - Interacts with **transformer-based code models** for bug fixing.  
  - Receives code input from frontend and returns fixed code or errors.

### 🤖 Final Model Used
- **Model**: `stabilityai/stablecode-completion-alpha-3b-4k`  
- **Reason for selection**:  
  - Balanced **performance** and **resource efficiency**.  
  - Produced the **most accurate and usable outputs** within hardware limits.  
- **Minimum System Specs**:
  - Intel i5 11th Gen  
  - RTX 2050 (4GB VRAM)  
  - 16GB RAM  

---

## 🕰️ What We Originally Planned

### 🧠 Initial Approach
- Used the **Defectors Dataset** (~150k Python samples).
- Built a classification model using:
  - `RandomForestClassifier`
  - `XGBoost`
  - Achieved ~70% accuracy on detecting buggy vs clean code.

### 🔨 Bug Fixing Plan
- Fixing bugs using **DeepSeek-Coder 6.7B**.
- Integrated **static analysis tools** like `PyFlakes` and `AutoPEP8` for basic checks.

### ❌ Why It Didn't Work
- **DeepSeek 6.7B** was **too large** to run on our system.
- **PyFlakes/AutoPEP8** lacked depth in identifying logical or structural issues.
- Model-based fixing was necessary — so we **pivoted.**

---

## 🔄 Second Attempt: New Datasets, New Models

### 📚 Datasets Used
- **CodeXGLUE (Python subset)**
- **many-types-4-py-dataset**
- **QuixBugs**

### ❌ What Went Wrong
- After **data cleaning and filtering**, dataset was **too small** for model training.
- Tried to **combine datasets**, but still:
  - Poor generalization
  - Inconsistent labeling
  - Model **couldn’t classify buggy code reliably**

---

## 🧪 Final Attempts Before Deadline

### 🧠 Tried Generative Models
- `deepseek/deepseek-coder-1.3b-instruct` → Poor quality responses
- `deepseek/deepseek-coder-1.3b-base` → Also inconsistent output
- ✅ **Final choice**: `stabilityai/stablecode-completion-alpha-3b-4k`
  - Best compromise between output quality and hardware efficiency.

---

## 🌟 If We Had More Time...

If time and resources permitted, we would have:
- **Fine-tuned smaller generative models** on domain-specific Python bug datasets.
- Built a **multi-stage pipeline**:
  1. Detect
  2. Localize
  3. Fix
- Improved dataset size using **data augmentation** (mutating clean code with known bug patterns).
- Created a **feedback loop** from user corrections to continuously fine-tune the model.
- Built **plugins for VS Code or Jupyter Notebooks** for smoother developer experience.

---

## 📁 Project Structure

```
C_D_Assit/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── bugfix_model/
│       └── fix_code.py

├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js

├── src/
│   ├── api_server.py
│   └── bug_fixer.py

├── models/
│   ├── models--stabilityai--stablecode-completion-alpha-3b-4k/
│   └── stored_tokens/
```

---

## 🧑‍💻 Run Locally

1. Clone the repo  
   ```bash
   git clone https://github.com/Yuvanraj-K-S/C_D_Assit.git
   cd C_D_Assit
   ```

2. Set up Python environment  
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Load Model
   ```bash
   python src/bug_fixer.py
   ```
3. Launch backend API  
   ```bash
   python src/api_server.py
   ```

4. Run Frontend
   ```bash
   Frontend/ui/index.html
   ```

---
