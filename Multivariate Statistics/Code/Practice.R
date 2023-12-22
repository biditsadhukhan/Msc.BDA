library(Flury)
data("apples")
str(apples)
data=apples[apples[,1]==1,]
data=data[,-1]
pca_apples=prcomp(data, center=TRUE,scale.=TRUE)
pca_apples
summary(pca_apples)
pca_apples_mat=as.matrix(pca_apples$rotation)
pca_apples_mat

apples_var_eigen=(pca_apples$sdev)^2
apples_var_eigen
plot(apples_var_eigen,type = 'b')
