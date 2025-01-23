test_tags = {}


def pytest_collection_modifyitems(config, items):
    selected_tags = config.getoption("--tags")

    if not selected_tags:
        return

    selected_tags = set(selected_tags.split(","))
    filtered_items = []
    deselected_items = []

    for item in items:
        item_tags = set()
        for marker in item.iter_markers(name="tags"):
            item_tags.update(marker.args)

        if item_tags & selected_tags:
            filtered_items.append(item)
        else:
            deselected_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = filtered_items


def pytest_configure(config):
    """Register the 'tags' marker."""
    config.addinivalue_line("markers", "tags(*tags): add tags to a given test")


def pytest_addoption(parser):
    """Add the --tags option to pytest."""
    parser.addoption(
        "--tags",
        action="store",
        default=None,
        help="Run only tests with the specified tags (comma-separated).\
If used without arguments, displays all available tags.",
    )


def pytest_runtest_call(item):
    """Store tags for each test."""
    item_tags = set()
    for marker in item.iter_markers(name="tags"):
        item_tags.update(marker.args)
    test_tags[item.nodeid] = item_tags
