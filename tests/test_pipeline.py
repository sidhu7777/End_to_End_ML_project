from src.pipeline.predict_pipeline import CustomData, PredictPipeline

try:
    # Create sample data
    data = CustomData(
        gender="male",
        race_ethnicity="group B",
        parental_level_of_education="bachelor's degree",
        lunch="standard",
        test_preparation_course="none",
        reading_score=85.0,
        writing_score=90.0
    )
    pred_df = data.get_data_as_data_frame()
    print("Input DataFrame:\n", pred_df)

    # Initialize prediction pipeline
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    print("Prediction Results:", results)
except Exception as e:
    print("Error:", e)
