#Name: Waleed Mulla
#Date: 1/25/2019
#Purpose: the objective is to create resonance frequency

#welcome the user to the program

print ("Welcome to my program")

#import the resonance circuit class
from resonancecircuitclass import ResonantCircuit


#input
series = SeriesResonantCircuit(1, 2, 3)
parallel = ParallelResonantCircuit(4, 5, 6)
series.display()
parallel.display()
