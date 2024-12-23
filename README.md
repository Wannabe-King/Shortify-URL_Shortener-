Here’s the updated version of your project installation guide, which includes the steps to create a virtual environment (`venv`) before installing dependencies from `requirements.txt`:

```markdown
# URL Shortener

A simple Python-based project that shortens long URLs into compact, shareable links.

## Features

- Shortens long URLs into manageable and shareable links.
- Built using Python for easy customization and deployment.
- Lightweight and fast.

## Requirements

- Python 3.x
- Pip (Python Package Manager)

## Installation

### Windows

1. **Download and Install Python**:
   - Download Python from the official website: [Python.org](https://www.python.org/downloads/)
   - Make sure to check the box for adding Python to the system `PATH` during installation.

2. **Clone the repository**:
   ```bash
   git clone https://github.com/akashbhaskar2011/URL_Shortner.git
   cd URL_Shortner
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   ```bash
   venv\Scripts\activate
   ```

5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the project**:
   ```bash
   python manage.py runserver
   ```

### MacOS

1. **Install Homebrew** (if not already installed):
   Open your terminal and run:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**:
   ```bash
   brew install python
   ```

3. **Clone the repository**:
   ```bash
   git clone https://github.com/akashbhaskar2011/URL_Shortner.git
   cd URL_Shortner
   ```

4. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

5. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

6. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

7. **Run the project**:
   ```bash
   python manage.py runserver
   ```

### Ubuntu

1. **Install Python and Git**:
   Open your terminal and run the following commands:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip git
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/akashbhaskar2011/URL_Shortner.git
   cd URL_Shortner
   ```

3. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the project**:
   ```bash
   python3 manage.py runserver
   ```

## Usage

1. After running the project, open your browser and go to:
   ```
   http://127.0.0.1:8000
   ```

2. Enter a long URL and hit "Shorten" to get your shortened URL.