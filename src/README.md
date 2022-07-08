# `src` package overview

All functions for this project, are stored in this folder. All tests are
stored in the `tests` folder, which is one-level above this folder in the main project
directory.

The sub-folders should be used as follows:

- `dao`: data access functions
- `data`: data processing-related functions
- `features`: feature-related functions, for example, functions to create features
  from processed data
- `models`: model-related functions
- `visualizations`: functions to produce visualizations
- `utils`: utility functions that are helpful in the project

Main functions are imported in the `src/__init__.py` script.