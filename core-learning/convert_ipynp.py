import os,json

cells=[]
files={}
def addMDCell(source):
    global cells
    cell={}
    cell['cell_type']="markdown"
    cell['metadata']={}
    cell['source']="### "+source
    cells.append(cell)


def addCodeCell(source):
    global cells
    cell={}
    cell['cell_type']="code"
    cell['metadata']={}
    cell['outputs']=[]
    cell['execution_count']=None
    cell['source']=source
    cells.append(cell)

    
for f in sorted(os.listdir(os.getcwd())):
    if f[-2:]=='py':
        title=f.upper()[:-3].replace('_',' ')
        addMDCell(title)
   
        files=[]
        with open("./"+f, 'r') as fp:
            while True:
                line = fp.readline()
                
                files.append(line)
                if not line:
                    break

        
        addCodeCell(files)

jupyter_notebook = {}
jupyter_notebook['cells'] = cells

jupyter_notebook['metadata']={"language_info": {
      "name": "python"
    }}

jupyter_notebook['nbformat']=4
jupyter_notebook['nbformat_minor']=2

with (open('0-Demo.ipynb', 'w')) as fp:
    json.dump(jupyter_notebook, fp)