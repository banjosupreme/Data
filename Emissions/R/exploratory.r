numberCommaOld <- function(number)
{
    outString <- ""
    while (number > 0)
    {    
        remainder <- number%%1000
        remString <- as.character(remainder)
        number <- (number - remainder)%/%1000
        
        if(number>0)
        {
            
            while(nchar(remString)<3)
            {
                remString <- paste("0",remString,sep = "")
            }
            remString<-paste(",",remString,sep="")
        }
        outString<-paste(remString,outString,sep="")     
    }
    outstring <- as.character(outString)
    return(outString)
}

numberComma <- function(number)
{
    ub <- nchar(number)
    toCopy <- ub
    commas <- (ub-1)%/%3
    
    copied<-0
    outString <- ""
    while (copied < toCopy)
    {
        lb <- max(1,ub-2)
        outString <- paste(substring(number,lb,ub),outString,sep="")
        copied <- copied + (ub - lb) + 1
        ub <- lb - 1
        if(commas>0)
        {
            outString <- paste(",",outString, sep ="")
            commas <- commas - 1
        }
    
    }
 
    return(outString)
}



}

library(reshape2)
setwd("")

socioEc <- read.csv("CAIT 2.0 Country Socio-Economic Data.csv")
socioEc <- socioEc[,c(1:3)]
names(socioEc)[3]<-"Population"
socioEc <- socioEc[with(socioEc, order(Country, Year)), ]
write.csv(socioEc, "popData.csv", row.names = FALSE)

#countries since 1960
socioEc <- read.csv("popData.csv")
socioEc <- socioEc[,c(1:3)]
names(socioEc)[3]<-"Population"
popTable<-data.frame(Population = socioEc$Population, pString = sapply(socioEc$Population, numberComma))
socioEc<-merge(socioEc,popTable)
socioEc <- socioEc[with(socioEc, order(Country, Year)), ]
longse <- melt(socioEc, id = c("Country", "Year"))
write.table(longse, "popPrinting.dat", row.names = FALSE, sep = "!")

#Countries since 1990
CountryGHG <- read.csv("CAIT 2.0 Country GHG Emissionsm.csv")
CountryGHG <- CountryGHG[,c(1,2,4,6,7,8)]
names(CountryGHG)[3:6]<-c("Total GHG", "Total CH4", "Total N20", "Total F-Gas") 



CountryGHG <- merge(CountryGHG,socioEc)
CountryGHG <- CountryGHG[complete.cases(CountryGHG),]
GHG <- melt(CountryGHG, id = c("Country", "Year", "Population", "pString"))

#CO2 since 1850
CountryCO2 <- read.csv("CAIT 2.0 Country CO2 Emissions.csv")
names(CountryCO2)[3]<-"Total CO2"

CountryCO2 <- merge(CountryCO2, socioEc)
CountryCO2 <- CountryCO2[complete.cases(CountryCO2),]
CO2 <- melt(CountryCO2, id = c("Country", "Year", "Population", "pString"))
GHG <- rbind(CO2, GHG)

names(GHG)[5:6] <- c("ghg","MtCO2")
GHG$TperCap <- GHG$MtCO2*1000000/GHG$Population
GHG$TperCap <- round(GHG$TperCap, digits = 2)

GHG <- GHG[with(GHG, order(ghg, Country, Year)), ]
write.table(GHG, "GHGsummaryData.dat", row.names = FALSE, sep="!")


