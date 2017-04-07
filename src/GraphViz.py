'''
Created: 07/04/2017
'''

import pydotplus,os

graph_data = 'graph A { a->b };\ngraph B {c->d}'

dot_file='tree.dot'
f = open(dot_file, 'rt')
graph_data = f.read()
f.close()
graph = pydotplus.graph_from_dot_data(graph_data)

fileUrl="iris.pdf"
graph.write_pdf(fileUrl)
os.startfile(fileUrl)