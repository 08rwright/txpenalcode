# txpenalcode
Tx-PenalCode-UI
### Texas Law Guide

This repository contains a Python script that utilizes Streamlit to create an interactive web application called "Texas Law Guide." The application allows users to input a legal term or concept and retrieves information from the Texas Penal Code regarding its definition, elements of offense, and punishment.

#### Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine:

```
git clone https://github.com/yourusername/your-repository.git
```

2. Navigate to the directory containing the cloned repository:

```
cd your-repository
```

3. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

4. Set up the required API key:

   - Obtain an OpenAI API key and save it in a file named `apikey.py`. Make sure to name the variable containing the API key as `apikey`.

5. Run the Streamlit application:

```
streamlit run app.py
```

#### Usage

Once the application is running, you will see the title "Texas Law Guide" and a text input field labeled "Example: 'Define Assault'." 

- Enter a legal term or concept (e.g., "Assault") into the text input field.
- Press Enter or click outside the input field to submit the query.

The application will fetch information from the Texas Penal Code related to the provided term, including its definition, elements of offense, and punishment, and display it on the screen.

#### Components

The main components of the Python script include:

- Importing necessary libraries such as `os`, `streamlit`, and custom modules.
- Setting up the Streamlit application with a title and a text input field for user input.
- Defining prompt templates for querying the Texas Penal Code.
- Generating responses using the OpenAI language model based on the user input.
- Displaying the retrieved information in a styled container on the web interface.

#### Note

Ensure that you have proper access rights to use the Texas Penal Code data and comply with any legal regulations regarding its usage.

For any issues or suggestions, please feel free to open an issue in this repository.

Thank you for using the Texas Law Guide application!
