import numpy as np
import pandas as pd

from regression_model.processing.data_management import load_pipeline
from regression_model.config import config
from regression_model.processing.validation import validate_inputs
from regression_model import __version__ as _version

from io import StringIO
import logging


_logger = logging.getLogger(__name__)

pipeline_file_name = "regression_model.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""
    print(" ---CALL make_prediction() --- ")
    data = pd.read_json(StringIO(input_data))

    #prediction = _price_pipe.predict(data[config.FEATURES])
    validated_data = validate_inputs(input_data=data)
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = np.exp(prediction)
    #response = {"predictions": output}
    results = {"predictions": output, "version": _version}
    _logger.info(
        f"Making predictions with model version: {_version} "
        f"Inputs: {validated_data} "
        f"Predictions: {results}"
    )
    #return response
    return results
