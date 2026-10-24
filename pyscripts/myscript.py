"""A small, friendly command-line idea generator."""

import random


IDEAS = {
	"build": [
		"Make a tiny app that tracks your favorite books.",
		"Write a script that sorts a folder by file type.",
		"Create a personal dashboard with today's top priorities.",
	],
	"play": [
		"Invent a one-minute word game.",
		"Generate a name and backstory for a tiny dragon.",
		"Make a quiz that matches people with a fictional sidekick.",
	],
	"learn": [
		"Explore a new Python module and build a small demo with it.",
		"Write a program that visualizes a simple sorting algorithm.",
		"Create flashcards for a topic you are learning.",
	],
}


def main() -> None:
	"""Choose and print a project idea."""
	print("\n✨ THE TINY IDEA MACHINE ✨")
	print("Categories: build, play, learn (press Enter for a surprise)")
	category = input("> ").strip().lower()

	if not category:
		category = random.choice(list(IDEAS))
	if category not in IDEAS:
		print("Please choose build, play, or learn.")
		return

	print(f"\nYour idea: {random.choice(IDEAS[category])}\n")


if __name__ == "__main__":
	main()
