# Libs
library(reticulate)
library(tidyverse)
library(janitor)
library(reactable) 

# Load python function
reticulate::source_python("python/get_hyperlink.py")

# Use the custom python function on a workbook
my_data <- get_hyperlink(path = "data/input.xlsx",
                         sheet = "Sheet1")

# Compose html string: <a href = link target>link text</a>
my_table_data <- my_data %>%
  clean_names() %>%
  mutate(display_string = paste0('<a href="',link,'">','View','</a>'))  

# Render html string in a table, check that it works on click
my_table_data %>%
  select(display_string) %>%
  reactable(.,
            defaultColDef = colDef(html = TRUE))


 