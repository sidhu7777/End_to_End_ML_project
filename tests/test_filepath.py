import os

artifacts_dir = r"C:\Users\91832\Desktop\End_to_End _ML_Project\artifacts"
model_path = os.path.join(artifacts_dir, "model.pkl")
preprocessor_path = os.path.join(artifacts_dir, "preprocessor.pkl")

print("Model exists:", os.path.exists(model_path))
print("Preprocessor exists:", os.path.exists(preprocessor_path))
