import builtins
import barbie


def run_func_with_inputs(func, inputs, monkeypatch, capsys) -> str:
    """
    Runs a function that calls input() by feeding it a list of strings.
    Returns everything printed to stdout.
    """
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(it))
    func()
    return capsys.readouterr().out


def test_beach(monkeypatch, capsys):
    # Example:
    # people=4, chairs=30, sunscreen=10, ice cream=5, toys=15
    # total=60.00
    # discounted total=53.50
    # share=13.38
    out = run_func_with_inputs(
        barbie.beach_day_challenge,
        inputs=["4", "30.00", "10.00", "5.00", "15.00"],
        monkeypatch=monkeypatch,
        capsys=capsys
    )

    assert "Total cost before discounts: $60.00" in out
    assert "Total cost after discounts: $53.50" in out
    assert "Each person's share: $13.38" in out


def test_escape(monkeypatch, capsys):
    # Example:
    # Route 1: 100/50 = 2.00
    # Route 2: 120/70 = 1.71
    # Route 3: 140/60 = 2.33
    # time saved: 2.33 - 1.71 = 0.62
    out = run_func_with_inputs(
        barbie.escape_plan_challenge,
        inputs=["100", "50", "120", "70", "140", "60"],
        monkeypatch=monkeypatch,
        capsys=capsys
    )

    assert "Time required for Route 1: 2.00 hours" in out
    assert "Time required for Route 2: 1.71 hours" in out
    assert "Time required for Route 3: 2.33 hours" in out
    assert "The fastest route takes 1.71 hours." in out
    assert "Time saved by choosing the fastest route: 0.62 hours" in out


def test_societal(monkeypatch, capsys):
    # Example:
    # proposed=20, successful=13 -> 65.00%
    # need 15 for 75% -> need 2 more
    # remaining = 7
    out = run_func_with_inputs(
        barbie.society_reformation_challenge,
        inputs=["20", "13"],
        monkeypatch=monkeypatch,
        capsys=capsys
    )

    assert "Percentage of successful changes: 65.00%" in out
    assert "Number of additional changes needed to achieve a 75% success rate: 2" in out
    assert "Remaining changes to be implemented: 7" in out
