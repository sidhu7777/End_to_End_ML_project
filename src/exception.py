import sys
import logging

# Configure logging to capture the logs in the console
logging.basicConfig(level=logging.ERROR, format="[%(asctime)s] %(levelname)s - %(message)s")

def error_message_detail(error, error_detail: sys):
    """
    Generate detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    """
    Custom Exception class to include additional error message.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        # Deliberately cause an exception to test CustomException
        a = 1 / 0  # Division by zero will cause a ZeroDivisionError
    except Exception as e:
        logging.error("An error occurred", exc_info=True)  # Logs the error with traceback
        raise CustomException(str(e), sys)  # Raise the custom exception
