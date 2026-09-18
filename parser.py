import argparse
import base64 as bs


def encode_file(input_file, output_file):
    with open(input_file, "rb") as file:
        data = file.read()

    encoded_data = bs.b64encode(data)
    with open(output_file, "wb") as file:
        file.write(encoded_data)

    print(f"File encoded successfully: {output_file}")


def decode_file(input_file, output_file):
    with open(input_file, "rb") as file:
        encoded_data = file.read()

    decoded_data = bs.b64decode(encoded_data, validate=True)
    with open(output_file, "wb") as file:
        file.write(decoded_data)

    print(f"File decoded successfully: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Base64 File Encoder and Decoder CLI Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-e",
        "--enc",
        "--encode",
        dest="encode",
        metavar="FILE",
        help="Encode a file into Base64",
    )
    group.add_argument(
        "-d",
        "--dec",
        "--decode",
        dest="decode",
        metavar="FILE",
        help="Decode a Base64 file",
    )
    parser.add_argument(
        "-o",
        "--out",
        "--output",
        dest="output",
        required=True,
        metavar="FILE",
        help="Output file path",
    )
    args = parser.parse_args()

    if args.encode and args.encode == args.output:
        parser.error("Input and output files cannot be the same.")

    if args.decode and args.decode == args.output:
        parser.error("Input and output files cannot be the same.")

    if args.encode:
        try:
            encode_file(args.encode, args.output)
        except FileNotFoundError:
            print(f"Error: File not found: {args.encode}")
        except Exception as e:  # noqa: BLE001
            print(f"Error: {e}")

    elif args.decode:
        try:
            decode_file(args.decode, args.output)
        except FileNotFoundError:
            print(f"Error: File not found: {args.decode}")
        except bs.binascii.Error: # type: ignore
            print("Error: Invalid Base64 file.")
        except Exception as e:  # noqa: BLE001
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
