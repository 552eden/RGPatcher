import sys

def replace_bytes_in_file(input_file_path, output_file_path, old_bytes, new_bytes):
    try:
        with open(input_file_path, 'rb') as file:
            file_data = file.read()

        old_bytes = bytes.fromhex(old_bytes)
        new_bytes = bytes.fromhex(new_bytes)

        if new_bytes in file_data:
            print("File already patched!")
            return
        
        if old_bytes not in file_data:
            print("Couldn't find wrong value to patch. Please make sure this is an RGLoader image (17489 or 17559) and that it includes HvxPeekPoke.s")
            return
        

        modified_data = file_data.replace(old_bytes, new_bytes)

        with open(output_file_path, 'wb') as file:
            file.write(modified_data)

        print("RGLoader image patched successfully.")
    except IOError as e:
        print(f"An error occurred while handling the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python RGPatcher.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    old_bytes = "2B04000441990094419A004438A0154C"
    new_bytes = "2B04000441990094419A004438A015F0"

    replace_bytes_in_file(input_file_path, output_file_path, old_bytes, new_bytes)