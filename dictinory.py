import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Word not found. Please try again.")
        return

    data = response.json()
    meanings = data[0].get("meanings", [])

    print(f"\n📘 Definitions for: *{word}*")
    for meaning in meanings:
        part_of_speech = meaning.get("partOfSpeech", "unknown")
        print(f"\nPart of Speech: {part_of_speech}")
        for idx, definition in enumerate(meaning["definitions"], 1):
            print(f"{idx}. {definition['definition']}")
            if 'example' in definition:
                print(f"   e.g. {definition['example']}")


def main():
    print("=== Dictionary App ===")
    while True:
        word = input("\nEnter a word (or 'exit' to quit): ").strip()
        if word.lower() == "exit":
            print("Goodbye!")
            break
        get_definition(word)

if __name__ == "__main__":
    main()

