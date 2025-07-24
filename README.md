# Data Dictionary AI Assistant

This project provides an interactive command-line interface (CLI) AI assistant that answers questions based on a data dictionary stored in Supabase. It leverages the Gemini AI model to provide intelligent responses.

## Features

- Fetches data dictionary information from a Supabase database.
- Uses the Gemini AI model to answer user questions based _only_ on the provided data dictionary context.
- Interactive CLI for real-time questions and answers.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- `pip` (Python package installer)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/AaronAwYewChung/llm_data_dictionary
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    - **On macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```
    - **On Windows:**
      ```bash
      .\venv\Scripts\activate
      ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

This application requires API keys and Supabase credentials, which should be stored in a `.env` file in the root directory of the project.

1.  **Create a `.env` file:**
    In the root directory of your project, create a file named `.env`.

2.  **Add the following environment variables to your `.env` file:**

    ```
    SUPABASE_URL="YOUR_SUPABASE_URL"
    SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

    - Replace `"YOUR_SUPABASE_URL"` with your Supabase project URL.
    - Replace `"YOUR_SUPABASE_ANON_KEY"` with your Supabase `anon` public key.
    - Replace `"YOUR_GEMINI_API_KEY"` with your Google Gemini API key. You can obtain one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

## Usage

1.  **Ensure your virtual environment is activated.** (See Installation steps 3)

2.  **Run the application:**

    ```bash
    python main.py
    ```

3.  **Interact with the AI Assistant:**
    Once the application starts, you will see a prompt:
    ```
    Welcome to the Data Dictionary AI Assistant.
    Ask a question about the data dictionary (or type 'exit' to quit).
    >
    ```
    Type your questions about your data dictionary and press Enter. To exit the assistant, type `exit` and press Enter.

## Customization

The AI's prompt template can be customized within the `main.py` file. Look for the `prompt_template` variable in the `ask_ai` function to modify the instructions given to the Gemini model. This allows you to fine-tune the AI's behavior and responses.
