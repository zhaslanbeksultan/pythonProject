#Functions_2////////////////////////////////////////////////////////////////////////////////////////////////////////////
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1//////////////////////////////////////
def imdb(n):
    for i in range(0, len(movies)):
        if movies[i]["name"] == n:
            print(movies[i]["imdb"] > 5.5)
n = input("Write a name of movie: ")
imdb(n)

#2//////////////////////////////////////
def imdb_list():
    list1 = []
    for i in range(0, len(movies)):
        if movies[i]["imdb"] > 5.5:
            list1.append(movies[i])
    else:
        print(list1)
imdb_list()

#3/////////////////////////////////////
def cat_func(cat):
    for i in range(0, len(movies)):
        if movies[i]["category"] == cat:
            print(movies[i])
cat = input("Choose a category: ")
cat_func(cat)

#4/////////////////////////////////////
def avg_imdb(list1):
    total = 0
    for i in range(0, len(list1)):
        for j in range(0, len(movies)):
            if movies[j]["name"] == list1[i]:
                total += movies[j]["imdb"]
    print(total/len(list1))
list1 = list(map(str, input().split(', ')))
avg_imdb(list1)

#5/////////////////////////////////////
def avg_imdb(cat):
    total = 0
    r = 0
    for j in range(0, len(movies)):
        if movies[j]["category"] == cat:
            total += movies[j]["imdb"]
            r += 1
    print("The average IMDB score of this category is " + str(total/r))
cat = input("Choose a category: ")
avg_imdb(cat)
