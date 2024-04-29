import random

# Function to convert Arabic numerals to Bengali numerals
def arabic_to_bengali(number):
    bengali_digits = {
        '0': '০',
        '1': '১',
        '2': '২',
        '3': '৩',
        '4': '৪',
        '5': '৫',
        '6': '৬',
        '7': '৭',
        '8': '৮',
        '9': '৯',
    }
    return ''.join([bengali_digits[digit] for digit in str(number)])

# Defined paths For Question_Paper(GEN).txt
output_file_path = "E:\Codeing\Python Language\Projects\Project_11_Question_Generator\Question_Paper(GEN).txt"

      #Intro Text
with open(output_file_path, "w", encoding="UTF-8") as output_file:
    output_file.write("\t\t\t\tডিপ্লোমা-ইন-ইঞ্জিনিয়ারিং\n\t\t\t\tবিষয় : জাভা প্রোগ্রামিং\n\t\t\t\t(কোডঃ ২৮৫৪১)\n\n")


def Question_Generator(Info1, Info2, Info3, Info4, output):
    # Create an empty list to store the random texts
    random_texts = []

    # Generate 5 random numbers
    random_numbers = random.sample(range(1, Info1[0]), Info1[1])


    # Read the corresponding lines from the input file and add Bengali numbering
    for i, num in enumerate(random_numbers, start=Info4 + 1):
        with open(Info2, "r", encoding="UTF-8") as file:
            lines = file.readlines()
            if num <= len(lines):
                bengali_text = lines[num - 1].strip()
                bengali_number = arabic_to_bengali(i)
                random_texts.append(f"{bengali_number}. {bengali_text}")

    # Join the random texts into a single string
    random_text = "\n".join(random_texts)

    # Write the header to the output file
    with open(output, "a", encoding="UTF-8") as output_file:
        output_file.write(Info3)

    # Append the random texts to the output file
    with open(output, "a", encoding="UTF-8") as output_file:
        output_file.write(random_text)

#Defineing Elements
A_1 = (39, 5)
A_2 = r"E:\Codeing\Python Language\Projects\Project_11_Question_Generator\Subjects\Java Programming\A_1.txt"
A_3 = "\t\t(ক ও খ বিভাগের সকল প্রশ্নের এবং গ বিভাগের যেকোন ২টি প্রশ্নের উত্তর দাও)\n\t\t\t\tক বিভাগ (মান: ১ X ৫ = ৫)\n\n"
A_4 = 0

S_1 = (26, 3)
S_2 = r"E:\Codeing\Python Language\Projects\Project_11_Question_Generator\Subjects\Java Programming\S_1.txt"
S_3 = "\n\n\t\t\t\tখ বিভাগ (মান: ২ X ৩ = ৬) \n\n"
S_4 = 5

R_1 = (7, 3)
R_2 = r"E:\Codeing\Python Language\Projects\Project_11_Question_Generator\Subjects\Java Programming\R_1.txt"
R_3 = "\n\n\t\t\t\tগ বিভাগ (মান : ৪.৫ x ২ = ১) \n\n"
R_4 = 8


Question_Generator(A_1, A_2, A_3, A_4, output_file_path)
Question_Generator(S_1, S_2, S_3, S_4, output_file_path)
Question_Generator(R_1, R_2, R_3, R_4, output_file_path)



