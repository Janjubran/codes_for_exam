## dict.values()
##dict.keys()
##dict.update()
##dict.items()
#%%
def popular_word(text):
    words = text.split()
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    counts = dict(sorted(counts.items(),
                         key =lambda x: x[1], reverse=True))
    return list(counts.keys())[:10]
text = '''jan jan jan longe longe berey longe text
'''
print(popular_word(text))
# %%

def combine(lst1,lst2):
    return dict(zip(lst1,lst2))
lst1 = ['banana','tot','apple']
lst2 = ['10₪ Per kilo','19.99₪ Per kilo','15.90₪ Per kilo']
print(combine(lst1,lst2))
# %%
## Return students name with average > 85:
def above_avg(students):
    for stud in students:
        avg = (stud['eng-grade']+ stud['math-grade']) /2
        if avg > 85:
            print(stud['name'])
        else:
            print(f'{stud['name']} did not pass') 

students = [
    {'name':'nir','eng-grade':90,'math-grade' : 73},
    {'name':'jan','eng-grade':60,'math-grade' : 73},
    {'name':'loxz','eng-grade':90,'math-grade' : 99},
    {'name':'chris','eng-grade':90,'math-grade' : 85} ]
print(above_avg(students))