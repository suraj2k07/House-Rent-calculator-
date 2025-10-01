# House Rent Predictor

## Overview

The **House Rent Predictor** is a web application designed to estimate the rental price of a house. By inputting key features such as **BHK**, **size** (in sqft), **floor number**, **number of bathrooms**, **furnishing status**, **tenant type**, **area type**, **locality**, and **city**, users can obtain an estimated monthly rent. The application utilizes a **linear regression model** trained on a dataset to make these predictions.

---

## Features

-   **User Input Form**: Enter details about the property.
-   **Prediction Engine**: Uses a trained **linear regression model** to predict the rent based on user inputs.
-   **Responsive Design**: Accessible on various devices.

---

## Technologies Used

| Category | Technology |
| :--- | :--- |
| **Frontend** | HTML, CSS |
| **Backend** | Python (**Flask**) |
| **Machine Learning** | Python (**scikit-learn**) |
| **Data Source** | Kaggle |
| **Deployment** | Render |

---

## Installation

To run this project from a web browser, access the deployed application:

**Deployment Link:** [https://house-rent-calculator.onrender.com/](https://house-rent-calculator.onrender.com/)

### Running Locally

To set up and run the predictor on your local machine:

1.  **Clone the repository** and navigate to the project directory:

    ```bash
    git clone [https://github.com/suraj2k07/House-Rent-calculator-](https://github.com/suraj2k07/House-Rent-calculator-)
    cd monthlyrent
    ```

2.  **Install the required dependencies** (listed in `requirements.txt`):

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Flask application** (using `app.py`):

    ```bash
    python app.py
    ```

4.  Open your web browser and navigate to the local address to view the application:

    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

---

## How to Use

1.  Once the application loads in your browser, you will see the input form.
2.  Fill in all the required details about the property, such as the **BHK**, **Size**, **City**, and **Locality**.
3.  Click the **"Predict Rent"** button.
4.  The application will display the predicted monthly rental price for the property.
