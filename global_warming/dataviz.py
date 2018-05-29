# visualizing temperature as it changes with atmospheric CO2 content and number of cars

# imports
import sys, os
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"

plt.style.use('seaborn-whitegrid')

# dataset filepaths
avg_temp_filepath = "./Complete_TAVG_complete.txt"
avg_co2_filepath = "./mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_000001-201412.csv"
num_cars = "./mv200.pdf"

# extract temperature data 
with open(avg_temp_filepath, "r") as tmp_f:
	temp_data = tmp_f.readlines()

temp_year = []
temp_avg = []
temp_unc = []
for line in temp_data:
	if line[0] == '%':
		del temp_data[temp_data.index(line)]
		continue
	else:
		splt = line.split()
		if len(splt) > 1:
			print splt[0], splt[1], splt[4], splt[4]
			# raw_input()
			temp_year.append(int(splt[0])+float(splt[1])/100.)
			temp_avg.append(float(splt[6]))
			temp_unc.append(float(splt[7]))

# make temp plot
plt.subplot(211)
plt.plot(temp_year, temp_avg)
# plt.fill_between(temp_year, temp_avg-temp_unc, temp_avg+temp_unc)
# plt.errorbar(temp_year, temp_avg, yerr=temp_unc)
plt.xlim(1750,2018)
plt.xlabel("Year")
plt.ylabel("$^\circ$C deviation")
plt.title("$^\circ$C deviation, based on average between 1951-1980, from 1750")

# extract co2 data
with open(avg_co2_filepath, "r") as co2:
	co2_data = co2.readlines()

co2_year = []
co2_avg = []
for line in co2_data:
	if co2_data.index(line) == 0:
		continue
	else:
		splt = line.split(',')
		year = int(splt[1])+float(splt[2])/100.
		if year < 1750:
			continue
		else:
			co2_year.append(year)
			co2_avg.append(float(splt[5]))

plt.subplot(212)
plt.plot(co2_year, co2_avg)
plt.xlim(1750,2018)
plt.xlabel("Year")
plt.ylabel("Mole fraction")
plt.title("Mole fraction of carbon dioxide in air (average of two hemispheres)")

plt.show()

