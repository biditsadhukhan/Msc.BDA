# =======================================================
# Principal Components Analysis
# Problem 8.1
# =======================================================

# Principal Component Calculation from Covariance Matrix
CovMat<-matrix(c(1,-2,0,-2,5,0,0,0,2),3,3)  # Cov(X)
r<-eigen(CovMat)
v<-r$vectors        # v=[e1:e2:...:eP]
# Rotational Matrix Y=XA'
A=t(v)
# Variance explained by Principal Component
lam<-r$values
PrnCovMat<-t(v)%*%CovMat%*%v                # Cov(Y) 
# Correlation of different Variables (Xs) on Principal Component (Ys)
CorrBetYandX<-t(v)%*%CovMat/(sqrt(lam)%o%sqrt(diag(CovMat)))

#########################################################
# Principal Component Calculation from Data
# Problem 8.4
# Load the dataset and convert to dataframe
#########################################################
library(Flury)
data(turtles)
str(turtles)
# Remove Factor variables and the Response variable
# Convert dataframe to matrix and check dimensions
turtlesMat<-as.matrix(turtles[,-c(1)])
dim(turtlesMat)
# Extract Male part of turtle data
turtlesMat<-turtlesMat[1:24,]
dim(turtlesMat)
# Transform to log scle
lgTurtlesMat<-log(turtlesMat)
##################################################
# Rotational Vectors for principal component are
# eigenvector of sample covariance matrix
##################################################
# We will find its Sample Mean and Sample Variance
sampleMeanlgTurtles<-colMeans(lgTurtlesMat)
sampleVariancelgTurtles<-var(lgTurtlesMat)
eigSampleVariancelgTurtles<-eigen(sampleVariancelgTurtles)
print(eigSampleVariancelgTurtles)
# We will do the Principal Component Analysis by "prcomp" method
lgTurtlesPCA <- prcomp(lgTurtlesMat)
print(lgTurtlesPCA)
pcaVariance=(lgTurtlesPCA$sdev)^2
print(pcaVariance)
plot(pcaVariance,type="b")
cumPercentage=100*(cumsum(pcaVariance))/sum(pcaVariance)
print(cumPercentage)
biplot(lgTurtlesPCA)
#########################################################
# Another Data Set
# Problem 8.5
#########################################################
Stock<-read.csv("Stock Price Data.csv", header=F)
StockMat<-as.matrix(Stock)
#########################################################################
# # Standerdizing the data
# n<-nrow(StockMat)
# p<-ncol(StockMat)
# StockMean<-colMeans(StockMat)
# DHalf<-sqrt((diag(var(StockMat))))
# StdStockMat<-(StockMat-t(matrix(rep(StockMean,n),p,n)))/t(matrix(rep(DHalf,n),p,n))
# # Variance of Standarized Data and Correlation of Original Data are same 
# StdStockMatVar=var(StdStockMat)
#########################################################################
StockMatCor=cor(StockMat)   #Correlation Matrix
print(StockMatCor)
# We will do the Principal Component Analysis by "prcomp" method
StockMatPCA <- prcomp(StockMat,center = TRUE,scale. = TRUE)   #PCA on standardized data by centering and scaling
print(StockMatPCA)
StockMatPcaVariance=(StockMatPCA$sdev)^2    #Eigen Values of correlation matrix
print(StockMatPcaVariance)
plot(StockMatPcaVariance,type="b")
cumPercentage=100*(cumsum(StockMatPcaVariance))/sum(StockMatPcaVariance)
print(cumPercentage)

#########################################################################
dataMat=matrix(c(26.4,13.2,6.25,2.19,1.26,2.85,2.86,9.58,23,15,7.05,2.6,1.44,3.15,2.69,9.65,34.9,20.6,9.64,3.74,1.73,4.21,2.5,8.42,34.2,19.8,9.1,3.68,1.89,4.2,2.47,9.45,27.5,16.2,7.27,3.15,1.44,3.43,2.3,8.96,26.3,14.5,6.39,3.04,1.87,3.01,2.09,12.8,25,14.6,6.35,3.14,1.25,3.33,2.02,8.55),byrow = TRUE, nrow = 8,ncol=7)
print(dataMat)
dataMatPCA=prcomp(dataMat,center = TRUE,scale. = TRUE)
print(dataMatPCA)      # The rotation gives the values of the eigen vectors that is the e's
pc1=dataMatPCA$x[,1]   # This gives the principal component e1`X 
pc2=dataMatPCA$x[,2]
dataMatPcaVariance=(dataMatPCA$sdev)^2    #Eigen Values of correlation matrix
print(dataMatPcaVariance)
Percentage=round(100*((dataMatPcaVariance))/sum(dataMatPcaVariance),2)
print(Percentage)
cumPercentage=100*(cumsum(dataMatPcaVariance))/sum(dataMatPcaVariance)
print(cumPercentage)
plot(dataMatPcaVariance,type = 'b')                  #Scree plot
plot(pc1,pc2,xlab=paste(c('PC axis 1',' ( ',Percentage[1],'% )'), collapse=''), ylab=paste(c('PC axis 2',' ( ',Percentage[2],'% )'), collapse=''), xlim=c(min(pc1)-.1*abs(min(pc1)), max(pc1)+.1*abs(max(pc1))), ylim=c(min(pc2)-.1*abs(min(pc2)), max(pc2)+.1*abs(max(pc2))))
names1 = c("1","2","3","4","5","6","7")
text(pc1,pc2,labels=names1,adj = c(0.3,-.8))

biplot(dataMatPCA)
f1<-dataMatPCA$sdev[1]*dataMatPCA$rotation[,1]
f2<-dataMatPCA$sdev[2]*dataMatPCA$rotation[,2]

plot(f1,f2,xlab="Factor 1", ylab="Factor 2",
     xlim=c(min(f1)-.1*abs(min(f1)), max(f1)+.1*abs(max(f1))), ylim=c(min(f2)-.1*abs(min(f2)), max(f2)+.1*abs(max(f2))))
names2 = c("A","B","C","D","E","F","G","H")
text(f1,f2,labels=names2,adj = c(0.3,-.8))

factanal(dataMat[,-c(3,4)],2)

