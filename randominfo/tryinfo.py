from os.path import abspath, join, dirname

full_path = lambda filename: abspath(join(dirname(__file__), filename))
print(full_path('first-names.csv'))