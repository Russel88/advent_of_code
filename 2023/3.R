library(mmand)

file <- "data/final3_1"

# Reading file
con <- file(file,"r")
first_line <- readLines(con,n=1)
close(con)
len <- nchar(first_line)

mat <- read.fwf(file, widths = rep(1, len), comment.char = "")

# Find the numbers in the array
mat_isnumber <- apply(mat, c(1,2), function(x) grepl("^[[:digit:]]",x))
number_clusters <- components(mat_isnumber, kernel = shapeKernel(c(1,3)))
number_clusters[is.na(number_clusters)] <- -1

# First
mat_symbol <- mat != "." & !mat_isnumber

## We dilate to get anything next to a symbol
symbol_dilate <- dilate(mat_symbol, kernel = shapeKernel(c(3,3), type = "box")) == 1

## Find number clusters in the symbol dilation
to_keep <- unique(as.numeric(number_clusters * symbol_dilate))
to_keep <- to_keep[!to_keep %in% c(-1, 0)]

## Extract the actual numbers
numbers_final <- sapply(to_keep, function(x) as.numeric(paste(as.numeric(mat[number_clusters == x]), collapse = "")))

sum(numbers_final)

# Second
mat_symbol <- mat == "*"

## We denote each asteriks with a unique number
symbol_clusters <- components(mat_symbol, kernel = shapeKernel(c(3,3)))

## We dilate to get the neighborhood
symbol_dilate <- dilate(symbol_clusters, kernel = shapeKernel(c(3,3), type = "box"))

## Find each unique asteriks ID
to_keep <- unique(as.numeric(symbol_dilate))
to_keep <- to_keep[!to_keep %in% c(-Inf)]

gear_ratio <- function(nn, ss, this){
  ## Find the number clusters within the dilation of a unique asteriks ID
  clusters <- unique(nn[ss == this][nn[ss == this] != -1])
  
  ## Only save information if there are two numbers in the neighborhood
  if(length(clusters) == 2){
    ## Get the actual numbers of the number clusters and return product
    n1 <- as.numeric(paste(as.numeric(mat[nn == clusters[1]]), collapse = ""))
    n2 <- as.numeric(paste(as.numeric(mat[nn == clusters[2]]), collapse = ""))
    return(n1 * n2)
  } else {
    return(0)
  }
}

numbers <- sapply(to_keep, function(x) gear_ratio(number_clusters, symbol_dilate, this = x))

sum(numbers)
