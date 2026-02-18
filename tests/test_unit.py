import pandas as pd
from src.pipeline.predict_pipeline import CustomData


def test_custom_data_dataframe_creation():
    """
    Test that CustomData correctly converts input into a pandas DataFrame
    with expected structure.
    """

    data = CustomData(
        gender="male",
        race_ethnicity="group A",
        parental_level_of_education="bachelor's degree",
        lunch="standard",
        test_preparation_course="none",
        reading_score=72,
        writing_score=74,
    )

    df = data.get_data_as_data_frame()

    # Check object type
    assert isinstance(df, pd.DataFrame)

    # Check shape (1 row, 7 columns)
    assert df.shape == (1, 7)

    # Check expected columns
    expected_columns = [
        "gender",
        "race_ethnicity",
        "parental_level_of_education",
        "lunch",
        "test_preparation_course",
        "reading_score",
        "writing_score",
    ]

    assert list(df.columns) == expected_columns

    # Check values
    assert df.loc[0, "gender"] == "male"
    assert df.loc[0, "reading_score"] == 72
    assert df.loc[0, "writing_score"] == 74
