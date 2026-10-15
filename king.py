"""Calculate a student's total, average percentage, and letter grade."""


def get_subject_count():
	"""Return a positive whole-number subject count from user input."""
	while True:
		try:
			subject_count = int(input("How many subjects do you have? "))
			if subject_count > 0:
				return subject_count
			print("Please enter a number greater than zero.")
		except ValueError:
			print("Please enter a valid whole number.")


def get_mark(subject_number):
	"""Return a subject mark between 0 and 100, inclusive."""
	while True:
		try:
			mark = float(input(f"Enter the mark for subject {subject_number} (0-100): "))
			if 0 <= mark <= 100:
				return mark
			print("The mark must be between 0 and 100.")
		except ValueError:
			print("Please enter a valid number.")


def grade_for(percentage):
	"""Return the letter grade for an average percentage."""
	if percentage >= 90:
		return "A"
	if percentage >= 80:
		return "B"
	if percentage >= 70:
		return "C"
	if percentage >= 60:
		return "D"
	return "F"


def main():
	subject_count = get_subject_count()
	marks = [get_mark(subject_number) for subject_number in range(1, subject_count + 1)]

	total = sum(marks)
	percentage = total / subject_count
	grade = grade_for(percentage)

	print("\nResults")
	print(f"Total marks: {total:g} / {subject_count * 100}")
	print(f"Average percentage: {percentage:.2f}%")
	print(f"Final grade: {grade}")


if __name__ == "__main__":
	main()
