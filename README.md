# 📝 Named Entity Recognition (NER) Annotation Tool

This project provides an **interactive annotation tool** for labeling entities in text.  
It is built with [Streamlit](https://streamlit.io/) and supports tagging words with categories such as:

- `PERSON`
- `COMPANY`
- `COUNTRY`
- `LOCATION`
- `DEVICE`
- `OTHER`
- `NONE`

The tool loads sentences from a JSON file, displays them in a user-friendly interface, and saves the labeled annotations.

---

## 🚀 Features

- Simple **web interface** for annotation (powered by Streamlit)  
- **Color-coded labels** for easy recognition  
- **Multi-label support**: assign more than one label per word  
- **Progress tracking** with navigation between sentences  
- **Auto-saving** to `labeled_data.json`  
- **Schema validation** with Pydantic models  

---

## 📂 Project Structure

```
.
├── app.py              # Main Streamlit application
├── utils.py            # Helper functions (load/save inputs & outputs)
├── structures.py       # Pydantic models & NER label definitions
├── inputs.json         # Input dataset with sentences
├── labeled_data.json   # Saved annotations (output)
├── requirements.txt    # Python dependencies
└── logo.jpg            # Logo displayed in the app (optional)
```

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # macOS/Linux
   .venv\Scripts\activate        # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the provided URL (default: `http://localhost:8501`) in your browser.

---

## 📊 Input & Output

- **Input (`inputs.json`)** – list of sentences to annotate:
  ```json
  [
    {
      "ID": "138d2c86-2e92-443e-9e04-d1446e26f9a5",
      "text": "Samsung released a new Galaxy phone in South Korea."
    }
  ]
  ```

- **Output (`labeled_data.json`)** – annotations saved automatically:
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
