# Libs
library(reticulate)
library(tidyverse)
library(janitor)
library(reactable) 

# Load python function
reticulate::source_python("python/get_hyperlink.py")

# Use python function on a data source
my_data<- get_hyperlink("data/input.xlsx")

# Data clean up
my_data <- my_data %>%
  row_to_names(row_number = 1) %>%
  clean_names()  

# Compose html string: <a href = link2>link</a>
my_table_data <- my_data %>%
  mutate(display_string = paste0('<a href="',link_2,'">',link,'</a>'))  

# Render html string in a table, check that it works on click
my_table_data %>%
  select(display_string) %>%
  reactable(.,
            defaultColDef = colDef(html = TRUE))