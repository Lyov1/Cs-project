import user_code
import random 

subject_file = r"Tables\subjects.csv"
questions_file = r"Tables\questions.csv"

# Internal Functions
def __find_class(class_code):
    subjects = user_code.__read_file_csv(subject_file)

    for subject in subjects:
        if subject[3] == class_code:
            return subject
        
def __find_questions(class_code):
    data = user_code.__read_file_csv(questions_file)
    needed_questions = []
    for row in data:
        if row[7] == class_code:
            needed_questions.append(row)

    return needed_questions

def __sort_questions(class_code):
    if __find_class(class_code):
        questions = __find_questions(class_code)
        easy = []
        medium = []
        hard = []
        for question in questions:
            if question[8] == "easy":
                easy.append(question)
            if question[8] == "medium":
                medium.append(question)
            if question[8] == "hard":
                hard.append(question)
        return [easy, medium, hard]


def __generate_test(class_code, easy_count, medium_count, hard_count):
    try:
        questions = __sort_questions(class_code)
        easy = questions[0]
        medium = questions[1]
        hard = questions[2]

        new_quiz = []

        for i in range(easy_count):
            number = random.randint(0, len(easy) - 1)
            new_quiz.append(easy[number])
            easy.remove(easy[number])

        for i in range(medium_count):
            number = random.randint(0, len(medium) - 1)
            new_quiz.append(medium[number])
            medium.remove(medium[number])

        for i in range(hard_count):
            number = random.randint(0, len(hard) - 1)
            new_quiz.append(hard[number])
            hard.remove(hard[number])

        return new_quiz
    except:
        raise Exception("H-hayvan, edqan harc chka")
        
# External Functions
def get_test(class_code, difficulty):
    quiz = []
    if difficulty == "easy":
        quiz = __generate_test(class_code, 5, 4, 1)
    if difficulty == "medium":
        quiz = __generate_test(class_code, 4, 4, 2)
    if difficulty == "hard":
        quiz = __generate_test(class_code, 3, 3, 4)

    return quiz


# Example Usage
get_test("CS102","hard") 