hash_table = {
    "animal": 3,
    "dev": 23,
    "celebrity": 4
}

# print(len(string))

test = {
    'animal': [
        {
            'Joke': 'They say curiosity killed the cat. This is false. Chuck Norris killed the cat. Every single one of them.',
            'Number of Characters': 104
        },
        {
            'Joke': 'Chuck Norris does not own a house. He walks into random houses and people move.',
            'Number of Characters': 79
        },
        {
            'Joke': 'Chuck Norris once rode a nine foot grizzly bear through an automatic car wash, instead of taking a shower.',
            'Number of Characters': 106
        }
    ],
    'dev': [
        {
            'Joke': "Chuck Norris doesn't need garbage collection because he doesn't call .Dispose(), he calls .DropKick().",
            'Number of Characters': 102
        },
        {
            'Joke': "Chuck Norris doesn't need a debugger, he just stares down the bug until the code confesses.",
            'Number of Characters': 91
        }
    ]
}
# print(type(test))
# print(test.keys())
print(test["career"][0]["Joke"])
