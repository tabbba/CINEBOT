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

      3. **Environment Variables**: The application uses environment variables for configuration, such as the OpenAI API key and TMDb API key. Make sure to create a `.env` file in the root directory of your project and add your API keys like so:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    TMDB_API_KEY=your_tmdb_api_key_here
    ```

    Replace `your_openai_api_key_here` with your actual OpenAI API key and `your_tmdb_api_key_here` with your TMDb API key.

    These API keys are necessary for the application to function properly and access external services. The OpenAI API key is used for generating text-based content, while the TMDb API key is used for fetching movie data and generating visualizations.

   ### Running Cinebot

   After installing all dependencies and setting up the environment variables, you're ready to run the application. To do so, execute the following command in your terminal or command prompt from the root directory of the Cinebot project:

   ```
   streamlit run app.py
   ```

   This command starts the Streamlit server and opens the Cinebot application in your default web browser. You're now ready to interact with Cinebot and explore the world of cinema through an engaging chat interface.
   
![image](https://github.com/tabbba/CINEBOT/assets/130760858/113b8e55-42a0-43e6-a345-c232104bdbc2)
![image](https://github.com/tabbba/CINEBOT/assets/130760858/6208f91c-cc7d-4328-92e2-99b5320995c7)



