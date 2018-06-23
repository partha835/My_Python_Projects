import pprint
story='good morning everyone i am partha , i am gonn ahost the todayes show ,\
lets make todets afternoon remarkeble.'
count=len(story)
print('Length of stinng is :'+str(count))
for i in range(count):
    pprint.pprint(story[i])
