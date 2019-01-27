import os
import csv 

pybankCSV = os.path.join('budget_data.csv')

with open(pybankCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_months = 0 
    net_amount = 0
    previous_month = 0 
    monthly_change_list=[]
    greatest_increase = 0
    greatest_decrease = 9999999
    for row in csvreader:
        #print(row[1])
        total_months = total_months + 1 
        net_amount = net_amount + int(row[1])
        monthly_change = int(row[1]) - previous_month
        previous_month = int(row[1])
        monthly_change_list.append(monthly_change)
        average_change = sum(monthly_change_list)/len(monthly_change_list)
        if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_date = row[0]
        elif monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_date = row[0]
        #print(previous_month)
    print("Financial analysis")    
    print("---------------------------------------------")

    print("total months: " + str(total_months))
    
    print("net amount: $ " + str(net_amount))

    print("greatest increase in profit" + str(greatest_increase_date) + " (" + str(greatest_increase) + ")")

    print("greatest decrease in profit" + str(greatest_decrease_date) + " (" + str(greatest_decrease) + ")")

    print("average change: " + str(average_change))

    with open("output_file.txt", "w", newline="") as datafile:
        datafile.write("Financial analysis")
        datafile.write("\n")
        datafile.write("------------------------------------------")
        datafile.write("\n")
        datafile.write("total months: " + str(total_months))
        datafile.write("\n")
    
        datafile.write("net amount: $ " + str(net_amount))
        datafile.write("\n")

        datafile.write("greatest increase in profit" + str(greatest_increase_date) + " (" + str(greatest_increase) + ")")
        datafile.write("\n")

        datafile.write("greatest decrease in profit" + str(greatest_decrease_date) + " (" + str(greatest_decrease) + ")")
        datafile.write("\n")

        datafile.write("average change: " + str(average_change))

   # writer = csv.writer(datafile)

    