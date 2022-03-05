# Background
Currently, no R package or function exists for extracting hyperlink values from excel files. There is a python solution to this problem using the `openpyxl` library. The aim is to leverage this python package within an R-based workflow seamlessly via `reticulate`.

## Requirements

1. Install `reticulate` 

2. Install python on your machine. You can use `reticulate::install_miniconda` to do this for you if you haven't an installation.

3. Install the `openpyxl` package in python via `reticulate::py_install('openpyxl')` 

4. Install the `pandas` package in python via `reticulate::py_install('pandas')` 

5. Follow the steps in `workflow.R` to use the custom python function I've written


## Example


```
library(reticulate)
library(tidyverse)

reticulate::source_python("python/get_hyperlink.py")

my_data<- get_hyperlink(path = "data/input.xlsx",
                        sheet = "Sheet1",
                        source_col = 2,
                        target_col = 3)
                        
head(my_data)
```
