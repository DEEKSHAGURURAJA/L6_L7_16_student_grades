# ==============================================================================
# Student Name: Deeksha G
# SRN: PES1UG24AM078
# Course: PES_SE_B_2026B
# Lab 6: Code Coverage Analysis
# Focus: Statement / Line Coverage (Ensuring >= 90% statement execution)
# ==============================================================================

import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


def test_letter_grade_all_statements():
    # Covers line 3 (ValueError for negative marks)
    with pytest.raises(ValueError):
        letter_grade(-5)

    # Covers lines 5, 7, 9, 11, 13, 15, 16
    assert letter_grade(95) == "S"
    assert letter_grade(85) == "A"
    assert letter_grade(75) == "B"
    assert letter_grade(65) == "C"
    assert letter_grade(55) == "D"
    assert letter_grade(45) == "E"
    assert letter_grade(35) == "F"


def test_final_marks_all_statements():
    # Covers lines 20-21 (ValueError when internal > 40)
    with pytest.raises(ValueError):
        final_marks(45, 50, False)

    # Covers lines 22, 23, 24, 25, 26, 27 (total > 100 path)
    assert final_marks(40, 60, True) == 100


def test_exam_eligibility_all_statements():
    # Covers lines 31-32 (fees not paid -> blocked)
    assert exam_eligibility(80, False, False) == "blocked"

    # Covers lines 33-34 (attendance >= 75 -> eligible)
    assert exam_eligibility(80, True, False) == "eligible"

    # Covers lines 35-36 (attendance >= 65 and medical -> eligible)
    assert exam_eligibility(70, True, True) == "eligible"

    # Covers line 37 (detained)
    assert exam_eligibility(50, True, False) == "detained"
