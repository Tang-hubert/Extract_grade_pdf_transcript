# Extract Grade PDF Transcript

Extract grades by terms from different students using `pdfplumber`.

## Usage
1. Have a bunch of student transcripts (in PDF format).
2. Create an `output` folder.
3. Change `dir_path` in `scripts/main.py`.
4. Run `scripts/main.py`.

## Output
Two Excel files:
1. `result`: This file extracts data from transcripts.
2. `error_id`: Transcripts that couldn't be extracted and need to be filled manually.
    - Picture: PDFs containing transcripts in picture format that cannot be extracted using pdfplumber.
    - A0651R not in lines[0]: This category is for transcripts which are not in the format named `A0651R`, which is commonly used by most universities.
    - score_lines and total_lines both false: Transcripts with a strange format.
    - error: Errors occurred when running this code. They need to be checked manually.
