from thefuck import gotchas


def test_mutable_default_bug_reproduces():
    # The buggy version leaks state between calls...
    gotchas.mutable_default_buggy("a")
    assert gotchas.mutable_default_buggy("b") == ["a", "b"]
    # ...while the fixed version starts fresh each time.
    assert gotchas.mutable_default_fixed("a") == ["a"]
    assert gotchas.mutable_default_fixed("b") == ["b"]


def test_float_equality():
    assert gotchas.float_equality_buggy() is False
    assert gotchas.float_equality_fixed() is True


def test_late_binding():
    assert gotchas.late_binding_buggy() == [2, 2, 2]
    assert gotchas.late_binding_fixed() == [0, 1, 2]


def test_mutate_while_iterating():
    # The buggy version skips a consecutive even number (4 survives).
    assert gotchas.mutate_while_iterating_buggy([2, 4, 6]) == [4]
    assert gotchas.mutate_while_iterating_fixed([2, 4, 6]) == []


def test_division():
    assert gotchas.division_buggy(7, 2) == 3
    assert gotchas.division_fixed(7, 2) == 3.5


def test_registry_and_explain():
    assert set(gotchas.list_gotchas()) == set(gotchas.GOTCHAS)
    text = gotchas.explain("mutable_default")
    assert "Mutable default argument" in text
