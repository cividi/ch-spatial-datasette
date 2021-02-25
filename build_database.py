import json
from pathlib import Path
import sqlite_utils
import csv

base_path = (Path(__file__) / "..").resolve()
ch_data_base = base_path / "ch-data"

EXTRA_CSVS = [
    # file_path, table_name
]

# TODO: load from Data Package

def load_municipalities():
    daily_reports = list(
        (ch_data_base).glob(
            "*.csv"
        )
    )
    for filepath in daily_reports:
        with filepath.open() as fp:
            for row in csv.DictReader(fp):
                province_or_state = (
                    row.get("gemeinde.NAME")
                    or None
                )
                country_or_region = row.get("Country_Region") or row.get(
                    "kanton.NAME"
                )
                yield {
                    "number": row.get("gemeinde.BFS_NUMMER") or None,
                    "canton": country_or_region.strip(),
                    "town": province_or_state.strip(),
                    "latitude": row.get("Latitude") or row.get("Lat") or None,
                    "longitude": row.get("Longitude") or row.get("Long_") or None,
                }


def load_csv(filepath):
    with filepath.open() as fp:
        for row in csv.DictReader(fp):
            for key in row:
                if row[key].isdigit():
                    # Convert integers
                    row[key] = int(row[key])
                else:
                    try:
                        float(row[key])
                    except ValueError:
                        pass
                    else:
                        # Convert floats
                        row[key] = float(row[key])
            yield row


if __name__ == "__main__":
    db = sqlite_utils.Database(base_path / "cividi.db")

    table = db["ch_municipalities"]
    if table.exists():
        table.drop()
    table.insert_all(load_municipalities(), alter=True)
    table.create_index(["number"], if_not_exists=True)
    table.create_index(["canton"], if_not_exists=True)
    table.create_index(["town"], if_not_exists=True)

    # Add a view
    if "municipalities" in db.table_names():
        db["municipalities"].drop()

    if "municipalities" not in db.view_names():
        db.create_view(
            "municipalities", "select * from ch_municipalities"
        )
