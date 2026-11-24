# Python Mad Libs

A simple command-line Mad Libs game built with Python.

## About the Project

This is a small Python project I originally created while learning programming. I recently rediscovered the project among my old files and decided to revisit it, complete the implementation, and update it for Python 3.

The program asks the user to provide different words, including names, adjectives, nouns, verbs, animals, food, and other random choices. It then inserts those words into a predefined story to generate a humorous result.

This repository also preserves the evolution of the project through its Git commit history.

## Features

- Interactive command-line interface.
- User-provided words and story customization.
- String interpolation using the `%` formatting operator.
- Predefined story template with 18 substitution positions.
- Python 3 compatible input handling.

## Technologies Used

- **Language:** Python 3
- **Interface:** Command-line interface (CLI)
- **String formatting:** `%` operator
- **Input handling:** `input()`
- **Version control:** Git and GitHub

## Requirements

- Python 3.x
- A terminal or command-line environment.

No external Python packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Shreyas-the-1st/Python-Mad-Libs.git
```

### 2. Navigate into the project

```bash
cd Python-Mad-Libs
```

### 3. Run the program

```bash
python3 Python-Mad-Libs.py
```

### 4. Play the game

Follow the prompts and enter your own words. Once all inputs have been collected, the program generates a completed story.

## How It Works

The program uses a predefined string template containing `%s` placeholders.

For example:

```python
STORY = "This morning %s woke up feeling %s."
```

User inputs are collected and inserted into the template using the `%` string-formatting operator:

```python
print(STORY % (name, ad1))
```

The complete program uses 18 substitution positions, with some variables reused throughout the story.

## Project Evolution

This repository documents the development of the project through separate Git commits.

| Stage | Description |
|---|---|
| Original version | Initial Mad Libs implementation using Python 2 input syntax |
| Story completion | Added the final story-output statement using `%` formatting |
| Python 3 migration | Replaced `raw_input()` with `input()` |

The original implementation is preserved in the Git history to document the project's development rather than presenting only the final version.

## What I Learned

Revisiting this project helped reinforce several fundamental programming concepts:

- Variables and data storage.
- Collecting user input.
- String manipulation and interpolation.
- Positional ordering of formatting arguments.
- Basic command-line application development.
- Git version control and incremental commits.
- Updating older Python code for Python 3 compatibility.

## Testing

Run the application with:

```bash
python3 Python-Mad-Libs.py
```

Provide responses to all prompts and verify that the final story is generated correctly.

There is currently no automated test suite.

## Future Improvements

Potential improvements for future versions:

- Add input validation.
- Allow users to generate different story templates.
- Introduce replay functionality.
- Improve the command-line interface.
- Add automated tests.

## Author

**Shreyas Bhat**

GitHub: [@Shreyas-the-1st](https://github.com/Shreyas-the-1st)

---

*An old student project, rediscovered, revisited, and updated.*
