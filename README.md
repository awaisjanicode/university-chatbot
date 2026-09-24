# University Chatbot

A small Python console chatbot that answers university FAQ questions by matching phrases in a built-in dictionary.

## Run

```bash
python uni.py
```

Ask about admissions, courses, exams, library, hostel, scholarships, or student services. Type `exit` to quit. It uses only the Python standard library and needs no API key.

## How it works

`uni.py` stores question phrases and responses in `faq_data`. The program lowercases each input and returns the first response whose phrase appears in the input. Unknown questions receive a fallback response.

The dates, fees, contact addresses, and university policies in the sample FAQ are illustrative. Verify them with the relevant university before relying on them.
