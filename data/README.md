# `data` folder overview

Any data that needs to be stored locally is saved in this location.

The sub-folders should be used as follows:

- `raw`: any raw data before any processing;
- `processed`: any raw data that has been fully processed into its final
  state.

The paths for these directories are loaded as environment variables written in `.env`. 
To load them in Python, use any or all of the following code:

```python
import os

# Load environment variables for the `data` folder, and its sub-folders
DIR_DATA = os.getenv("DIR_DATA")
DIR_DATA_EXTERNAL = os.getenv("DIR_DATA_EXTERNAL")
DIR_DATA_RAW = os.getenv("DIR_DATA_RAW")
DIR_DATA_INTERIM = os.getenv("DIR_DATA_INTERIM")
DIR_DATA_PROCESSED = os.getenv("DIR_DATA_PROCESSED")
```