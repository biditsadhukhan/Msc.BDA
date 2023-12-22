#########################################################################
#########################################################################
#                       Data Visualization in R [6]
#########################################################################
#########################################################################
# Basis R graphics
#########################################################################
# 2. Different plot types and customizations
#########################################################################
# 2.a Catergorical Data
# -----------------------------------------------------------------------
religion=factor(c("Hindu","Muslim",'Muslim','Buddhist',
                  'Christian','Sikh','Muslim','Buddhist',
                  'Muslim','Muslim','Buddhist','Buddhist',
                  'Christian','Hindu','Christian','Sikh',
                  'Christian','Christian','Christian',
                  'Buddhist','Buddhist','Christian','Hindu',
                  'Christian','Muslim'))  
table(religion)                           # frequency table
# -----------------------------------------------------------------------
# 2.a.(i) vertical bar diagram
# -----------------------------------------------------------------------
barplot(table(religion))                  # vertical bar diagram
barplot(table(religion),
        xlab = 'Religion',ylab = 'Number of people',
        ylim = c(0,10),col='blue')        # vertical bd customized
title(main='Religion Frequency Distribution',sub='Vertical bar diagram')
box()
# -----------------------------------------------------------------------
# 2.a.(ii) horizontal bar diagram
# -----------------------------------------------------------------------
barplot(table(religion),horiz = TRUE)     # horizontal bar diagram
barplot(table(religion),horiz = TRUE,
        ylab = 'Religion', xlab = 'Number of people',
        xlim = c(0,9),col='blue')         # horizontal bd customized
title(main='Religion Frequency Distribution',sub='Horizontal bar diagram')
box()
# -----------------------------------------------------------------------
# 2.a.(iii) divided bar diagram
# -----------------------------------------------------------------------
data=matrix(table(religion), nrow=5)
colnames(data)=c("Religion")
rownames(data)=c("Buddhist","Chirstian","Hindu","Muslim","Sikh")
barplot(data,col=c('red','magenta','orange','green','blue'),
        border="white",space=0.04,font.axis=2,xlab="group",
        legend.text=c("Buddhist","Chirstian","Hindu","Muslim","Sikh"))
title(main='Religion percentages',sub='Divided Bar Diagram')
box()
# -----------------------------------------------------------------------
# 2.a.(iv) pie chart
# -----------------------------------------------------------------------
pie(table(religion))                      # pie chart
pie(table(religion),col=c('red','white','orange','green','blue'),clockwise = T, 
    init.angle = 180,cex=1.2)             # pie chart customized
title(main='Religion percentages',sub='Pie Chart')
box()
#########################################################################
# 2.b Variable Discrete
# -----------------------------------------------------------------------
siblings = c(0,2,2,1,1,1,1,3,0,0,2,1,1,0,2,3,1,4,1,2,2,0,1,0,0,1,3,0,1,1)
table(siblings)
# -----------------------------------------------------------------------
# 2.b.(i) Freqyency bar chart
# -----------------------------------------------------------------------
plot(table(siblings),col='blue',
     xlab = 'Number of Siblings',ylab = 'Frequency')
title(main='Sibling Frequency Distribution',sub='Freqyency bar chart')
# -----------------------------------------------------------------------
# 2.b.(ii) Cumulative frequency plot/ogive
# -----------------------------------------------------------------------
plot(x=seq(0,4,1),cumsum(table(siblings)),type='s',col='blue',
     xlab = 'Number of Siblings',ylab = 'Cumm. Freq.',ylim = c(0,40))
title(main='Sibling Cumulative Frequency Distribution',sub='Cumulative frequency plot')
# -----------------------------------------------------------------------
# 2.b.(iii) Vertical bar diagram
# -----------------------------------------------------------------------
barplot(table(siblings))                  # vertical bar diagram with axis name
barplot(table(siblings),xlab = 'Number of Siblings',
        ylab = 'Freq', ylim = c(0,15),col='blue',
        border = 'red',density = 16)      # vertical bd customized
abline(h = c(seq(0,16,4)), lty = 3, 
       lwd = .5, col = 'gray40')         # adding horizontal axes in bd
title(main='Sibling Frequency Distribution',sub='Vertical bar diagram')
box()
#########################################################################
# 2.c Variable Continuous
# -----------------------------------------------------------------------
baby_wt=c(2.99,2.74,3.08,3.04,2.79,2.63,2.62,3.40,2.72,2.53,
          3.19,2.77,3.39,3.67,2.45,2.41,2.90,3.50,2.84,3.55,
          3.25,2.56,3.52,3.03,3.14,3.07,3.46,3.13,3.02,3.15,
          3.05,3.20,2.82,2.89,3.26,3.01,2.88,3.01,2.87,2.70,
          3.24,3.74,3.53,3.34,2.44,3.72,2.95,3.09,3.38,3.16,
          2.96,2.39,3.06,2.86,2.54,2.94,2.61,2.48,2.55,2.62)
# -----------------------------------------------------------------------
# 2.c.(i) Histogram
# -----------------------------------------------------------------------
hist(baby_wt)
h<-hist(baby_wt, breaks=seq(2.0,4.0,by=.4),
        main="New-born baby wt in Kolkata",
        xlab="Baby Weight",xlim=c(2,4),
        col="darkmagenta",border='yellow',freq=FALSE)       # customized class width and density
h<-hist(baby_wt,main="New-born baby wt in Kolkata",
     xlab="Baby Weight",xlim=c(2,4),col="darkmagenta")      # customized histogram and frequency
h                                                           # histogram object
text(h$mids,h$counts,labels=h$counts,adj=c(0.5,0.5))        # more customization
# -----------------------------------------------------------------------
# 2.c.(ii) Frequency polygon
# -----------------------------------------------------------------------
mv = c(min(h$mids)-(h$mids[2]-h$mids[1]),
       h$mids,max(h$mids)+(h$mids[2]-h$mids[1]))            # midvalue of class
freq=c(0,h$counts,0)                                        # frequency of class
lines(mv,freq,type="b",pch=20,col="red",lwd=3)              # frequency polygon

title(sub='Histogram with frequency polygon')
# -----------------------------------------------------------------------
# 2.c.(iii) Cumulative frequency diagram/ogive
# -----------------------------------------------------------------------
ucl=seq(from=min(h$breaks),to=max(h$breaks),by=h$breaks[2]-h$breaks[1])
cf=c(0,cumsum(h$counts))
plot(ucl,cf,xlab='Class Boundary',ylab='Cummulative Frequency',
     type="b",col="blue",pch=20)
title(main='New-born baby wt in Kolkata',sub='Cumulative frequency diagram/ogive')
# -----------------------------------------------------------------------
# 2.c.(iv) Box Plot
# -----------------------------------------------------------------------
b<-boxplot(baby_wt,col=c("yellow"),border="pink",
        horizontal=T,notch=T,range = 1.5)
title(main='New-born baby wt in Kolkata',sub='Box-plot')
fivenum(baby_wt)
#########################################################################
# 2.d Non-frequency data
# -----------------------------------------------------------------------
advData=read.csv("Advertising.csv")
x=advData$TV
y=advData$Radio
z=advData$Sales
# -----------------------------------------------------------------------
# 2.d.(i) Two dimensional plot
# -----------------------------------------------------------------------
plot(x,z,col="red",xlab = "TV Expenditure",ylab = "Sales")
title(main='Sales vs TV Expenditure')
# -----------------------------------------------------------------------
# 2.d.(ii) Three dimensional plot
# -----------------------------------------------------------------------
library(scatterplot3d)
scatterplot3d(x,y,z,xlab = "TV Expenditure",
          ylab = "Radio Expenditure",zlab = "Sales",color = "red")
# -----------------------------------------------------------------------
# 2.e. Functional Plot
# -----------------------------------------------------------------------
xf=seq(1:10);yf=seq(1:10)
f=outer(xf,yf,function (x,y)cos(y)/(1+x^2))
fa=outer(xf,yf,function (x,y)2.921+.046*x+.188*y)
ele_3d=persp(xf,yf,f,theta=30,phi=20,col = "green")
elevation_points<-persp(xf,yf,fa,theta=30,phi=20,col='red')
# -----------------------------------------------------------------------

#########################################################################
#########################################################################
# Advance R graphics
#########################################################################
# II Complex Interactive Plots
#########################################################################
# II.a Non-frequency data
# -----------------------------------------------------------------------
# II.a.(i) Three dimensional plot
# -----------------------------------------------------------------------
library(plotly)
plot_ly(advData,x= ~TV,y= ~Radio, z= ~Sales)
# -----------------------------------------------------------------------
# II.a.(ii) Multiple bar diagram
# -----------------------------------------------------------------------
expenditure=
  matrix(c(1.3,1.9,2.5,3.4,3.4,3.3,8.3,5.5,4.7,2.7,4.9,17.1,5.8,1.9,3.3,2.4,3.3,5.6),
         nrow = 3,ncol = 6,byrow = TRUE)                  # Create the matrix of the values.
colors=c("red","blue",'yellow')                           # Create the input vectors.
countries=c("Brazil","China","India",
            "Pakistan",'Singapore',"United States")       # Create the input vectors.
colnames(expenditure)=countries
categories=c("Defense","Health","Education")              # Create the input vectors.
rownames(expenditure)=categories
barplot(expenditure,main = "total expenditure",
        names.arg = countries,xlab = "countries",
        ylab = "expenditure",col = colors)                # multiple bar diagram
legend("topleft", categories, cex = .6, fill = colors)    # add legend to chart
title(sub='multiple bar diagram')
barplot(expenditure,main = "total expenditure",
        names.arg = countries,xlab = "countries",
        ylab = "expenditure",col = colors,beside = TRUE)  # multiple bar diagram
legend("topleft", categories, cex = .6, fill = colors)    # add legend to chart
title(sub='multiple bar diagram')
# -----------------------------------------------------------------------
# II.a.(iii) Line diagram
# -----------------------------------------------------------------------
attach(Orange)
Orange$Tree=as.numeric(Orange$Tree)       # convert factor to numeric
ntrees=max(Orange$Tree)                   # find number of trees
xrange=range(Orange$age)                  # get the range for the x axis
yrange=range(Orange$circumference)        # get the range for the y axis
plot(xrange, yrange, type="n", xlab="Age (days)",
     ylab="Circumference (mm)" )          # set up the plot
colors=rainbow(ntrees)                    # get 5 colors of rainbow
linetype=c(1:ntrees)                      # get 5 line types
plotchar=seq(18,18+ntrees,1)              # get 5 types of point to plot
for (i in 1:5)
{
  tree=subset(Orange, Tree==i) 
  lines(tree$age, tree$circumference, type="b", lwd=1.5,
        lty=linetype[i], col=colors[i], pch=plotchar[i]) 
}                                               # plot 5 different lines
title(main="Tree Growth",sub='line diagram')    # add a title 
legend(xrange[1],yrange[2],1:ntrees,cex=0.7,col=colors,
       pch=plotchar,lty=linetype,title="Tree")  # add a legend
#########################################################################
# II.b Frequency data
# -----------------------------------------------------------------------
# II.b.(i) Pie Chart
# -----------------------------------------------------------------------
library(ggplot2)
dRel=as.data.frame(table(religion))
pie = ggplot(dRel,aes(factor(religion),y=as.numeric(Freq),fill=religion)) +
  geom_bar(width =0.5,stat = "identity")+xlab("Religion")+
  ylab("No. of people")+ggtitle("Extended Pie Chart")+
  coord_polar("x",start =0)
pie
# -----------------------------------------------------------------------
# II.b.(ii) Vertical Bar Diagram
# -----------------------------------------------------------------------
bp<- ggplot(dRel, aes(factor(religion),y=as.numeric(Freq),fill=religion))+
  geom_bar(width = 1,stat="identity")+xlab("Religion")+
  ylab("No. of people")+ggtitle("Divided Bar Diagram")
bp
#########################################################################