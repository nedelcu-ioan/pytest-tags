def test_include_single_tag(testdir):
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
    result = testdir.runpytest("--tags", "a")
    result.assert_outcomes(passed=2)


def test_include_multiple_tags(testdir):
    testdir.makepyfile(
        """
        import pytest

        @pytest.mark.tags("c", "a", "b")
        def test_example_0(): pass

        @pytest.mark.tags("a", "b")
        def test_example_1(): pass

        @pytest.mark.tags("a")
        def test_example_2(): pass
        """
    )
    result = testdir.runpytest("--tags", "b")
    result.assert_outcomes(passed=2)
