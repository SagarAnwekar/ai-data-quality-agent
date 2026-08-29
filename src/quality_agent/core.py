from dataclasses import dataclass


@dataclass(frozen=True)
class QualityResult:
    passed: bool
    checks: int
    violations: int
