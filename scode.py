import pandas as pd
from scipy import sparse
# Using map() and lambda
def listOfTuples(l1, l2):
    return list(map(lambda x, y: (x, y), l1, l2))



list1 = ["Amazing Spider-Man, The (2012)", "Mission: Impossible III (2006)", "10 Cloverfield Lane (2016)",
         "Affair to Remember, An (1957)"]
list2 = []
print("Enter The rating for The Five movies from 1-5")

print("    Amazing Spider-Man, The (2012)\n", "   Mission: Impossible III (2006)\n", "   10 Cloverfield Lane (2016)\n",
      "   Affair to Remember, An (1957)")

for i in range(0, 4):
    list2.append(int(input()))

i_f = listOfTuples(list1, list2)
ratings = pd.read_csv('dataset/ratings.csv')
movies = pd.read_csv('dataset/movies.csv')
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings.head()
#print
print("PROCESSING \n")
userRatings = userRatings.dropna(thresh=5, axis=1).fillna(0,axis=1)
#userRatings.fillna(0, inplace=True)
#print("After: ",userRatings.shape)
corrMatrix = userRatings.corr(method='pearson')
corrMatrix.head(100)
def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings



similar_movies = pd.DataFrame()
for movie, rating in i_f:
    similar_movies = similar_movies.append(get_similar(movie, rating), ignore_index=True)
print("YOUR MOVIE RECOMMENDATION SYSTEM \n ________________________________________________________")
similar_movies.head(10)
print(similar_movies.sum().sort_values(ascending=False).head(20))