import tabula

tables = tabula.read_pdf("sample.pdf", pages="4")     #select pages to read
dataframe = tables[0]     #display table information
print(dataframe[dataframe.India > 50])     #filter table data to display