Subject_Wise_Marks = {'CS': 32,
                      'eng':12,
                      'sci':15}
My_JSON = {'name': 'A',
           'age': 18,
           'marks': Subject_Wise_Marks}
My_JSON_Array=[My_JSON,Subject_Wise_Marks]
my_key = Subject_Wise_Marks.keys()
for key in my_key:
    print(Subject_Wise_Marks[key])