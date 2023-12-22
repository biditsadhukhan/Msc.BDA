#########################################################################
#########################################################################
#                       Data Summary in R [6]
#########################################################################
#########################################################################
# Data Summary
#########################################################################
# 3. Different measures of data
#########################################################################
# 3.a Catergorical Data
# -----------------------------------------------------------------------
religion=factor(c("Hindu","Muslim",'Muslim','Buddhist',
                  'Christian','Sikh','Muslim','Buddhist',
                  'Muslim','Muslim','Buddhist','Buddhist',
                  'Christian','Hindu','Christian','Sikh',
                  'Christian','Christian','Christian',
                  'Buddhist','Buddhist','Christian','Hindu',
                  'Christian','Muslim'))  
table(religion)                           # frequency table
addmargins(table(religion))
#########################################################################
# 3.b Variable Discrete
# -----------------------------------------------------------------------
siblings = c(0,2,2,1,1,1,1,3,0,0,2,1,1,0,2,3,1,4,1,2,2,0,1,0,0,1,3,0,1,1)
addmargins(table(siblings))
mean(siblings)
1/mean(1/(siblings+1))      # H.M.
exp(mean(log(siblings+1)))  # G.M.
mean(siblings+1)            # A.M.
sd(siblings)
#########################################################################
# 3.c Variable Continuous
# -----------------------------------------------------------------------
baby_wtN=rnorm(1000,mean = 4,sd=.5)
baby_wtR=rnorm(1000,mean = 4,sd=1)
# --------------------- Central Tendency --------------------------------
# Mean
mean(baby_wtN);mean(baby_wtR)
# Median
median(baby_wtN);median(baby_wtR)
# ------------------------ Dispersion -----------------------------------
# Range
range(baby_wtN);range(baby_wtR)
a=floor(min(range(baby_wtN),range(baby_wtR)))
b=ceiling(max(range(baby_wtN),range(baby_wtR)))
# Mean absolute deviation w.r.t median
mad(baby_wtN);mad(baby_wtR)
# Standard deviation
sd(baby_wtN);sd(baby_wtR)
# Varaince
var(baby_wtN);var(baby_wtR)
# Coefficient of variatio
(sd(baby_wtN)/mean(baby_wtN));(sd(baby_wtR)/mean(baby_wtR))
par(mfrow=c(1,2))
# Histogram
hN<-hist(baby_wtN, breaks=seq(a,b,by=.25),main="Baby wts in NRS",
         xlab="Baby Weight",xlim=c(a,b),col="darkmagenta",border='yellow',freq=FALSE)   
hR<-hist(baby_wtR, breaks=seq(a,b,by=.25),main="Baby wts in RGK",
         xlab="Baby Weight",xlim=c(a,b),col="darkmagenta",border='yellow',freq=FALSE)   
# Box Plot
par(mfrow=c(1,2))
boxplot(baby_wtN,col=c("yellow"),border="pink",range = 1.5,main='Baby wts in NRS',ylim=c(a,b))
fivenum(baby_wtN)
boxplot(baby_wtR,col=c("yellow"),border="pink",range = 1.5,main='Baby wts in RGK',ylim=c(a,b))
fivenum(baby_wtR)
# -------------------------- Skewness -----------------------------------
library(sn)
dataN=rsn(10000,3,1,-4)   # Negatively skeewed
dataS=rsn(10000,3,1,0)    # Symmetric
dataR=rsn(10000,3,1,4)    # Positively skeewed
library(moments)
skewness(dataN)
skewness(dataS)
skewness(dataR)
a=floor(min(range(dataN),range(dataS),range(dataR)))
b=ceiling(max(range(dataN),range(dataS),range(dataR)))
par(mfrow=c(3,1))
# Histogram
hN<-hist(dataN, breaks=seq(a,b,by=.25),main="-ve Skew",xlab="DataN",xlim=c(a,b),col="darkmagenta",border='yellow')   
mvN=c(min(hN$mids)-(hN$mids[2]-hN$mids[1]),hN$mids,max(hN$mids)+(hN$mids[2]-hN$mids[1]));
freqN=c(0,hN$counts,0);lines(mvN,freqN,type="b",pch=10,col="red",lwd=3)
hS<-hist(dataS, breaks=seq(a,b,by=.25),main="zero Skew",xlab="DataS",xlim=c(a,b),col="darkmagenta",border='yellow')   
mvS=c(min(hS$mids)-(hS$mids[2]-hS$mids[1]),hS$mids,max(hS$mids)+(hS$mids[2]-hS$mids[1]));
freqS=c(0,hS$counts,0);lines(mvS,freqS,type="b",pch=10,col="red",lwd=3)
hR<-hist(dataR, breaks=seq(a,b,by=.25),main="+ve Skew",xlab="DataR",xlim=c(a,b),col="darkmagenta",border='yellow')   
mvR=c(min(hR$mids)-(hR$mids[2]-hR$mids[1]),hR$mids,max(hR$mids)+(hR$mids[2]-hR$mids[1]));
freqR=c(0,hR$counts,0);lines(mvR,freqR,type="b",pch=10,col="red",lwd=3)
# Box Plot
par(mfrow=c(1,3))
boxplot(dataN,col=c("yellow"),border="pink",range = 1.5,main='-ve Skew',ylim=c(a,b))
boxplot(dataS,col=c("yellow"),border="pink",range = 1.5,main='zero Skew',ylim=c(a,b))
boxplot(dataR,col=c("yellow"),border="pink",range = 1.5,main='+ve Skew',ylim=c(a,b))
#########################################################################
# -------------------------- Kurtosis -----------------------------------
dataM=rnorm(10000,0,sqrt(1.4))  # Mesokurtic
dataL=rt(10000,7)               # Leptokurtic
dataP=runif(10000,-2.05,2.05)   # Platykurtic
mean(dataM);mean(dataL);mean(dataP)
var(dataM);var(dataL);var(dataP)
skewness(dataM);skewness(dataL);skewness(dataP)
kurtosis(dataM)   
kurtosis(dataL)
kurtosis(dataP)
a=floor(min(range(dataM),range(dataL),range(dataP)))
b=ceiling(max(range(dataM),range(dataL),range(dataP)))
# Histogram
par(mfrow=c(3,1))
hM<-hist(dataM, breaks=seq(a,b,by=.25),main="Mesokurtic (=3)",xlab="DataM",xlim=c(a,b),col="darkmagenta",border='yellow')   
mvM=c(min(hM$mids)-(hM$mids[2]-hM$mids[1]),hM$mids,max(hM$mids)+(hM$mids[2]-hM$mids[1]));
freqM=c(0,hM$counts,0);lines(mvM,freqM,type="b",pch=10,col="red",lwd=3)
hL<-hist(dataL, breaks=seq(a,b,by=.25),main="Leptokurtic (>3)",xlab="DataL",xlim=c(a,b),col="darkmagenta",border='yellow')   
mvL=c(min(hL$mids)-(hL$mids[2]-hL$mids[1]),hL$mids,max(hL$mids)+(hL$mids[2]-hL$mids[1]));
freqL=c(0,hL$counts,0);lines(mvL,freqL,type="b",pch=10,col="red",lwd=3)
hP<-hist(dataP, breaks=seq(a,b,by=.25),main="Platykurtic (<3)",xlab="DataP",xlim=c(a,b),col="darkmagenta",border='yellow')   
mvP=c(min(hP$mids)-(hP$mids[2]-hP$mids[1]),hP$mids,max(hP$mids)+(hP$mids[2]-hP$mids[1]));
freqP=c(0,hP$counts,0);lines(mvP,freqP,type="b",pch=10,col="red",lwd=3)
# Box Plot
par(mfrow=c(1,3))
boxplot(dataM,col=c("yellow"),border="pink",range = 1.5,main='Mesokurtic (=3)',ylim=c(a,b))
boxplot(dataL,col=c("yellow"),border="pink",range = 1.5,main='Leptokurtic (>3)',ylim=c(a,b))
boxplot(dataP,col=c("yellow"),border="pink",range = 1.5,main='Platykurtic (<3)',ylim=c(a,b))
#########################################################################
