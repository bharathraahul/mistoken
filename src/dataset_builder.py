

file_path = '/Users/bharathraahulmurugesan/Documents/mistoken/mistoken/data/google-10000-english-no-swears.txt'
with open (file_path,'r') as f:
    words = f.read().strip().split('\n')


rank=1
t1 = []

for word in words:
    if word:
        t1.append((rank,word))
        rank+=1

t1_filtered = [(rank,word) for rank,word in t1 if len(word) >=4]

print(len(t1_filtered))


def random_char(exclude= None):
    import random
    import string
    # char = random.choice(string.ascii_lowercase)
    # while exclude and char == exclude:
    #     char = random.choice(string.ascii_lowercase)
    # return char
    if exlude:
        pool = string.ascii_lowercase.replace(exclude, '')
    else:
        pool = string.ascii_lowercase
    return random.choice(pool)
        


