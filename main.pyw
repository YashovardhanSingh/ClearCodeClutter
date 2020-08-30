import os

items = os.listdir()
files1 = [item for item in items if os.path.isfile(item)]
if 'code.py' in files1:
    files1.remove('code.py')

def createFolder(folderName):
    global items
    if folderName not in items:
        os.makedirs(folderName)
    
foldersToCreate = ['Javascript', 'Java', "Python", "C++", "C", "Dart", "Typescript", "Html", "Css", "Php", "Kotlin", "Golang", "Data", "Swift", "Csharp", "R", "Ruby", 'Executables']
for name in foldersToCreate:
    createFolder(name)

def moveFiles(folderName, files):
    for file in files:
        try:
            os.replace(file, f'{folderName}\\{file}')
        except:
            pass
    try:
        if len(files) == 0:
            os.rmdir(folderName)
    except:
        pass

pythonExt = ['.py', '.pyw', '.pyc', '.pyx', '.pyd', '.py3', '.pyo']
python = [file for file in files1 if os.path.splitext(file)[1].lower() in pythonExt]
moveFiles('Python', python)

javaExt = ['.java', '.class', '.dpj', '.jar', '.jsp', '.']
java = [file for file in files1 if os.path.splitext(file)[1].lower() in pythonExt]
moveFiles('Java', java)

jsExt = ['.js']
js = [file for file in files1 if os.path.splitext(file)[1].lower() in jsExt]
moveFiles('Javascript', js)

dartExt = ['.dart']
dart = [file for file in files1 if os.path.splitext(file)[1].lower() in dartExt]
moveFiles('Dart', dart)

tsExt = ['.ts']
ts = [file for file in files1 if os.path.splitext(file)[1].lower() in tsExt]
moveFiles('Typescript', ts)

dataExt = ['.json', '.db', ".txt", '.csv', '.pdf', '.dbs', '.dtf', '.sql', '.db2', '.db3']
data = [file for file in files1 if os.path.splitext(file)[1].lower() in dataExt]
moveFiles('Data', data)

cppExt = ['.cpp', '.cc', 'cxx', '.hpp', '.hxx', '.c++', '.h++']
cpp = [file for file in files1 if os.path.splitext(file)[1].lower() in cppExt]
moveFiles('C++', cpp)

cExt = ['.c', '.h', '.hdl']
c = [file for file in files1 if os.path.splitext(file)[1].lower() in cExt]
moveFiles('C', c)

htmlExt = ['.html', '.htm']
html = [file for file in files1 if os.path.splitext(file)[1].lower() in htmlExt]
moveFiles('Html', html)

cssExt = ['.css']
css = [file for file in files1 if os.path.splitext(file)[1].lower() in cssExt]
moveFiles('Css', css)

ktExt = ['.kt', '.kts', '.ktm']
kt = [file for file in files1 if os.path.splitext(file)[1].lower() in ktExt]
moveFiles('Kotlin', kt)

goExt = ['.go']
go = [file for file in files1 if os.path.splitext(file)[1].lower() in goExt]
moveFiles('Golang', go)

phpExt = ['.php', '.phtml', '.php3', '.php4', '.php5', '.php7', '.pht', '.phar']
php = [file for file in files1 if os.path.splitext(file)[1].lower() in phpExt]
moveFiles('Php', php)

swiftExt = ['.swift']
swift = [file for file in files1 if os.path.splitext(file)[1].lower() in swiftExt]
moveFiles('Swift', swift)

csExt = ['.cs']
cs = [file for file in files1 if os.path.splitext(file)[1].lower() in csExt]
moveFiles('Csharp', cs)

rubyExt = ['.rb']
ruby = [file for file in files1 if os.path.splitext(file)[1].lower() in rubyExt]
moveFiles('Ruby', ruby)

rExt = ['.r', 'rdata', '.rds', '.rda']
r = [file for file in files1 if os.path.splitext(file)[1].lower() in rExt]
moveFiles('R', r)

exeExt = ['.exe', '.bin', '.com', '.out', '.app', '.bat', '.osx']
exe = [file for file in files1 if os.path.splitext(file)[1].lower() in exeExt]
moveFiles('Executables', exe)

others = []
for file in files1:
    exts = pythonExt + javaExt + jsExt + tsExt + dartExt + ktExt + goExt + phpExt + cExt + cppExt + htmlExt + dataExt + cssExt + swiftExt + csExt + rubyExt + rExt + exeExt
    if os.path.splitext(file)[1].lower() not in exts:
        others.append(file)
        
moveFiles('Others', others)
