# cityhash128-converter
Convert plaintext to cityhash-128 hash

```bash
git clone https://github.com/yottajunaid/cityhash128-converter.git
cd cityhash128-converter
pip install cityhash
python cityhasher.py
```

# Code
```bash
import cityhash

def main():
    print("ðŸ” CityHash128 Hasher")
    print("Enter text to hash (type 'exit' to quit):\n")

    while True:
        user_input = input("â–¶ Input: ").strip()
        if user_input.lower() == "exit":
            print("ðŸ‘‹ Exiting...")
            break
        if not user_input:
            print("âš  Please enter some text.")
            continue

        hash_128 = cityhash.CityHash128(user_input)
        hex_hash = f"{hash_128:032x}"
        print(f"â†’ CityHash128: {hex_hash}\n")

if __name__ == "__main__":
    main()
```
## Happy Encoding !!!
