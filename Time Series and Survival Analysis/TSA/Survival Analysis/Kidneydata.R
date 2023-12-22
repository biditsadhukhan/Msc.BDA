# Calling the required librarieS
library(survival)
library(KMsurv)
library(flexsurv)
library(ggfortify)

data=kidney


# getting the structure of the data
str(data)
head(data)
names(data)
summary(data)
sum(is.na(data))


#creating the survival object
survobj=Surv(data$time,data$status)

#Estimating the survival function using the Kaplan Mayer estimate of survival function
fit_KM_1=survfit(survobj~1,data=data,stype = 1) #direct way of estimating the survival function using the kaplan mayer estimate
summary(fit_KM_1)
plot(fit_KM_1)
autoplot(fit_KM_1)
fit_KM_2=survfit(survobj~1,data = data,stype = 2)   #indirect way of estimating the survival function from the Nelson Alen estimator
plot(fit_KM_2)

#Estimating the survival function using the kaplan mayer estimate of survival function using the covariates

fit_KM_cov=survfit(survobj~1+sex+disease,data = data,stype = 1)
summary(fit_KM_cov)
plot(fit_KM_cov)
autoplot(fit_KM_cov)
# using the AFT model to predict the survival function without covariate
left=data$time
right=data$time
right[which(data$delta==0)]=NA
toest_data= data.frame(left,right)
fgamma=fitdistcens(toest_data,'gamma')
shapeg=fgamma$est[1]
rateg=fgamma$est[2]
plot(fgamma)

par(mfrow=c(1,1))
trange = (0:max(na.omit(toest_data[,2])))                 # 0 to maximum failure time
plot(trange,1-pgamma(trange, shape = shapeg, rate = rateg),xlab="Time", 
     ylab="Survival probability",ylim=c(0,1),col=2,type='l')      # gamma MLE
# using the AFT model to predict the survival function with covariates

predict_cov_g=flexsurvreg(survobj~as.factor(type),data=data,dist = 'lo')
summary(predict_cov_g)
plot(predict_cov_g,col=c(4,6))
str(data$type)
