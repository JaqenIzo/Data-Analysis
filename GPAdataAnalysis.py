import numpy as np
import matplotlib.pyplot as plt



with open("gpa.txt", "r") as f:
   lines = f.readlines()


list_of_tuples = []
for line in lines:
  
   parts = line.split(",")


  
   tuple = (parts[0], parts[1],parts[2],parts[3],parts[4],parts[5])
   

   # Add the tuple to the list
   list_of_tuples.append(tuple)
y = np.array(list_of_tuples)
x = y[:, np.newaxis]
# print(y)

gps = [i[2] for i in y]
ndGpa = np.array(gps, dtype=float)
myMean = round(np.mean(ndGpa),2)
print(myMean)

myType = np.dtype([('ID',np.int32),('gender','U20'),('gpa',np.float64),('firstName','U20'),('lastname','U20'),('state','U2')])
arr = np.array([ i for i in list_of_tuples],dtype=myType)




belowAv =len( np.array([i for i in ndGpa if i< myMean]))

aboveAv = len(np.array([i for i in ndGpa if i> myMean]))



maskMaleOnly = arr['gender'] == "Male"
maleOnly=arr[maskMaleOnly]
males_gpa = maleOnly['gpa'].mean()


maskFemaleOnly = arr['gender']== 'Female'
femaleOnly =  arr[maskFemaleOnly]
female_gpa = femaleOnly['gpa'].mean()

# print(maleOnly)

maskMaleBelow = maleOnly['gpa']<myMean
male_below_ave = len(maleOnly[maskMaleBelow])


maskfemalebelow = femaleOnly['gpa']<myMean
female_below_ave = len(femaleOnly[maskfemalebelow])

male_above_average = len(maleOnly) - male_below_ave
female_above_average = len(femaleOnly) - female_below_ave

mask = maleOnly['gpa'] > myMean
maleMask = arr['gender'] == 'Male'
onlyMale = arr[maleMask]
print(onlyMale == maleOnly)

male_Above = maleOnly[mask]
print(len(male_Above))

print(male_above_average)





 
 
# print(female_below_ave)

barNames= ('MALE GPA','FEMALE GPA','STUDENT ABOVE AV ','STUDENTS BELOW AV','MALE ABOVE','FEMALE ABV','MALE BELOW','FEMALE BELOW')

plot_values = (males_gpa,female_gpa,aboveAv,belowAv,male_above_average,female_below_ave,male_below_ave,female_below_ave)

plt.bar(barNames,plot_values ,color="cyan")
plt.xlabel("Stats")
plt.ylabel('GPA')
plt.title("Stats on National Exam 2023")
plt.plot()
plt.show()





 
 


