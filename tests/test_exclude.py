def test_exclude_single_tag(testdir):
    testdir.makepyfile(
        """
        import pytest

        @pytest.mark.tags("a")
        def test_example_0():
             assert True

        @pytest.mark.tags("a")
        def test_example_1():
             assert True

        def test_example_2():
             assert True
        """
    )
    result = testdir.runpytest("--exclude-tags", "a")
    result.assert_outcomes(passed=1)


def test_exclude_multiple_tags(testdir):
    testdir.makepyfile(
        """
        import pytest

        @pytest.mark.tags("a", "b", "c")
        def test_example_0():
             assert True

        @pytest.mark.tags("a", "ISSUE-0x11", "PR-001")
        def test_example_1():
             assert True

        def test_example_2():
             assert True
        """
    )
    result = testdir.runpytest("--exclude-tags", "PR-001,b")
    result.assert_outcomes(passed=1)
