# solution to selected exercises of R-part1.pdf
# Q. What type will be output of
typeof(x <- 1) #double
typeof(x+1)  #double
y <- 2020L
typeof(y)  #integer
typeof(as.numeric("1.7")*2) #double as "1.7" converted to double
"1.7" * 2 #gives error as "1.7" is char and not auto converted to numeric

# Q. Create a matrix with any continuous sequence of numbers of dimension 4x5
# Create a matrix of 2 x 3 with dimension names as r1,r2 and c1, c2,c3
# What is the output of the following:
# m1 <- matrix(3:20,3,8); m1
# m1 <- matrix(3:20,3,5); m1
# CHALLENGE: Try using paste function to construct the row and column names
# Create a matrix with a sequence of numbers arranged row-wise (row- major fashion)

m1 <- matrix(seq(1.2,4.1,0.15),4); m1 #second parameter indicates no. of rows
dimnames(m1) <- list(paste0('r',1:4),paste0('c',1:5)); m1
#below to get the arrangement in row-wise
m1 <- matrix(seq(1.2,4.1,0.15),4,byrow = TRUE); m1

# Q. Create 4 vectors of lengths 2,3,4 and 1 and 
# create a list with the two vectors as its two components with names
# Access the 2nd element of the 3rd vector 
# (i.e. 2nd element of the 3rd component of the list)
v1 <- letters[1:2]
v2 <- LETTERS[1:3]
v3 <- 1:4
v4 <- 1.2
l1 <- list(a=v1,b=v2,v3,v4); l1                     
l1[[3]][2]  #second element of 3rd vector
l1[[c(3,2)]]  #same as above
l1[[3]][[2]] #same as above
l1[['a']][2] #second element of 1st vector
l1[[1]][2]  #same as above
l1[c(3,2)] #accessing 3rd and 2nd element of the list in that order - single square bracket

# Q. Create a vector p <- c(0,3,2,2,1) and convert it into a factor
# CHALLENGE: Assign new levels to the factor using levels function and 
# assignment operation using the vector c(‘a’,’d’,’b’,’c’) & 
# check the contents of the factor (notice any changes?)
p <- c(0,3,2,2,1)
p_fac <- factor(p)
levels(p_fac) #check the levels of the new factor object created
p_fac_new_levels <- factor(p_fac,levels = levels(p_fac), 
                           labels = c('a','d','b','c'))
levels(p_fac_new_levels)
p_fac_new_levels
p_fac

# Again assign new levels to the factor of a sequence of 
# numbers in reverse sorted order (e.g. 10,9,8,7)
p <- 1:10
p_fac <- factor(p); levels(p_fac)
# step 1
levels(p_fac)
# step 2
as.numeric(levels(p_fac))
# step 3
sort(as.numeric(levels(p_fac)),decreasing = TRUE)
# all the steps together will give the solution as below
p_fac_new_levels <- factor(p_fac,
                           labels = sort(as.numeric(levels(p_fac)),
                                         decreasing = TRUE))
# verify solution
levels(p_fac_new_levels)
p_fac_new_levels

# Q. What is the output of
# v1 <-c('1','4','b') 
# as.numeric(v1[!is.na(as.integer(v1))]) 
# x <- c(10.4, 5.6, 3.1, 6.4, 21.7) 
# sum((x-mean(x))^2)/(length(x)-1) 
# (x+1)[(!is.na(x)) & x>0] -> z

v1 <-c('1','4','b')
# we break down the following expression into parts in order to understand it:
# as.numeric(v1[!is.na(as.integer(v1))]) 

# the following expression tries to convert elements of the vector into integer 
# which is success for 1st and 2nd element, 3rd gives NA
as.integer(v1) 
# checks for NA and hence gives a boolean vector
is.na(as.integer(v1))
# gives opposite of above due to negation operator
!is.na(as.integer(v1))
#since the above is a boolean vector of the same length as the original vector
# it can be used as an index vector inside the index operator - [ ]
# so only effectively only the number type elements are chosen
v1[!is.na(as.integer(v1))]
# the number type elements are successfully converted to number
as.numeric(v1[!is.na(as.integer(v1))]) 

# check output of each of the expression below to understand the
# the evaluation of sum((x-mean(x))^2)/(length(x)-1)
x <- c(10.4, 5.6, 3.1, 6.4, 21.7)
length(x)
length(x)-1
mean(x)
x-mean(x)
(x-mean(x))^2
sum((x-mean(x))^2)
sum((x-mean(x))^2)/(length(x)-1)

# (x+1)[(!is.na(x)) & x>0] -> z
is.na(x)
(!is.na(x))
x>0
(!is.na(x)) & x>0
x+1
(x+1)
(x+1)[(!is.na(x)) & x>0]  #[ ] indicates use of indexing operator
(x+1)[(!is.na(x)) & x>0] -> z  #assignment of LHS to RHS
z

# Compute the value and explain the precedence to yourself for the following:
#2+3^2
2+3^2 # equivalent to (==>) 2+(3^2) as ^ operator has higher precedence
2+3^2^3 # ==> 2+(3^(2^3))
x <- y <- z <- 0; x; y; z  # 0 assigned to z which is assigned to y and
                          # which in turn assigned to x)

3+3/2
2:3+2
2:-3 # ==> 2:(-3) 
2 > 2:-3 # ==> 2 > (2:-3)  # check list of operator precedence to verify

# solution to selected exercises of R-part2.pdf
# Q. Experiment with variations in write.table function (command) to get 
# the data in the orginal format as shown below:
tab1 <- read.table(file='house_copy.txt',header = T)
write.table(tab1,file = "new_file.txt") # or write.csv command
# the above plain write.csv will give text file as below:
#  "area" "sale.price" "availability" "region" "last.sale.date"
#  "1" 694 192 1 "N" "20/09/2021"
#  "2" 905 215 2 "W" "20/09/2021"
#  "3" 802 215 3 "S" "20/09/2021"
#  ...
#  ...
# the above output does not match the original text file contents so
# we need to modify the write.csv command appropriately as below:
write.table(tab1,'new_file.txt',quote = FALSE,row.names = FALSE)

# Answers to selected question from Assignment 1

# Q. WHat is the difference between the use of along.with and 
# length.out parameters of the seq function - 
# demonstrate with your own examples using a vector of characters.
v1 <- 3:10; v1
seq(1,along.with =v1 ) # creates a new vector starting at 1 of same length as v1
seq(1,by=0.5,length.out=10) # creates vector of length 10 with start as 1 and interval as 0.5

# Q. consider the following vector:
#  v1 <- c('a','b','c','a','c')
# generate another vector of same length which 
# have the value 2 in those positions where there is 'a' and 0 for others. 
# That is, output vector is 2 0 0 2 0
v1 <- c('a','b','c','a','c')
v2 <- factor(v1,labels = c(2,0,0)); v2

# Q. Create a matrix of 100 elements with 25 columns. 
# The elements are single characters such as 'a', 'b', etc. 
# Multiple elements of the matrix could be same value. 
# Create another smaller matrix from this character matrix 
# where only the elements which are neither 'a' nor 'b' 
# from the original matrix are chosen. 
# The new matrix should have the number of rows as a fraction 
# of total number of elements extracted from the original matrix. 
# For example if only 30 elements are extracted from original matrix 
# then the new matrix could have 15 rows (approx a fraction 1/2). 
# Attempt to create the second matrix in a single expression. 
# You may start by using multiple steps then attempt to combine them together.

#Example:
#  From 
# a b c f
# b d e f 

# the elements c,f,d,e,f are selected and a 
# matrix with these elements are created having 5/2 rows i.e. 
# 2 rows so something like this would be created
# d e f
# c f d

m1 <- matrix(rep(letters[1:25],4), ncol=25); m1
m1.index.vector <- !(m1 %in% c('a','b'))
l1 <- length(m1.index.vector)
m2 <- matrix(m1[m1.index.vector],ncol=l1/10); m2

# Q. Using the character sub-matrix (smaller matrix) created in the earlier
# question convert it into a numeric matrix. Attempt the answer without doing
# individual character by character conversion as there could be a large 
# number of different characters in the sub-matrix to be attempted 
# individually. (Hint: try applying the concept of factor). 
# Remember the result matrix should have the same structure as the character sub-matrix.
# Example:
  
#  The above character submatrix would produce something like this:
#  1 2 3
# 4 3 1

v3 <- as.numeric(factor(m2)); v3
m3 <- matrix(v3,nrow = dim(m2)[1]); m3 #dim(m2) gives the dimension of matrix as a vector
m4 <- m3+9; m4
m4 <- matrix(v3,nrow = dim(m2)[1]) + 9; m4
