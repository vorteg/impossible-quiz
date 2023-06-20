import time
from dataclasses import dataclass
from random import choice, shuffle


@dataclass(slots=True)
class Question:
    question: str
    answers: list[str]
    correct_answer: str


def random_question(questions: list[Question]) -> int:
    question: Question = choice(questions)
    print(f"{question.question}")

    shuffle(question.answers)

    for answer in question.answers:
        print("-", answer)

    user_input: str = input("\nYour answer >> ").lower().strip()

    if user_input == question.correct_answer:
        print("Correct!\n")
        questions.remove(question)
        return 1
    else:
        print(f"Wrong, the answer was: {question.correct_answer.capitalize()}\n")
        questions.remove(question)
        return 0


def run_quiz(questions: list[Question]):
    total_score: int = 0
    while questions:
        score: int = random_question(questions=questions)
        total_score += score
        time.sleep(2)
    else:
        print("Final score:", total_score)


def get_questions() -> list[Question]:
    return [
        Question(
            question="How are you",
            answers=["Good", "Bad", "Ok", "Potato"],
            correct_answer="good",
        ),
        Question(
            question="What is your name?",
            answers=["Mario", "Luigi", "Peach"],
            correct_answer="luigi",
        ),
        Question(
            question="What time is it?",
            answers=["10", "11", "12", "13"],
            correct_answer="11",
        ),
        Question(
            question="What is 1 + 1?",
            answers=["The answer", "The question"],
            correct_answer="the question",
        ),
    ]


def main():
    questions: list[Question] = get_questions()
    run_quiz(questions=questions)


if __name__ == "__main__":
    main()
