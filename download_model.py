import os
import requests
from tqdm import tqdm  # make sure to install: pip install tqdm

def download_file(url, dest):
    """Download a file from a URL to a local path with a progress bar."""
    if not os.path.exists(dest):
        print(f"Downloading {url} → {dest}")
        r = requests.get(url, stream=True)
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        chunk_size = 100000000
        with open(dest, "wb") as f, tqdm(
            total=total_size, unit='B', unit_scale=True, desc=os.path.basename(dest)
        ) as bar:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                bar.update(len(chunk))
        print(f"Finished downloading {dest}")
    else:
        print(f"{dest} already exists, skipping download.")

def unite_zip(output_file, parts):
    """
    Combines the parts back into a single zip file.
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
    os.makedirs(folder, exist_ok=True)

    # URLs of your GitHub release assets
    urls = [
        "https://github.com/Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter/releases/download/weight/nnU-Net_results-part1.zip",
        "https://github.com/Spine-Biomechanics-Group-Alkalay-Lab/Spine-Muscle-Segmenter/releases/download/weight/nnU-Net_results-part2.zip",
    ]

    parts = []
    for url in urls:
        filename = os.path.join(folder, os.path.basename(url))
        download_file(url, filename)
        parts.append(filename)

    output_file = os.path.join(folder, "nnU-Net_results.zip")
    unite_zip(output_file, parts)
