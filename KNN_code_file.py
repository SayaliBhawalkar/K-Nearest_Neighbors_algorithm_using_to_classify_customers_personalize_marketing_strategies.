# step no 1
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# step no 2
data = np.array([[25,50000,2],[30,80000,1],[35,60000,3],[20,30000,2],[40, 90000,1],[45,75000,2]])
labels = np.array([1,2,1,0,2,1])#0:low, 1:medium, 2:high
# step no 3
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
# step no 4
scalar = StandardScaler()
x_train = scalar.fit_transform(x_train)
x_test = scalar.fit_transform(x_test)
# step no 4
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
accuracy = knn.score(x_test, y_test)
print(f"Model accuracy: {accuracy}")
# user input
user_input = np.array([[30, 60000, 1]])
user_input_scaled = scalar.transform(user_input)
knn.predict(user_input_scaled)
