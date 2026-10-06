import logging

logger = logging.getLogger(__name__)

def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # TODO 2:
    # Check if any of the configured columns (list) are missing from df.
    # If any are missing, log an ERROR and raise ValueError.
    # Log an INFO.
    # Return the DataFrame.
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column {col} missing")
    logger.info("All required columns exist")
    return df