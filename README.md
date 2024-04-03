   # CINEBOT

   Cinebot is an innovative application that seamlessly integrates OpenAI's GPT models with Streamlit's user-friendly interface. It serves as a chatbot, leveraging natural language processing to provide accurate and contextually relevant responses to cinema-related queries.

   ### Installation and Setup

   Before running the application, you need to install the necessary dependencies. These dependencies are listed in the `requirements.txt` file included in the project. To install these dependencies, follow the steps below:

   1. **Ensure Python is Installed**: Cinebot requires Python. It's recommended to use Python 3.11 or newer. You can check your Python version by running `python --version` or `python3 --version` in your terminal or command prompt.

   2. **Install Dependencies**: Navigate to the root directory of the Cinebot project in your terminal or command prompt. Run the following command to install all required libraries:

      ```
      pip install -r requirements.txt
      ```

      This command reads the `requirements.txt` file and installs all the Python libraries listed there.

   3. **Environment Variables**: The application uses environment variables for configuration, such as the OpenAI API key. Make sure to create a `.env` file in the root directory of your project and add your OpenAI API key like so:

      ```
      OPENAI_API_KEY=your_api_key_here
      ```

      Replace `your_api_key_here` with your actual OpenAI API key.

   ### Running Cinebot

   After installing all dependencies and setting up the environment variables, you're ready to run the application. To do so, execute the following command in your terminal or command prompt from the root directory of the Cinebot project:

   ```
   streamlit run app.py
   ```

   This command starts the Streamlit server and opens the Cinebot application in your default web browser. You're now ready to interact with Cinebot and explore the world of cinema through an engaging chat interface.

