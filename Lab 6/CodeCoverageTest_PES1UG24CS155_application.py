import pytest

from traffic_fine import license_action, speeding_fine, total_penalty


@pytest.mark.parametrize(
    ("speed", "limit", "zone", "expected"),
    [
        (49, 50, "school", 0),
        (50, 50, "highway", 0),
        (51, 50, "school", 2000),
        (51, 50, "highway", 1000),
        (51, 50, "residential", 500),
        (70, 50, "school", 2000),
        (71, 50, "highway", 2000),
        (90, 50, "residential", 1000),
        (91, 50, "school", 6000),
        (150, 50, "unknown", 1500),
    ],
)
def test_speeding_fine_thresholds_zones_and_speed_boundaries(
    speed, limit, zone, expected
):
    assert speeding_fine(speed, limit, zone) == expected


@pytest.mark.parametrize(
    ("points", "commercial", "repeat", "expected"),
    [
        (0, False, False, "none"),
        (3, True, True, "none"),
        (4, False, False, "notice"),
        (7, True, False, "notice"),
        (8, False, False, "warning"),
        (11, True, True, "suspend"),
        (12, True, False, "revoke"),
        (12, False, False, "suspend"),
        (20, True, True, "revoke"),
    ],
)
def test_license_action_thresholds_and_licence_types(
    points, commercial, repeat, expected
):
    assert license_action(points, commercial, repeat) == expected


def test_total_penalty_returns_zero_for_empty_list():
    assert total_penalty([]) == 0


@pytest.mark.parametrize(
    ("fines", "expected"),
    [
        ([250], 250),
        ([0], 0),
        ([100, 200, 300], 600),
        ([4000, 5999], 9999),
        ([5000, 5000], 10000),
        ([7000, 4000], 10000),
    ],
)
def test_total_penalty_sums_and_caps_valid_fines(fines, expected):
    assert total_penalty(fines) == expected


@pytest.mark.parametrize("fines", [[-1], [100, -1], [50, 25, -100]])
def test_total_penalty_rejects_negative_fines(fines):
    with pytest.raises(ValueError, match="^negative fine$"):
        total_penalty(fines)
