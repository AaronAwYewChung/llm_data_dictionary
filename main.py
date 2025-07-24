import os
import google.generativeai as genai
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_supabase_client():
    """Initializes and returns the Supabase client."""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    return create_client(url, key)


def fetch_data_dictionary(client: Client) -> str:
    """Fetches the data dictionary from Supabase and formats it as a string."""
    # Order by table_name to group related columns together in the context
    response = client.table("data_dictionary").select("*").order("table_name").execute()
    if not response.data:
        return "No data dictionary found."

    # Format the data into a string for the prompt
    dict_str = ""
    current_table = ""
    for row in response.data:
        table = row.get("table_name")
        if table != current_table:
            dict_str += f"\n--- Table: {table} ---\n"
            current_table = table

        dict_str += f"- Column: {row.get('column_name')}\n"
        dict_str += f"  Definition: {row.get('definition')}\n"
        dict_str += f"  Data Type: {row.get('data_type')}\n"
        dict_str += f"  Example: {row.get('example_value')}\n\n"
    return dict_str


def ask_ai(question: str, context: str) -> str:
    """Constructs the prompt and gets an answer from the Gemini AI."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # --- EDIT THIS PROMPT TEMPLATE FOR CUSTOMIZATION ---
    # You can change the instructions, add more context, or modify the structure
    # to guide the AI's responses.
    prompt_template = f"""
    You are an expert assistant for our internal data dictionary.
    Your task is to answer questions based ONLY on the context provided below.
    If the answer is not found in the context, say "I cannot answer this question based on the available data dictionary."

    --- CONTEXT: DATA DICTIONARY ---
    {context}
    --- END OF CONTEXT ---

    USER'S QUESTION:
    {question}

    ANSWER:
    """

    response = model.generate_content(prompt_template)
    return response.text


def main():
    """Main function to run the application."""
    try:
        supabase_client = get_supabase_client()
        data_context = fetch_data_dictionary(supabase_client)

        if "No data" in data_context:
            print(data_context)
            return

        # Check if the script is running in an interactive terminal
        if not os.isatty(0):
            print("This script is intended to be run interactively.")
            print("Please run it from your terminal:")
            print("python main.py")
            return

        print("Welcome to the Data Dictionary AI Assistant.")
        print("Ask a question about the data dictionary (or type 'exit' to quit).")

        while True:
            user_question = input("> ")
            if user_question.lower() == "exit":
                break

            answer = ask_ai(user_question, data_context)
            print(f"\nAI Assistant:\n{answer}\n")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
