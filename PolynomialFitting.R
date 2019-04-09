TimeOfDaySVM <- read.csv("~/school/IPAM/TimeOfDaySVM.csv")
HoursRequestedSVM <- read.csv("~/school/IPAM/HoursRequestedSVM.csv")
DayOfWeekSVM <- read.csv("~/school/IPAM/DayOfWeekSVM.csv")
PriceSVM <- read.csv("~/school/IPAM/PriceSVM.csv")
NoticeGivenSVM <- read.csv("~/school/IPAM/NoticeGivenSVM.csv")

for (dataset in list(TimeOfDaySVM, HoursRequestedSVM, DayOfWeekSVM, PriceSVM, NoticeGivenSVM)) {

  real <- unlist(dataset[1], use.names = FALSE)
  SVM  <- unlist(dataset[2], use.names = FALSE)
  Axis <- as.numeric(unlist(dataset[3], use.names = FALSE))
  #turns into easier to use vectors
  minmax <- c(real, SVM)
  #combines real values and SVM approximations to get total range
  
  Nreal <- ((real - min(minmax))/(max(minmax)-min(minmax)))
  NSVM  <- ((SVM  - min(minmax))/(max(minmax)-min(minmax)))
  #uses minmax to normalize vectors
  
  RealSVMTitle <- paste("Real (Black), SVM Prediction (Red),", names(dataset)[1])
  #Title for Comparison
  
  RealTitle <- paste("Real (Black), Polynomial Approximation (Gray),", names(dataset)[1])
  #Title for Real
  
  SVMTitle <- paste("SVM Prediction (Red), Polynomial Approximation (Orange),", names(dataset)[1])
  #Title for SVM
  
  TPTitle <- paste("Total Plot,", names(dataset)[1])
  #Title for total plot

  SVMOffBy <- function(x) {
    n <- 100
    NrealModel <- (lm(Nreal ~ poly(x, n, raw = TRUE)))
    NSVMModel  <- (lm(NSVM  ~ poly(x, n, raw = TRUE)))
    plot(Nreal ~ Axis, type = "o", main = RealSVMTitle, ylim = c(0,1))
    lines(NSVM ~ Axis, type = "o", col = "red")
    #Normalized Real, Normalized SVM Plot
    plot(Nreal ~ Axis, type = "o", main = RealTitle, ylim = c(0,1))
    lines(Axis, fitted(NrealModel), col = "gray")
    #Normalized Real, Polynomial Model Plot
    plot(NSVM ~ Axis, type = "o", col = "red", main = SVMTitle, ylim = c(0,1))
    lines(Axis, fitted(NSVMModel), col = "orange")
    #Normalized SVM,  Polynomial Model Plot
    plot(Nreal ~ Axis, type = "o", main = TPTitle, ylim = c(0,1))
    lines(Axis, fitted(NrealModel), col = "gray")
    lines(NSVM ~ Axis, type = "o", col = "red")
    lines(Axis, fitted(NSVMModel), col = "orange")
    #Everything Plot
    return ((fitted(NrealModel) - fitted(NSVMModel))*(fitted(NrealModel) - fitted(NSVMModel)))
  }
  #squared error of SVM (using normalized polynomial model)
  
  print(paste("Approximate MSE of Normalized SVM Predictions for",  names(dataset)[1], ":", signif(sum(SVMOffBy(Axis))/(max(Axis)-min(Axis)))))
  #approx. mean squared error of SVM

}