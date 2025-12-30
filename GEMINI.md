# Project Overview

This project is a series of Python-based tasks designed to teach users how to interact with various Large Language Models (LLMs) through the DIAL API. The tasks focus on configuring and exploring different request parameters to control the output of the LLMs.

**Key Technologies:**

*   Python 3.11+
*   requests

**Architecture:**

The project is structured into a `task` directory containing a series of task files, each focusing on a specific API parameter. A simple client application in `task/app` is provided to send requests to the DIAL API.

# Building and Running

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Set your API key:**
    *   Ensure that you are connected to the EPAM VPN.
    *   Get the DIAL API key from the internal EPAM support portal.

3.  **Run a task:**

    To run a specific task, execute the corresponding Python file. For example, to run the first task:

    ```bash
    python -m task.1-task-models
    ```

    You will need to modify the task files to experiment with different parameters as described in the `TODO` comments within each file.

# Development Conventions

*   The project uses the `requests` library for making HTTP requests to the DIAL API.
*   Each task is self-contained in a single Python file and is meant to be run individually.
*   The `task/models` directory contains data classes for representing conversations, messages, and roles.
*   The `task/app` directory contains the core logic for the DIAL client and the main application loop.
