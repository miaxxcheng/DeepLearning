# ChatEats App

## Introduction
------------
ChatEats is a Python application that allows you to chat with a chatbot that processes yelp reviews from json files. You can ask questions about restaurant reviews and get tailored recommendations without having to scroll and parse through all the reviews manually. We specifically used a subset of a [yelp dataset](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset) from Kaggle as the custom dataset for the model. We fine-tuned the gpt-3.5-turbo model with 100+ question-answer pairs to tailor the chatbot to our specific use case. The base of the app comes from the [ask-multiple-pdfs repository](https://github.com/alejandro-ao/ask-multiple-pdfs).

## Dependencies and Installation
----------------------------
To install the ChatEats App, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

## Usage
-----
To use the ChatEats App, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple PDF documents into the app by following the provided instructions.

5. Ask questions in natural language about the loaded PDFs using the chat interface.