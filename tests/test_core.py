from quality_agent.core import QualityResult


def test_quality_result_is_explicit() -> None:
    result = QualityResult(passed=True, checks=4, violations=0)
    assert result.passed is True
    assert result.violations == 0
