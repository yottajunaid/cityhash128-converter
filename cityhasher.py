import cityhash

def main():
    print("🔐 CityHash128 Hasher")
    print("Enter text to hash (type 'exit' to quit):\n")

    while True:
        user_input = input("▶ Input: ").strip()
        if user_input.lower() == "exit":
            print("👋 Exiting...")
            break
        if not user_input:
            print("⚠ Please enter some text.")
            continue

        hash_128 = cityhash.CityHash128(user_input)
        hex_hash = f"{hash_128:032x}"
        print(f"→ CityHash128: {hex_hash}\n")

if __name__ == "__main__":
    main()
