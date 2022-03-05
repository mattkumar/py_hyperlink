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

# Data wrangle - compose html string:
# display text of the link comes from the column link (e.g. "a link")
# the target of the link comes from link_2 (e.g. "www.google.com")
my_table_data <- my_data %>%
  mutate(display_string = paste0('<a href="',link_2,'">',link,'</a>'))

# Test that html string is rendered and works when clicked
my_table_data %>%
  select(display_string) %>%
  reactable(.,
            defaultColDef = colDef(html = TRUE))