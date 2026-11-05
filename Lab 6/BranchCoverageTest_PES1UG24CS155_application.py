import pytest

from traffic_fine import license_action, speeding_fine, total_penalty


@pytest.mark.parametrize(
    ("speed", "zone", "expected"),
    [
        (50, "school", 0),       # speed <= limit: true
        (51, "school", 2000),    # speed <= limit: false; school: true
        (51, "highway", 1000),   # school: false; highway: true
        (51, "unknown", 500),    # school: false; highway: false
        (70, "school", 2000),    # excess > 40 false; > 20 false at 20
        (71, "school", 4000),    # excess > 40 false; > 20 true at 21
        (90, "highway", 2000),  # excess > 40 false at 40; > 20 true
        (91, "highway", 3000),  # excess > 40 true at 41
    ],
)
def test_speeding_fine_covers_decision_outcomes(speed, zone, expected):
    assert speeding_fine(speed, 50, zone) == expected


@pytest.mark.parametrize(
    ("points", "commercial", "repeat", "expected"),
    [
        (12, True, False, "revoke"),    # >=12 true; commercial true
        (12, False, False, "suspend"),  # >=12 true; commercial false
        (8, True, True, "suspend"),     # >=12 false; >=8 true; repeat true
        (8, False, False, "warning"),   # >=12 false; >=8 true; repeat false
        (4, False, False, "notice"),    # >=8 false; >=4 true
        (3, False, True, "none"),      # >=4 false
    ],
)
def test_license_action_covers_nested_decisions(
    points, commercial, repeat, expected
):
    assert license_action(points, commercial, repeat) == expected


def test_total_penalty_empty_iterable_terminates_without_loop_entry():
    assert total_penalty([]) == 0


def test_total_penalty_loop_runs_and_terminates_after_valid_fines():
    assert total_penalty([10, 20, 30]) == 60


def test_total_penalty_negative_fine_branch_raises():
    with pytest.raises(ValueError, match="^negative fine$"):
        total_penalty([10, -1])


def test_total_penalty_nonnegative_branch_and_uncapped_total():
    assert total_penalty([100, 200]) == 300


def test_total_penalty_cap_branch_and_exact_boundary():
    assert total_penalty([5000, 5000]) == 10000
    assert total_penalty([5000, 5001]) == 10000
