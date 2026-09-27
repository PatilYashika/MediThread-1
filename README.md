# MediThread — AI-Enabled Health Memory Timeline Platform

**MediThread** is a production-ready, clinical-grade web platform designed to solve medical record fragmentation. It enables multi-generational households and individual patients to own, structure, and visualize their lifelong health memory with real-time AI assistance, while empowering physicians with high-impact clinical digests.

---

## 🌟 Key Features & Clinical Capabilities

### 1. Multi-Generational Household Dashboard
- Manage up to 5–6 profiles per account (Self, Spouse, Children, Aging Parents).
- **Persistent Emergency Anchor Banner**: Instant visibility of Blood Group, Severe Drug Allergies (e.g., Anaphylactic Penicillin, Peanuts), Emergency Caregiver Contacts, and DNR/Organ Donor directives.
- Real-time profile switching with dedicated health memory histories.

### 2. Chronological Health Memory Timeline
- Vertical interactive chronological spine with high-contrast, category-specific markers:
  - 🔴 **Diagnoses & Clinical Encounters**
  - 🔵 **Lab Reports & Metabolic Panels** (with biomarker trend indicators)
  - 🟢 **Medication Regimens** (with dosage schedules & active statuses)
  - 🟣 **Surgical Procedures & Immunization Boosters**
- Multi-dimensional filtering by Category, Severity, and Free-text Keyword Search.
- Source Document OCR text inspector for full provenance tracking.

### 3. AI Document Ingestion & Structuring Studio
- Drag-and-drop or camera scan simulated intake for JPG, PNG, and PDF medical records.
- Real-time 4-stage processing visualizer:
  `[Uploading & Sanitization]` ➔ `[OCR Layout Decomposition]` ➔ `[AI Biomarker Isolation]` ➔ `[Timeline Link]`
- Automatic biomarker parameter extraction (HbA1c, Fasting Glucose, eGFR, Creatinine, LDL/HDL) with reference interval auditing.

### 4. Personal Google Drive Cloud Storage & Medical Vault
- **100% Patient Privacy**: Files are saved directly to each user's personal Google Drive account in a dedicated `MediThread Medical Vault` folder.
- **Direct Drive File Links**: Each timeline event card includes a direct `Drive Vault ↗` badge to open the original file directly on Google Drive.
- **Import from Google Drive**: Browse and import medical documents stored in Google Drive directly into the AI parsing pipeline.
- **1-Click Full Health Memory Backup**: Export and backup all timeline events, clinical records, doctor profile details, and attachments into a timestamped Google Drive cloud backup package (`MediThread_Health_Memory_Backup_*.json`).

### 5. Multi-Context AI Clinical Summary Engine
- **1-Minute Emergency Brief**: Rapid triage overview for paramedics and ER personnel.
- **5-Minute Doctor Consultation Summary**: SOAP-aligned longitudinal synthesis with biomarker trend deltas and differential prompts.
- **Travel Health Passport**: Multilingual medical warning flags (English, Spanish, French) and cryptographically verified immunization proofs.

### 6. Preventive Health Gap Detection Engine
- Clinical guideline scanner based on ADA, USPSTF, CDC, and AAP recommendations.
- Automated alerts for overdue glycemic tests, renal microalbuminuria, lipid panels, and senior/pediatric vaccines.

### 7. Doctor Specialist Portal & Time-Limited Sharing
- Generate encrypted, 24-hour / 7-day access links with custom PIN codes and high-contrast SVG QR codes.
- Specialist review cockpit with parameter correlation graphs, medication interaction audits, and physician clinical notes authoring.

---

## ☁️ Google Drive Integration Setup (Personal Drive)

To enable live saving to your own personal Google Drive, follow these 1-minute steps to get a free **Google Cloud OAuth Client ID**:

1. **Create a Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/) and create a new project (e.g., `MediThread-Vault`).

2. **Enable the Google Drive API**:
   - In the search bar, search for **Google Drive API** and click **Enable**.

3. **Configure OAuth Consent Screen**:
   - Go to **APIs & Services > OAuth consent screen**.
   - Select **External** and enter an App name (e.g., `MediThread`) and your email.

4. **Create OAuth 2.0 Client ID**:
   - Go to **APIs & Services > Credentials > Create Credentials > OAuth client ID**.
   - Select **Application type**: `Web application`.
   - Under **Authorized JavaScript origins**, add:
     - `http://localhost:3000`
     - `http://127.0.0.1:3000`
   - Click **Create** and copy your **Client ID**.

5. **Connect in MediThread**:
   - Open MediThread (`http://localhost:3000`), click the **`Drive Vault`** button in the top navigation bar, paste your Client ID, and click **`Sign in with Google & Authorize Drive`**!

> **Note on Security & Scopes:** MediThread uses Google's `drive.file` scope (`https://www.googleapis.com/auth/drive.file`), which **strictly limits access ONLY to files and folders created by MediThread**. It never accesses other unrelated files in your Google Drive.

---

## 🏗️ Tech Stack & Directory Map

```
DE webapp/
├── index.html                 # Single Page Application entry point & CSS/Lucide/GSI scripts
├── server.py                   # Local development server with CORS & proper MIME handling
├── README.md                   # Project documentation & setup instructions
├── css/
│   ├── main.css                # Custom clinical theme styling & glow animations
│   └── timeline.css            # Chronological vertical timeline spine styling
├── js/
│   ├── app.js                  # Main controller, UI rendering & view orchestrator
│   ├── googleDriveService.js   # Google Drive v3 REST API & GIS OAuth Token Client
│   ├── state.js                # Reactive state store with LocalStorage persistence
│   ├── ocrPipeline.js          # AI OCR & clinical parameter extraction engine
│   ├── sampleDocs.js           # Preloaded clinical lab reports & discharge summaries
│   ├── mockData.js             # Initial household & biomarker longitudinal datasets
│   ├── charts.js               # Canvas biomarker longitudinal trend graphs
│   ├── summaryEngine.js        # Multi-context AI clinical summary generators
│   ├── preventiveEngine.js     # ADA / USPSTF preventive gap analyzer
│   └── doctorPortal.js         # Doctor specialist review cockpit & secure link sharing
└── db/
    └── schema.sql              # Production PostgreSQL schema with RLS security policies
```

---

## 🚀 Quick Start Guide

### Running Locally

To launch the application locally on your machine:

```powershell
# In PowerShell or Command Prompt:
python server.py
# Or using standard python:
python -m http.server 3000
```

Then open your browser and navigate to:
👉 **`http://localhost:3000`**

### Direct Browser Access
You can also directly double-click [`index.html`](file:///c:/Users/yashika/OneDrive/Desktop/DE%20webapp/index.html) to open it in Google Chrome, Microsoft Edge, or Firefox!
