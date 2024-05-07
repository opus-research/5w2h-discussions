import csv

from chatgpt_completion import classify_text_with_completions

with open('messages.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    output = [['MESSAGE', 'WHO', 'WHAT', 'WHEN', 'WHERE', 'WHY', 'HOW', 'HOW MUCH']]
    output2 = [['MESSAGE', 'WHO', 'WHAT', 'WHEN', 'WHERE', 'WHY', 'HOW', 'HOW MUCH']]

    for row in reader:
        print(row)
        categories = {
            'WHO': 0,
            'WHAT': 0,
            'WHEN': 0,
            'WHERE': 0,
            'WHY': 0,
            'HOW': 0,
            'HOW MUCH': 0
        }
        categories_bool = {
            'WHO': False,
            'WHAT': False,
            'WHEN': False,
            'WHERE': False,
            'WHY': False,
            'HOW': False,
            'HOW MUCH': False
        }
        classification, possible_classes = classify_text_with_completions(row)
        for possible_class in possible_classes:
            category = possible_class[0]
            category = category.upper()
            categories[category] = possible_class[1]
            categories_bool[category] = True if possible_class[1] > 0.14 else False

        print(categories)
        output.append([row, categories['WHO'], categories['WHAT'],
                       categories['WHEN'], categories['WHERE'],
                       categories['WHY'], categories['HOW'],
                       categories['HOW MUCH']])

        output2.append([row, categories_bool['WHO'], categories_bool['WHAT'],
                       categories_bool['WHEN'], categories_bool['WHERE'],
                       categories_bool['WHY'], categories_bool['HOW'],
                       categories_bool['HOW MUCH']])

        with open('results.csv', 'w', newline='', encoding='utf-8') as new_file:
            writer = csv.writer(new_file)
            writer.writerows(output)

        with open('results_bool.csv', 'w', newline='', encoding='utf-8') as new_file:
            writer = csv.writer(new_file)
            writer.writerows(output2)


