# ssh-pwner


# SSH-PWNER

This repository contains a tool for SSH operations using Python and Paramiko.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone git@github.com:angusgee/ssh-pwner.git
    cd ssh-pwner
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```sh
      .\venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```sh
      source venv/bin/activate
      ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the application**:

First you will want to change the IP address from `127.0.0.1` to your real target IP. 

Then run the application:

    ```sh
    python ssh-pwner.py
    ```

