d <- read.csv('federal_title_ix_investigations.txt', na.strings=c("NA", "N/A"))
d$DateOpened <- as.Date(d$DateOpened, "%B %d, %Y")
d$DateResolved <- as.Date(d$DateResolved, "%B %d, %Y")
write.csv(d, 'title-ix-investigations-chronicle.csv', row.names=F)