import matplotlib.pyplot as plt

d = {"i":""}
 #open model output file
f = open('output_240_day-april.dat', 'rb')
for _ in range(2):
    line = f.readline()
line = f.readline()
foo = line.split()

for item in foo:
    d[item] = ""

print  d
print
print foo

#Draw model results

plt.figure(1)

plt.subplot(311)
plt.title('Water') # subplot 313 title
plt.xlabel('$\mu$M')
plt.ylabel('M')
plt.axis([0, 160, 0, 110])

plt.subplot(312)
plt.title('BBL') # subplot 312 title
plt.xlabel('mM')
plt.ylabel('M')

plt.subplot(313)
plt.title('Sediment') # subplot 313 title
plt.xlabel('mM')
plt.ylabel('Cm')


#plt.show()