#program to find the wordcount in a file (input.txt) for each line and then print the output
def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            lines = infile.readlines()
            word_count = {}

            outfile.writelines(lines)
            outfile.write("\nWord_Count:\n")

            for line in lines:
                words = line.strip().split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1

            for word, count in word_count.items():
                outfile.write(f"{word}: {count}\n")

            print(f"Word count has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")

if __name__ == "__main__":
    count_words_in_file("input.txt", "output.txt")
