import numpy as np
 
 
 
np.random.seed(42)
fake = np.random.randint(50 , 2000, size=30)
 
print(fake)

# Print the total, the average, the median, and the highest and lowest day.
print("Total:" , fake.sum())
print("Average:" , fake.mean())
print("Median:" , np.median(fake))
print("Highest:" , fake.max())
print("Lowest:" , fake.min())

# Print how many days were above 1000. Hint: (arr > 1000).sum(), where True counts as 1.
print("Days above 1000:" , (fake > 1000).sum())

# Create a labels array: "High" if > 1000, "Medium" if > 300, otherwise "Low". Hint: np.where inside another np.where.
labels = np.where(fake > 1000, "High", np.where(fake > 300 , "Medium" , "Low") )
print(labels)

# Reshape the 30 days into weeks: take the first 28 days and run .reshape(4, 7). Then print the total per week, using the correct axis.
print(fake[:28].reshape(4,7).sum(axis=1))
# Bonus: find which week spent the most. Hint: look up np.argmax.
print(fake[:28].reshape(4,7).sum(axis=1).argmax())