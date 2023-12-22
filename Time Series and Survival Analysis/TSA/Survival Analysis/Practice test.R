# Loading the required libraries

library(survival)
library(MASS)
library(fitdistrplus)
library(survminer)
library(ggfortify)

# Loading the dataset in R

dataset= read.csv('haberman_survival.csv',header = T)

#Knowing the dataset
head(dataset,4)     # for getting the head part of the dataset
names(dataset)      # for the coloumn names in the dataset
summary(dataset)    # five point summary of the dataset
sum(is.na(dataset)) # checking for na values in the dataset
str(dataset)        # structure of the dataset

# Changing the coloumn names of the dataset
colnames(dataset)=c('Age','OP_year','axil_nodes','status')
names(dataset)
head(dataset)

#Recoding variables in the status coloumn of the dataset
dataset$status=ifelse(dataset$status==2,1,0)
dataset$status

#Creating the survival object 
survobject= Surv(dataset$OP_year,dataset$status)

# Estimating the survival function using the non parametric method kaplan Meir 
fit_data_KM=survfit(survobject~2,data = dataset,stype = 1)    #direct way of estimating the survival function kaplan Meir
summary(fit_data_KM)
plot(fit_data_KM)
