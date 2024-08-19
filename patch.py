def main():
    """Hello! This script take in a valid value, and uses it to patch the
    executable, overwriting the value of 'x'. This was possible through
    the use of tools like Ghidra, not only to find the exact byte that
    stores the value of 'x', but also the offset thats leads straight to
    it as well."""
    
    input_value: str = input("Enter a number between 0-255: ")

    try:
        value = int(input_value)
        if (value > 255):
            value = 255
    except ValueError:
        value = 0

    patch: bytes = value.to_bytes()
    print(f"Value: {value}")
    print(f"Byte Value: {patch}")

    with open("reverse2.exe", 'r+b') as file:
        # Byte Offset: 0xA5D
        file.seek(0xA5D+3)

        file.write(patch)

    print("Patch has been applied.")


if __name__ == "__main__":
    main()

