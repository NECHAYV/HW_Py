import csv
import pandas as pd
from typing import List, Dict, Union, Optional
from pathlib import Path


def read_csv(
        file_path: str,
        delimiter: str = ";",
        use_pandas: bool = False
) -> List[Dict]:

    if not Path(file_path).exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")

    if use_pandas:
        try:
            df = pd.read_csv(file_path, delimiter=delimiter)
            return df.to_dict('records')
        except Exception as e:
            raise ValueError(f"Pandas CSV read error: {str(e)}")
    else:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=delimiter)
                return [row for row in reader]
        except csv.Error as e:
            raise ValueError(f"CSV read error: {str(e)}")


def write_csv(
        file_path: str,
        data: List[Dict],
        delimiter: str = ";",
        use_pandas: bool = False
) -> None:

    if use_pandas:
        try:
            df = pd.DataFrame(data)
            df.to_csv(file_path, sep=delimiter, index=False)
        except Exception as e:
            raise ValueError(f"Pandas CSV write error: {str(e)}")
    else:
        try:
            with open(file_path, 'w', encoding='utf-8', newline='') as file:
                if not data:
                    return

                writer = csv.DictWriter(
                    file,
                    fieldnames=data[0].keys(),
                    delimiter=delimiter
                )
                writer.writeheader()
                writer.writerows(data)
        except csv.Error as e:
            raise ValueError(f"CSV write error: {str(e)}")


def read_excel(
        file_path: str,
        sheet_name: Optional[Union[str, int]] = None
) -> List[Dict]:

    if not Path(file_path).exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")

    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)


        if isinstance(df, dict):
            df = next(iter(df.values()))

        return df.to_dict('records')
    except Exception as e:
        raise ValueError(f"Excel read error: {str(e)}")


def write_excel(
        file_path: str,
        data: List[Dict],
        sheet_name: str = "Sheet1"
) -> None:

    try:
        df = pd.DataFrame(data)
        df.to_excel(file_path, sheet_name=sheet_name, index=False)
    except Exception as e:
        raise ValueError(f"Excel write error: {str(e)}")