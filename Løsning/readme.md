# Projektbeskrivelse

Dette projekt er et Python-baseret værktøj til download og validering af PDF-filer angivet in en GRI-excel-fil og skrive resultatet til en MetaData-excel-fil. Appliktionen bruger Asyncio og aiohttp til at håndtere de mange filhentninger asykront.


## Installation

1. Klon dette repository til din lokale maskine.
2. Sørg for at have Python 3.12 og pipenv installeret.
3. Installer de nødvendige pakker ved at køre:
    ```sh
   pipenv install
   ```

## Brug

1. Konfigurer de nødvendige indstillinger i `config.py`.
2. Aktiver det virtuelle miljø ved at køre:
    ```sh
    pipenv shell
    ```
2. Kør `main.py` for at starte processen.

## Projektstruktur

### `config.py`

- `Config`: En enum-klasse, der definerer forskellige konfigurationsindstillinger som filstier, kolonnenavne og værdier.

### `downloader.py`

- `Downloader`: En klasse, der indeholder metoder til at downloade filer og validere dem.
  - `download_file(url)`: Downloader en fil fra en given URL.
  - `download_row(row)`: Downloader en fil baseret på en række fra en pandas DataFrame og validerer den.

### `excel.py`

- `Excel`: En klasse, der håndterer læsning og skrivning af Excel-filer.
  - `read_excel()`: Læser en Excel-fil og returnerer en DataFrame.
  - `write_file(new_file_path)`: Skriver DataFrame til en Excel-fil.

### `main.py`

- `download_row(i, row)`: Asynkron funktion, der downloader en række og opdaterer metadata.
- `main()`: Hovedfunktionen, der styrer hele downloadprocessen.

### `pdf_validater.py`

- `PdfValidater`: En klasse, der bruger PyPDF2 til at validere PDF-filer.

## Afhængigheder

Projektet bruger følgende Python-pakker:
- `pandas`: Et kraftfuldt dataanalyseværktøj, der gør det nemt at arbejde med strukturerede data.
- `openpyxl`: En pakke til at læse og skrive Excel 2010 xlsx/xlsm/xltx/xltm filer.
- `pypdf2`: Et rent Python-bibliotek til at arbejde med PDF-filer.
- `aiohttp`: En asynkron HTTP-klient/server framework til Python.

