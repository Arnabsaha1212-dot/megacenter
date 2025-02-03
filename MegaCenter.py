import json
import os

class MegaCenter:
    def __init__(self, dictionary_file='megacenter_dict.json'):
        self.dictionary_file = dictionary_file
        self.load_dictionary()

    def load_dictionary(self):
        if os.path.exists(self.dictionary_file):
            with open(self.dictionary_file, 'r', encoding='utf-8') as file:
                self.dictionary = json.load(file)
        else:
            self.dictionary = {}

    def save_dictionary(self):
        with open(self.dictionary_file, 'w', encoding='utf-8') as file:
            json.dump(self.dictionary, file, ensure_ascii=False, indent=4)

    def add_term(self, shortcut, full_form):
        self.dictionary[shortcut] = full_form
        self.save_dictionary()
        print(f"Added: '{shortcut}' -> '{full_form}'")

    def remove_term(self, shortcut):
        if shortcut in self.dictionary:
            del self.dictionary[shortcut]
            self.save_dictionary()
            print(f"Removed shortcut: '{shortcut}'")
        else:
            print(f"Shortcut '{shortcut}' not found!")

    def list_terms(self):
        if not self.dictionary:
            print("No terms in the dictionary.")
            return
        for shortcut, full_form in self.dictionary.items():
            print(f"'{shortcut}': '{full_form}'")

    def replace_shortcuts(self, text):
        words = text.split()
        replaced_text = ' '.join(self.dictionary.get(word, word) for word in words)
        return replaced_text

def main():
    mega_center = MegaCenter()

    while True:
        print("\nMegaCenter - Custom Dictionary Manager")
        print("1. Add Term")
        print("2. Remove Term")
        print("3. List Terms")
        print("4. Replace Shortcuts in Text")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            shortcut = input("Enter the shortcut: ")
            full_form = input("Enter the full form: ")
            mega_center.add_term(shortcut, full_form)
        elif choice == '2':
            shortcut = input("Enter the shortcut to remove: ")
            mega_center.remove_term(shortcut)
        elif choice == '3':
            mega_center.list_terms()
        elif choice == '4':
            text = input("Enter the text: ")
            print("Replaced Text: ", mega_center.replace_shortcuts(text))
        elif choice == '5':
            print("Exiting MegaCenter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()