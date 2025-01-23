# pytest-tags

**pytest-tags** is a simple pytest plugin that allows tagging tests with arbitrary strings.  
It supports filtering tests by tags and displays a summary of failures grouped by tags.

## Features
- Tag tests using `@tag(...)`.
- Run tests by specific tags using `pytest --tags tag1,tag2`.
- View tag-based failure summaries.

## Installation
```bash
pip install pytest-tags

