#################################################################
#---------------- Scatter Plot of Tree Data --------------------#
DataTree=trees
Diameter=DataTree[,1]     # inch (at 54 inches above ground)
Height=DataTree[,2]       # ft
Volume=DataTree[,3]       # cubic ft
par(mfrow=c(1,2))         # set the plotting area into a 1*2 array
plot(Height,Volume,title('Figure 1a'))
plot(Diameter,Volume,title('Figure 1b'))
cov(Height,Volume)
cov(Diameter,Volume)
#################################################################
#---------- Scatter Plot at different correlation --------------#
library('mvtnorm')
ArrayOfRho=seq(-1,1,by=.25)
x1=seq(-2,2,.05)
x2=seq(-2,2,.05)
Mu1=0; S1=1
Mu2=0; S2=1
Grid=expand.grid(x1, x2) 
par(mfrow=c(3,3))
sample_size=40
Mu=rbind(Mu1,Mu2)
for(i in 1:9)
{
  CovarianceMatrix=matrix(c(S1,sqrt(S1*S2)*ArrayOfRho[i],sqrt(S1*S2)*ArrayOfRho[i],S2),2)
  z=rmvnorm(sample_size, Mu, CovarianceMatrix) #Generating multivariate normal
  plot(z[,1],z[,2],main=paste("Correlation ",ArrayOfRho[i]),
     xlab="X1", ylab="X2",xlim=c(-4, 4), ylim=c(-4,4))  #Scatter plot of bivariate normal
}
mtext('Figure 2', outer=TRUE,  cex=1, line=-1.25)
#################################################################
#----------- Pearson's Correlation of Tree Data ----------------#
cor(Diameter,Volume)
cor(Height,Volume)
cor(DataTree)
library(corrplot)
par(mfrow=c(1,1));corrplot(cor(DataTree));mtext('Figure 3', outer=TRUE,  cex=1.5, line=-1.25)
cor.test(Diameter,Volume)
cor.test(Height,Volume)
#################################################################
#-------- Pearson's Sensitivity and Rank Correlation -----------#
#################################################################
#------------------- Nonlinear Relationship --------------------#
x=seq(0,1,.01);y=x^4              # Non-linear relation
par(mfrow=c(1,1));plot(x,y)
cor(x,y)                          # Pearson
cor(x,y,method = 'spearm')        # Spearman
cor(x,y,method = 'kendall')       # Kendall
#----------------------- Sensitiveness -------------------------#
x=seq(0,1,.01);y=x                # Linear relation
y[length(y)]=10                   # Outlier
cor(x,y)
cor(x,y,method = 'spearm')
cor(x,y,method = 'kendall')
#################################################################
#--------------- Excell Example Data with Tie ------------------#
x=c(6,27,46,30,28,30,15,18,24,32,22,34,24,4,25,38,50,6)
y=c(4,8,8,14,15,9,11,9,6,9,13,10,7,9,5,11,12,4)
cor(x,y)                    # Pearson's Correlation of Excell Data
cor(x,y,method = 'spearm')  # Spearman's Correlation of Excell Data 
cor(x,y,method = 'kendall') # Kendall's Correlation of Excell Data 
#################################################################
#----------- Spearman's Correlation of Tree Data ---------------#
cor.test(Diameter,Volume,method = 'spearm')
cor.test(Height,Volume,method = 'spearm')
#------------ Kendall's Correlation of Tree Data ---------------#
cor.test(Diameter,Volume,method = 'kendall')
cor.test(Height,Volume,method = 'kendall')
