import tabula

tables = tabula.read_pdf("sample.pdf", pages="4")     #select pages to read
dataframe = tables[0]     #display table information
print(dataframe[dataframe.Japan > 5])     #filter table data to display

#save extracted tables into .txt file
f = open("table.txt", "w")
f.write(str(dataframe))
f.close()