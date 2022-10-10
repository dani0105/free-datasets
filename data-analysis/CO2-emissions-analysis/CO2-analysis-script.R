##################################################
## Project: https://github.com/dani0105/free-datasets
## Script purpose: Analyze the CO2 emissions dataset
## Date: 2022-10-08
## Author: informationvulture
##################################################

# Packages to load
library(`ggplot2`)

# Set absolute path to CN_CHINA.csv
path <- getwd() # From where this script is run
setwd(path)

# Assuming you are doing this in the free-datasets directory,
# the relative path to the csv file is:
content <- read.csv("../../datasets/CO2-emissions/CN_CHINA.csv", header = TRUE)

## ---------------------------

# Total emissions plot

png(filename = "CO2-analysis-img/total-emissions.png")
ggplot(content, aes(x = year, y = co2_total_megatonne)) +
       geom_bar(stat = "identity",  fill = "#cd7270", colour = "#000000") +
       xlab("Years") + ylab("CO2 Emissions (Megatonne)") +
       ggtitle("Total CO2 Emissions in China (Mt/yr)")
dev.off()

# CO Emissions in kilograms per $1000 GDP

png(filename = "CO2-analysis-img/emissions-per-kg.png")
ggplot(content, aes(x = year, y = co2_kilogram_for_one_thousand_dollars)) +
       geom_bar(stat = "identity",  fill = "#7e509a", colour = "#000000") +
       xlab("Years") + ylab("Kilograms per $1000") +
       ggtitle("CO2 emissions per (Kg/$1,000 of GDP)")
dev.off()

## ---------------------------
## IMAGES
## ---------------------------

# Box plot to show any outliers

png(filename = "CO2-analysis-img/total-data-boxplot.png")
boxplot(content$co2_total_megatonne,
       main = "Boxplot of CO2 Emissions in China since 1970",
       xlab = "Megatonnes",
       ylab = "CO2 Emissions",
       col = "grey",
       border = "black",
       horizontal = TRUE)
dev.off()

## ---------------------------
## Summary Statistics
## ---------------------------

# Using 'co2_total_megatonne' column
mu <- mean(content$co2_total_megatonne) # mean
sd <- sd(content$co2_total_megatonne) # standard deviation
median <- median(content$co2_total_megatonne) # median

t_test <- t.test(content$co2_total_megatonne, conf.level = 0.95) # t-test
t_test

linear_model <- lm(content$co2_total_megatonne ~ content$year) # linear model
linear_model


quant <- quantile(content$co2_total_megatonne) # quantiles
quant