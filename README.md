# IdeaVault Django Project
![image](https://github.com/sanyuktajoshi/AgastyaProject/assets/79038075/cfd33970-93e9-4afd-8784-68607ce50d29)

Welcome to IdeaVault, a Django-based platform that empowers students to showcase their project ideas and connect with mentors/sponsors. This README file provides essential information to help you understand, set up, and contribute to the IdeaVault project.

## Features

- **Student Profiles:** Students can create profiles and upload details about their project ideas.
- **Project Showcase:** A dedicated space for students to showcase their projects with detailed information.
- **Mentor/Sponsor Interaction:** Mentors/Sponsors can explore student projects and choose to offer mentorship or sponsorship.
- **Secure Authentication:** User authentication and authorization are implemented to ensure secure access.
- **User-Friendly Interface:** Intuitive design for easy navigation and a seamless user experience.

## Installation

To set up IdeaVault on your local machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/AgastyaProject.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ideavault
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

Visit `http://localhost:8000` in your web browser to access IdeaVault.


