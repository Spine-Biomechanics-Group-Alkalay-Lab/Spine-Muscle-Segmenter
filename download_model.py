import os

def unite_zip(output_file, parts):
    """
    Combines the parts back into a single zip file.

    Args:
        output_file (str): Name of the output zip file.
        parts (list): List of part filenames in order.
    """
    print("Starting to unite the model parts...")
    with open(output_file, 'wb') as f:
        for part in parts:
            print(f"Processing: {part}")
            with open(part, 'rb') as part_file:
                f.write(part_file.read())
    print(f"Reuniting completed! Output file: {output_file}")

if __name__ == "__main__":
    folder = os.path.join("models", "v.0.0.1")
    parts = [
        os.path.join(folder, "nnU-Net_results-part1.zip"),
        os.path.join(folder, "nnU-Net_results-part2.zip"),
    ]

    output_file = os.path.join(folder, "nnU-Net_results.zip")
    unite_zip(output_file, parts)