from extract_entities import EntityExtraction
from fact_extraction import FactExtraction
from noun_chunk_extraction import NounExtraction
from redact_text import Redact


class MainClass:
    def __init__(self):
        self.redact_text = Redact()
        self.noun_extraction_instance = NounExtraction()
        self.fact_extraction_instance = FactExtraction()
        self.entity_extraction_instance = EntityExtraction()

    def fact(self):
        dog_facts = self.fact_extraction_instance.extract_facts("london.txt")
        print("Here are the things I know about Dogs:")
        print(dog_facts)

    def entity(self):
        entities = self.entity_extraction_instance.extract_entities("london.txt")
        print("Named entities detected in the text:")
        for entity, label in entities:
            print(f"{entity} ({label})")

    def nouns(self):
        nouns = self.noun_extraction_instance.extract_nouns("london.txt")
        for noun in nouns:
            print(f" - {noun}")

    def verbs(self):
        verbs = self.noun_extraction_instance.extract_nouns("london.txt")
        for verb in verbs:
            print(f" - {verb}")

    def redact(self):
        redacted_text = self.redact_text.scrub("london.txt")
        print("Redacted text:")
        print(redacted_text)

    def user_choice(self):
        while True:
            print("\nWhich method would you like to call?")
            print("1. Extract facts")
            print("2. Extract entities")
            print("3. Extract nouns")
            print("4. Extract verbs")
            print("5. Redact text")
            print("6. Quit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.fact()
            elif choice == "2":
                self.entity()
            elif choice == "3":
                self.nouns()
            elif choice == "4":
                self.verbs()
            elif choice == "5":
                self.redact()
            elif choice == "6":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main_instance = MainClass()
    main_instance.user_choice()
