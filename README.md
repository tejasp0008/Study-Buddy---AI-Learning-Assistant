# Study Buddy - AI Learning Assistant

Study Buddy is a real-time chatbot designed to help students learn and understand complex topics more effectively. By leveraging the power of AI, Study Buddy provides custom explanations, generates quiz questions, and remembers previous interactions to personalize the learning experience. Whether you're struggling with a specific concept or preparing for an exam, Study Buddy is here to assist you on your learning journey.

## Features

*   **Custom Explanations:** Get detailed explanations of various topics tailored to your specific needs.
*   **Quiz Generation:** Test your knowledge with automatically generated quizzes on different subjects.
*   **Memory:** Study Buddy remembers your previous interactions to provide a more personalized and efficient learning experience.
*   **Real-Time Chat:** Interact with the AI assistant in real-time using a user-friendly chat interface.
*   **Groq Integration:** (Optional) Utilize the Groq API for faster and more accurate responses (API key required).

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd study-buddy
    ```

    *Replace `<repository_url>` with the actual URL of the repository.*

2.  Create a virtual environment:

    A virtual environment helps to isolate the project dependencies.

    ```bash
    python -m venv venv
    ```

    *If you are using Python 3.3 or earlier, you may need to install the `virtualenv` package:*

    ```bash
    pip install virtualenv
    virtualenv venv
    ```

3.  Activate the virtual environment:

    *   On Windows:

        ```bash
        venv\Scripts\activate
        ```

        *If you encounter an error, try running `venv\Scripts\activate.bat`.*

    *   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    *This command installs all the required packages listed in the `requirements.txt` file.*

5.  Set up the environment variables:

    *   Create a `.env` file in the project root directory.

        *If a `.env` file already exists, ensure it is in the correct location.*

    *   Add your OpenAI API key and Groq API key to the `.env` file:

        ```
        OPENAI_API_KEY=<your_openai_api_key>
        GROQ_API_KEY=<your_groq_api_key>
        ```

        *Replace `<your_openai_api_key>` and `<your_groq_api_key>` with your actual API keys.*

6.  Run the application:

    ```bash
    python app.py
    ```

    *Ensure that you are in the project root directory when running this command.*

7.  Access the application in your browser at `http://127.0.0.1:5000`.

## Usage

*   Ask questions using the chat interface.
*   Use "groq:" prefix to use Groq API (e.g., "groq: Explain quantum physics").

## Troubleshooting

*   If you encounter a `ModuleNotFoundError`, ensure that you have activated the virtual environment and installed the dependencies correctly.
*   If the application does not start, check the console output for any error messages.
*   If the chat interface is not working, ensure that the Flask application is running and that the JavaScript code in `index.html` is correctly configured.

## Contributing

Feel free to contribute to the project by submitting pull requests.