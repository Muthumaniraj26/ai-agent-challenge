# test_parser.py
import pandas as pd
import pytest
from custom_parsers.icici_parser import parse

def test_icici_parser_output():
    pdf_path = r"data\icici\icici_sample.pdf"
    expected_csv_path = r"data\icici\icici_sample.csv"

    expected_df = pd.read_csv(expected_csv_path)
    actual_df = parse(pdf_path)

    try:
        pd.testing.assert_frame_equal(actual_df, expected_df)
    except AssertionError as e:
        pytest.fail(f"The parsed DataFrame does not match the expected CSV.\nDetails: {e}")