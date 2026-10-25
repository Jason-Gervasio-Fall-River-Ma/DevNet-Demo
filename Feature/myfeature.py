"""A small greeting feature."""


def greet(name: str) -> str:
	"""Return a friendly greeting for *name*."""
	cleaned_name = name.strip()
	if not cleaned_name:
		raise ValueError("name must not be empty")
	return f"Hello, {cleaned_name}!"


if __name__ == "__main__":
	print(greet("World!"))
