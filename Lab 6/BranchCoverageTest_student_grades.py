# ==============================================================================
# Student Name: Deeksha G
# SRN: PES1UG24AM078
# Course: PES_SE_B_2026B
# Lab 6: Branch Coverage Analysis
# Focus: Branch Coverage (Ensuring all decision branches evaluate True and False)
# ==============================================================================

import pytest
from student_grades import letter_grade, final_marks, exam_eligibility

# ------------------------------------------------------------------------------
# 1. Tests for letter_grade(marks)
# Decision Branches:
# - marks < 0 or marks > 100:
#     * marks < 0 is True
#     * marks > 100 is True
#     * neither is True (valid marks)
# - marks >= 90: True ("S") / False
# - marks >= 80: True ("A") / False
# - marks >= 70: True ("B") / False
# - marks >= 60: True ("C") / False
# - marks >= 50: True ("D") / False
# - marks >= 40: True ("E") / False
# - Else: "F"
# ------------------------------------------------------------------------------

def test_letter_grade_invalid_negative():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-1)


def test_letter_grade_invalid_exceeds_100():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(101)


def test_letter_grade_boundaries_and_ranges():
    # Grade S: 90 to 100
    assert letter_grade(100) == "S"
    assert letter_grade(90) == "S"

    # Grade A: 80 to 89
    assert letter_grade(89) == "A"
    assert letter_grade(80) == "A"

    # Grade B: 70 to 79
    assert letter_grade(79) == "B"
    assert letter_grade(70) == "B"

    # Grade C: 60 to 69
    assert letter_grade(69) == "C"
    assert letter_grade(60) == "C"

    # Grade D: 50 to 59
    assert letter_grade(59) == "D"
    assert letter_grade(50) == "D"

    # Grade E: 40 to 49
    assert letter_grade(49) == "E"
    assert letter_grade(40) == "E"

    # Grade F: below 40 down to 0
    assert letter_grade(39) == "F"
    assert letter_grade(0) == "F"


# ------------------------------------------------------------------------------
# 2. Tests for final_marks(internal, external, has_project)
# Decision Branches:
# - internal > 40 or external > 60:
#     * internal > 40 is True
#     * external > 60 is True
#     * both valid (False)
# - has_project:
#     * True: adds 5 bonus marks
#     * False: no bonus
# - total > 100 (when has_project is True):
#     * True: capped at 100
#     * False: total remains total + 5
# ------------------------------------------------------------------------------

def test_final_marks_internal_out_of_range():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(41, 50, False)


def test_final_marks_external_out_of_range():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(30, 61, False)


def test_final_marks_without_project():
    # has_project is False (branch 23 -> False, skipping bonus)
    assert final_marks(30, 45, False) == 75


def test_final_marks_with_project_not_exceeding_100():
    # has_project is True, total + 5 <= 100 (branch 25 -> False)
    assert final_marks(35, 55, True) == 95


def test_final_marks_with_project_exceeding_100_cap():
    # has_project is True, total + 5 > 100 (branch 25 -> True, capped at 100)
    assert final_marks(40, 60, True) == 100


# ------------------------------------------------------------------------------
# 3. Tests for exam_eligibility(attendance, fees_paid, has_medical)
# Decision Branches:
# - not fees_paid: True -> "blocked", False -> continue
# - attendance >= 75: True -> "eligible", False -> continue
# - attendance >= 65 and has_medical:
#     * attendance >= 65 and True -> "eligible"
#     * attendance >= 65 and False -> "detained"
#     * attendance < 65 -> "detained"
# ------------------------------------------------------------------------------

def test_exam_eligibility_fees_unpaid():
    # not fees_paid -> True
    assert exam_eligibility(85, False, True) == "blocked"


def test_exam_eligibility_high_attendance():
    # fees_paid is True, attendance >= 75
    assert exam_eligibility(75, True, False) == "eligible"
    assert exam_eligibility(90, True, False) == "eligible"


def test_exam_eligibility_condonation_with_medical():
    # fees_paid is True, 65 <= attendance < 75, has_medical is True
    assert exam_eligibility(65, True, True) == "eligible"
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_eligibility_condonation_without_medical():
    # fees_paid is True, 65 <= attendance < 75, has_medical is False
    assert exam_eligibility(65, True, False) == "detained"
    assert exam_eligibility(70, True, False) == "detained"


def test_exam_eligibility_low_attendance_detained():
    # fees_paid is True, attendance < 65 (medical certificate cannot compensate)
    assert exam_eligibility(64, True, True) == "detained"
    assert exam_eligibility(40, True, False) == "detained"
