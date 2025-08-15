# Project A.L.B.U.M.
**Automated Local Bundling Of User Memories**  

My attempt at a fully **offline**, **cross-platform** desktop application that scans your local drives and organizes your photo collection intelligently. 

### Inspiration

- Google Photos has most of the features I am going to propose but with a caveat that those photos need to be uploaded to Google servers and thats requires a Google One subscription.
- Data backup options like Google One, iCloud, etc came in the last few years and people still have a lot of images backed up on their offline storages. This option would enable the organisation of those backups. No cloud uploads, no subscriptions, full privacy.

### Core Features (MVP)

- **Sort By:**
  - People
  - Places
  - Time
  - Important Docs
  - Receipts
  - Memes & Screenshots detection

- **Search:**
  - Natural queries like `"Mudit in Dublin on Christmas"`
  
- **Heatmap Views:**
  - Location clustering on a map
  - Calendar heatmap for time-based grouping

---

## Core Responsibilities

### Backend
1. Recursively scan selected folders (`.jpg`, `.jpeg`, `.png` initially)
2. Extract metadata
3. Perform:
   - Face detection + clustering
   - Place grouping
   - Time grouping
   - Image type detection (meme, screenshot)
   - OCR for important docs
4. Store all results in database
5. Serve organized data via REST API

### Frontend
- Display images in tabs:
  - By Time  
  - By People  
  - By Location  
  - Important Docs  
  - Others (Memes, Screenshots, etc.)  
- Search bar with natural query parsing  
- Map & calendar heatmap views  
- Cluster labeling UI

---

## End goal 

Ship as a single executable (`.exe`, `.dmg`, `.AppImage`) for one-time installation.

---

## Data Flow
1. **User selects folder(s)** => app scans them for images
2. **Backend extracts metadata** => saves in database
3. **AI modules analyze images** => generate tags & clusters
4. **Frontend displays organized results** via API
5. Package both frontend and backend into a single offline desktop app using something like **Electron**

---

## Project Goals
- 100% offline privacy-focused photo organization
- Cross-platform support (Windows, Mac, Linux)
- AI-powered local image classification
- Single-click install & simple setup

---

## Future Features
- Support more formats
- Advanced search queries (“person + place + time”)
- Video support (keyframe face detection)
- Duplicate detection & cleanup
- Pet detection (treated as “people”)
- Blur detection & cleanup
- Mass rename/delete/export clusters
- Model/data encryption
- Login to save/import custom-trained models

---

**NOTE**: I authored this README.md with the help of Generative AI. I did not generate this but wrote this with the assistance of ChatGPT to consolidate my thoughts and ideas about the project.