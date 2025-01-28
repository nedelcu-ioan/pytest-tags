test_tags = {}


def collect_tags(selected_tags, config, items):
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
    print(f"[debug] {filtered_items}")
    config.hook.pytest_deselected(items=deselected_items)
    items[:] = filtered_items


def exclude_tags(excluded_tags, config, items):
    filtered_items = []
    deselected_items = []

    for item in items:
        item_tags = set()
        for marker in item.iter_markers(name="tags"):
            item_tags.update(marker.args)

        if item_tags & excluded_tags:
            deselected_items.append(item)
        else:
            filtered_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = filtered_items


def pytest_collection_modifyitems(config, items):
    selected_tags = config.getoption("--tags")
    excluded_tags = config.getoption("--exclude-tags")

    if selected_tags:
        collect_tags(set(selected_tags.split(",")), config, items)

    if excluded_tags:
        exclude_tags(set(excluded_tags.split(",")), config, items)


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
    parser.addoption(
        "--exclude-tags",
        action="store",
        default=None,
        help="Exclude tags when runnign tests (comma-separated).\
If used without arguments, displays all available tags.",
    )


def pytest_runtest_call(item):
    """Store tags for each test."""
    item_tags = set()
    for marker in item.iter_markers(name="tags"):
        item_tags.update(marker.args)
    test_tags[item.nodeid] = item_tags
