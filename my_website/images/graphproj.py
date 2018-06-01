'''
histogram_age_income.py 
reads data from the age_income_feb14.csv
and creates two histograms: the age distribution and the income 
distribution. The data are from U.S. Census Bureau's February 2014 
Current Population Survey. 

(c) 2014 Project Lead The Way
'''
import matplotlib.pyplot as plt

# A generic helper function for matplotlib.pyplot graphics
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)

###
# Get the income/age data from CSV
###
# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Project12.csv')
datafile = open(filename,'r')
data = datafile.readlines()

####
# Transform the data from strings to signed integers
####
ages=[]
incomes=[]

for line in data[3:116]: # Omit 0, 1, 2 because _______
    age, income = line.split(',')

    # ___________ the age data
    ages.append(int(age))

        # Do not use the first 2 characters: space and $
        # and do not use the last character: \n
    incomes.append(income)
    
    
    
ages1=[]
incomes1=[]

for line in data[117:230]: # Omit 0, 1, 2 because _______
    age, income = line.split(',')

    # ___________ the age data
    ages1.append(int(age))

        # Do not use the first 2 characters: space and $
        # and do not use the last character: \n
    incomes1.append(income)
ages2=[]
incomes2=[]

for line in data[231:344]: # Omit 0, 1, 2 because _______
    age, income = line.split(',')

    # ___________ the age data
    ages2.append(int(age))

        # Do not use the first 2 characters: space and $
        # and do not use the last character: \n
    incomes2.append(income)
        
           

fig, ax = plt.subplots(1,1)
ax.plot(ages,incomes,'#FF0000')
ax.plot(ages1,incomes1,'#0000FF')
ax.plot(ages2,incomes2,'#008000')
ax.set_xlabel('Year')
ax.set_ylabel('Average Life Expectancy (Age)')
make_PLTW_style(ax)
ax.set_ylim(35,83)
ax.set_xlim(1900,2020)
ax.set_title('Life Expectancy Over The Last Century by Sex\n',fontweight="bold", size=18)
fig.patch.set_facecolor('xkcd:light blue')
ax.set_facecolor('xkcd:yellow')

fig.show()
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

red_patch = mpatches.Patch(color='red', label='Both Sexes')
blue_patch = mpatches.Patch(color='blue', label='Male')
green_patch = mpatches.Patch(color='green', label='Female')
plt.legend(handles=[red_patch,blue_patch,green_patch])
plt.show()