import base64 as bs


def encode_file(input_file, output_file):
    with open(input_file, "rb") as file:
        data = file.read()

    encoded_data = bs.b64encode(data)
    with open(output_file, "wb") as file:
        file.write(encoded_data)
    return output_file


def decode_file(input_file, output_file):
    with open(input_file, "rb") as file:
        encoded_data = file.read()

    decoded_data = bs.b64decode(encoded_data, validate=True)
    with open(output_file, "wb") as file:
        file.write(decoded_data)
    return output_file


def main():
    print("=" * 50)
    print("        BASE64 - FILE ENCODER | DECODER")
    print("=" * 50)
    while True:
        print("\n[1] Encode")
        print("[2] Decode")
        print("[3] Exit")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            input_file = input("Enter File Path: ").strip()
            output_file = input("Enter Output File Name (Include Extension): ").strip()
            try:
                result = encode_file(input_file, output_file)
                print(f"File encoded successfully: {result}")
            except FileNotFoundError:
                print("Error: Input file not found.")
            except Exception as e:  # noqa: BLE001
                print(f"Error: {e}")

        elif choice == "2":
            encoded_file = input("Enter Encoded Base64 File Path: ").strip()
            output_file = input("Enter New File Name (Include Extension): ").strip()
            try:
                result = decode_file(encoded_file, output_file)
                print(f"File decoded successfully: {result}")
            except FileNotFoundError:
                print("Error: Input file not found.")
            except Exception as e:  # noqa: BLE001
                print(f"Error: {e}")

        elif choice == "3":
            print("\nExiting.... See You Soon....")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
