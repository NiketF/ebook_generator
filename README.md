

# Professional E-Book Generator

## **Project Overview**

The **Professional E-Book Generator** is a specialized AI-powered tool designed for recruitment agencies and HR professionals. It automates the creation of comprehensive, 10–15 page equivalent career guides for specific job roles or professional communities. By leveraging advanced generative AI, it produces publication-ready HTML5 documents featuring industry insights, skill matrices, and multi-year roadmaps.

## **Why I Chose This Idea**

This project addresses a real-world bottleneck in the recruitment and educational sectors:

* **Scalability:** Manually researching and writing industry whitepapers is time-consuming. This tool reduces the process from days to seconds.


* **Standardization:** It ensures consistent quality and structure across different job roles, providing a professional "look and feel" through embedded CSS.
* **Utility:** It serves as a high-value lead magnet for agencies or a training resource for new hires.

## **Core Technology**

* 
**Hugging Face / Generative AI:** This project utilizes the **Google Gemini API** (via the `google-generativeai` library) to handle complex, long-form content generation.


* 
**Streamlit:** Used for the frontend to create a responsive, user-friendly interface.


* **HTML5/CSS3:** The model is prompted to output structured code rather than plain text, allowing for instant preview and professional formatting within the app.

## **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone <your-repository-link>
cd ebook_generator-main

```

### **2. Install Dependencies**

Ensure you have Python 3.11+ installed. Install the required libraries using the provided `requirements.txt`:

```bash
pip install -r requirements.txt

```

### **3. Configure API Keys**

This application requires a Gemini API Key.

* **Local Development:** Create a `.streamlit/secrets.toml` file and add:
```toml
GEMINI_API_KEY = "your_api_key_here"

```


* **Streamlit Cloud:** Add `GEMINI_API_KEY` to the app's "Secrets" settings.

## **How to Run the Project**

Launch the application using Streamlit:

```bash
streamlit run app.py

```

Once running, navigate to `http://localhost:8501` in your browser.

## **Example Input/Output**

* **Input:** "Data Scientists"
* 
**Process:** The AI analyzes industry trends, salary ranges, and learning curves.


* 
**Output:** A downloadable `.html` file containing 16 structured sections, including a hyperlinked Table of Contents and an Industry Evaluation.



## **Assumptions & Limitations**

* **API Limits:** The quality and speed of generation depend on the Gemini model quota.
* **Formatting:** While the model is instructed to provide valid HTML, occasionally complex CSS may require manual adjustment for specific PDF converters.
* **Future Improvements:**
* Add PDF export functionality using libraries like `pdfkit`.
* Implement image generation for e-book covers.
* Support for multiple languages.



---

### **Project Structure**

```text
├── .devcontainer/     # Configuration for cloud development
├── app.py             # Main application logic and UI
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation

```
