import csv

filename=input("What would you like to the name the file that's going to contain your coordinate values? \n")


listofcoord=[]
for i in range(1000):
    coord=input("Insert a set of coord? Format x,y,z \n")
    if coord=="q":
        print("Exiting inserting coordinate system.")
        break
    listofcoord.append(coord)
    print("Coordinate has been inserted")
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for coord in listofcoord:
        x, y, z = coord.split(',')
        writer.writerow([x.strip(), y.strip(), z.strip()])
    print(f"Data has been written to {filename} successfully.")

print("Complete")
