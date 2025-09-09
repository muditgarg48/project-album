# Project A.L.B.U.M. Backend

This directory contains the backend codebase and database handling for Project A.L.B.U.M. The backend is based on Flask and utilises SQLite for its database purpose.

### Libraries Used:

#### MTCNN: Face detection

**Resources used for researching:**

- CampusX; Introduction to Face Detection using MTCNN: 
    https://www.youtube.com/watch?v=ZjbWF9f3VD4

#### OpenCV: Image processing

#### PIL: Metadata extraction

### Setup

After the repository is cloned,

- Navigate to the `backend` folder from root of the repository in the terminal:
    ```
    cd backend
    ```

- Create a virtual environment to contain all the dependency installation:
    ```
    python -m venv venv
    ```

- Then activate the virtual environment:
    **For Windows**:
    ```
    "venv/Scripts/activate.bat"
    ```
    **For Linux**:
    ```
    "venv/Scripts/activate"
    ```

- Remember to make sure that virtual environment is always active when initiating the backend server. It is evident by `(venv)` written before the present working directory path within each command line in the terminal

- Install all the dependencies to make the virtual environment and backend ready:
    ```
    python -m pip install -r requirements
    ```
  
### Run

To run the project, make sure to follow the [setup](#setup) before proceeding.

- Make sure that the terminal is in the `backend` folder. The terminal should display a path with a similar ending ` ...\...\project-album\frontend>`

- Once the dependencies are installed and ready, start the frontend server:
    ```
    npm run dev
    ```


# Project A.L.B.U.M. Database

Once the backend [setup](#setup) is completed, the SQLite database should be ready for data storage and management for the project.

### Prechecks

- Verify that you have SQLite installed on your system
- Verify the existence of the `database.db` file exists in the `backend` directory.

### Database commands

- **Open SQLite shell**
    ```
    sqlite3 database.db
    ```

- **List all existing tables within the shell**
    ```
    .tables
    ```

- **To see the data stored within your `database.db` within the shell**
    ```
    SELECT * FROM <table_name>
    ```

- **Exit shell**
    ```
    .exit
    ```