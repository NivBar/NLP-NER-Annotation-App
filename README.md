# Named Entity Recognition (NER) Annotation Tool

An interactive annotation tool for **Named Entity Recognition (NER)** tasks, built with [Streamlit](https://streamlit.io/).  
This project allows annotators to efficiently label words in sentences with entity categories such as `PERSON`, `COMPANY`, `COUNTRY`, `LOCATION`, `DEVICE`, and more.  
The labeled data is stored in a structured JSON format, ready for downstream machine learning tasks.

---

## Key Features

- User-friendly interface with color-coded entity labels  
- Support for multiple labels per word  
- Automatic saving of annotations to `labeled_data.json`  
- Progress tracking (streak counter, sentence navigation)  
- Schema validation with [Pydantic](https://docs.pydantic.dev/) models  
- Optional logo display for branding  

---

## Repository Structure

```
.
├── app.py              # Main Streamlit application
├── utils.py            # Utility functions (data loading & saving)
├── structures.py       # Data models & label definitions (Pydantic + Enum)
├── inputs.json         # Input dataset (sentences for annotation)
├── labeled_data.json   # Output dataset (annotations, generated automatically)
├── requirements.txt    # Python dependencies
└── logo.jpg            # Logo displayed in the UI (optional)
```

---

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Launch the annotation tool with:

```bash
streamlit run app.py
```

By default, the app will be available at [http://localhost:8501](http://localhost:8501).

---

## Input & Output Formats

### Input (`inputs.json`)
A list of sentences to annotate:
```json
[
  {
    "ID": "138d2c86-2e92-443e-9e04-d1446e26f9a5",
    "text": "Samsung released a new Galaxy phone in South Korea."
  }
]
```

### Output (`labeled_data.json`)
A list of annotated sentences with word-level labels:
```json
[
  {
    "ID": "138d2c86-2e92-443e-9e04-d1446e26f9a5",
    "labeled_data": [
      {
        "word": "Samsung",
        "labels": ["COMPANY"],
        "position": 0,
        "sentence_id": "138d2c86-2e92-443e-9e04-d1446e26f9a5"
      }
    ]
  }
]
```

---

## Technologies Used

- [Streamlit](https://streamlit.io/) – interactive web app framework  
- [Pydantic](https://docs.pydantic.dev/) – data validation and management  
- [Pillow](https://python-pillow.org/) – image handling (for logo support)  
