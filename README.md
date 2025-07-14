# DFA Password Validation

A web and command-line application for validating passwords using a Deterministic Finite Automaton (DFA) and a naive rule-based approach. This project demonstrates how DFAs can be used for pattern recognition and validation tasks, specifically for password checking.

## Features

- **Web Interface**: User-friendly web app built with Flask for password validation.
- **Command-Line Tool**: Simple CLI for quick password checks.
- **Two Validation Methods**:
  - **DFA-Based**: Uses a deterministic finite automaton to validate passwords.
  - **Naive Rule-Based**: Uses a direct state-transition logic (mirroring the DFA) for validation.
- **Performance Metrics**: Web app displays validation time for each method.

## Password Rules

A valid password must:

- Be at least **5 characters** long.
- Contain only the following characters: `a`, `b`, `A`, `B`, `0`, `1` (case-sensitive).
- Follow a specific sequence as defined by the DFA (see `dfa transition table.md` for the full state table).
- The DFA starts at state `q1` and only accepts if it ends in state `q15` after processing the entire input.
- Any invalid character or transition leads to rejection.

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Toc_Group_Project
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install Flask
   ```

## Usage

### Web Application

1. Run the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. Enter a password and select a validation method (DFA or Naive).
4. View the result and validation time.

### Command-Line Tool

1. Run the CLI tool:
   ```bash
   python command.py
   ```
2. Follow the prompts to select a validation method and enter a password.

## File Structure

- `app.py` - Flask web application
- `command.py` - Command-line interface
- `dfa.py` - DFA implementation
- `naive.py` - Naive rule-based validator
- `dfa transition table.md` - DFA state transition table
- `templates/` - HTML templates for the web app
- `static/` - CSS styles

## Authors

- Darren Drummond
- Frederica Forbes
- Justin Edwards
- Rajaire Thomas

---

_July 13, 2025_
