#T-test for two independent univariate normal populations

diff<-c(5,22,-2,3,4,-2,6,18,11,-11,7,15,10,6,-1,5,-3,5,1,8,12,-4)
t.test(diff, mu = 0,alternative="greater")
t.test(diff, mu = 0,alternative="less")
t.test(diff, mu = 0,alternative="both")
t.test(diff, mu = 0)

#T-test for two independent univariate normal populations

batch_1<-c(1505, 1556, 1801, 1629, 1644, 1607, 1825, 1748)
batch_2<-c(1799, 1618, 1604, 1655, 1708, 1765, 1728)
t.test(batch_1, batch_2)
t.test(batch_1, batch_2,var.equal = TRUE)

#Paired T-test
before<-c(109,112,98,114,102,97,88,101,89)
after<-c(115,120,99,117,105,98,91,99,93)
t.test(before, after, paired=TRUE)

#If Correlation is ignored
t.test(before, after)

#Testing of Variance
install.packages("EnvStats")

library(EnvStats)

x<-c(62, 63, 64, 65, 67, 67, 68, 69, 70, 72)

###########################################################

# Known sigma = 2
#Two sided test

varTest(x, alternative = "two.sided", conf.level = 0.95, sigma.squared = 4, data.name = NULL)

#Greater than type test

varTest(x, alternative = "greater", conf.level = 0.95, sigma.squared = 2, data.name = NULL)

#Less than type test

varTest(x, alternative = "less", conf.level = 0.95, sigma.squared = 2, data.name = NULL)

