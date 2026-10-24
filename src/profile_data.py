"""Utilities for inspecting local RoadGuard datasets."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = PROJECT_ROOT / "data"


def list_data_files(root: Path = DATA_ROOT) -> list[dict]:
    """List dataset files without reading their contents."""
    results = []

    for path in root.rglob("*"):
        if path.is_file() and path.name != ".gitkeep":
            results.append(
                {
                    "name": path.name,
                    "extension": path.suffix.lower(),
                    "size_mb": round(path.stat().st_size / (1024 * 1024), 2),
                    "path": str(path.relative_to(PROJECT_ROOT)),
                }
            )

    return sorted(results, key=lambda item: item["path"].lower())


if __name__ == "__main__":
    files = list_data_files()

    if not files:
        print("No dataset files found inside the project's data folder.")
        print("Your original LTPP dataset can remain elsewhere on your PC.")
    else:
        for item in files:
            print(
                f"{item['path']} | {item['extension']} | "
                f"{item['size_mb']} MB"
            )
