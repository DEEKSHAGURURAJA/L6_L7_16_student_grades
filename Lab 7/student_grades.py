# ==============================================================================
# Student Name: Deeksha G
# SRN: PES1UG24AM078
# Course: PES_SE_B_2026B
# Lab 7: Fuzzing for Input Validation Bugs
# Fixed and hardened student_grades module
# ==============================================================================

def average_marks(marks_csv):
    """
    Computes average of marks from a comma-separated string.
    Hardened against: None, non-string, empty strings, missing values, non-numeric tokens.
    """
    if marks_csv is None or not isinstance(marks_csv, str):
        return None
    marks = []
    for m in marks_csv.split(','):
        item = m.strip()
        if item:
            try:
                marks.append(int(item))
            except ValueError:
                pass
    if not marks:
        return None
    return round(sum(marks) / len(marks), 2)


def parse_srn(srn):
    """
    Parses SRN into (campus, year, department).
    Hardened against: None, non-string, truncated strings, invalid year tokens.
    """
    if srn is None or not isinstance(srn, str) or len(srn) < 10:
        return None
    campus = srn[:4]
    year_str = srn[6:8]
    dept = srn[8:10]
    try:
        year = int(year_str)
        return campus, year, dept
    except ValueError:
        return None


def short_name(full_name):
    """
    Formats full name into 'F. Last' format.
    Hardened against: None, non-string, empty string, single-word names, multi-word names.
    """
    if full_name is None or not isinstance(full_name, str):
        return None
    parts = full_name.split()
    if not parts:
        return None
    first = parts[0]
    last = parts[-1] if len(parts) > 1 else ""
    if not first:
        return None
    initial = first[0].upper() + "."
    if last:
        return initial + " " + last.capitalize()
    return initial


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    print("Short Name:", result)


if __name__ == "__main__":
    main()
