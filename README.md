# pytest-tags

`pytest-tags` is a `pytest` plugin that allows you to organize and filter your tests using tags. Tags are flexible and can represent test characteristics such as:

- Issue Numbers: Track tests associated with specific bug reports or feature requests (e.g., issue-123).
- Pull Requests (PRs): Identify tests related to specific PRs (e.g., pr-456).
- Components: Group tests by application modules or components (e.g., auth, database, frontend).
- Test Types: Highlight specific test types (e.g., smoke, regression, performance).
- With pytest-tags, you can run only the tests matching certain tags for faster and more targeted test execution.

## usage

### Tagging Tests
Use the `@pytest.mark.tags()` marker to tag tests with one or more labels.

```python
import pytest

# Tagging tests with single and multiple tags
@pytest.mark.tags("smoke", "regression")
def test_example_1():
    assert True

@pytest.mark.tags("performance")
def test_example_2():
    assert True

def test_example_3():
    assert True  # Untagged test
```

### Running Tagged Tests

To run tests with specific tags, use the --tags option followed by the desired tag(s).

```bash
pytest --tags smoke
```
