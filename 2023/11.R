file <- "data/final11_1"

# Reading file
con <- file(file,"r")
first_line <- readLines(con,n=1)
close(con)
len <- nchar(first_line)

mat <- read.fwf(file, widths = rep(1, len), comment.char = "")

# Binary
mat <- ifelse(mat == '#', 1, 0)

# What to expand
rows_no_galax <- which(rowSums(mat) == 0)
cols_no_galax <- which(colSums(mat) == 0)

# Manhattan distance
dist <- function(x1, y1, x2, y2){

  expanded_rows <- sum(rows_no_galax > min(x1, x2) & rows_no_galax < max(x1, x2))
  expanded_cols <- sum(cols_no_galax > min(y1, y2) & cols_no_galax < max(y1, y2))
  
  # First
  #manhattan <- (abs(x1-x2)+expanded_rows) + (abs(y1-y2)+expanded_cols)
  # Second
  manhattan <- (abs(x1-x2)+expanded_rows*999999) + (abs(y1-y2)+expanded_cols*999999)
  return(manhattan)
}

mat_id <- as.matrix(ifelse(mat == 1, 1:(nrow(mat) * ncol(mat)), 0))

pairs <- combn(which(mat == 1), 2)

dd <- apply(pairs, 2, function(x)
  dist(which(apply(mat_id == x[1], 1, any)), which(apply(mat_id == x[1], 2, any)),
       which(apply(mat_id == x[2], 1, any)), which(apply(mat_id == x[2], 2, any)))
)
sum(dd)

