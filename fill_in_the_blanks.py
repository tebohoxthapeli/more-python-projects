def main():
    sentences = [
        f"Her * had never seemed so * to me as it did that day.",
        f"When * convinced her of this she immediately * as if that was the intolerable part of the *.",
        f"The morning of the * I went up to * to see *; I couldn't seem to * him any other way.",
    ]

    print("\nNote: Enter 'q' to quit the program\n")

    for sen_num, sen in enumerate(sentences, 1):
        blank_count = sen.count("*")

        for i in range(1, blank_count + 1):
            sen = sen.replace("*", f"<blank {i}>", 1)

        print(f"{sen_num}. Fill in the blanks:\n{sen}\n")

        for i in range(1, blank_count + 1):
            old = f"<blank {i}>"
            new = input(f"{old}: ")

            if new.lower() == "q":
                print("\nQuitting program...")
                quit()

            sen = sen.replace(old, new)

        print(f"\nResult:\n{sen}\n\n")


if __name__ == "__main__":
    main()
