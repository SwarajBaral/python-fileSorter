import os
import shutil

FILE_DIRS = {
	'.py' 	: 'python',
	'.c' 	: 'C',
	'.java' : 'java',
	'.html' : 'HTML',
	'.cpp'	: 'C++',
	'.cs'	: 'C#',
	'.js'	: 'JavaScript',
}

def sort_files():
	'''
	Python File Sorter :-

	This script sorts the files in the directory and puts it in respective folder based on the file's extension.
	Add more extensions and their respective folders in the FILES_DIRS dictionary.

	Author		: Swaraj Baral
	Github-id	: SwarajBaral
	'''

	path = os.getcwd()
	files = os.listdir(path)

	for file in files:
		if file in ['file_sort.py','README.md']: 		# Exclude the current script and README of the repo
			continue
		else:
			fi,ex = os.path.splitext(file)
			if os.path.isfile(file):
				if not FILE_DIRS.get(ex, None):			# Move file to 'unlabeled' folder if FILE_DIRS[ex] doesn't exist 
					os.makedirs(path+'\\'+'unlabeled', exist_ok=True)
					shutil.move(path+'\\'+file, path+'\\'+'unlabeled'+'\\'+file)
				else:
					os.makedirs(path+'\\'+FILE_DIRS[ex], exist_ok=True)
					shutil.move(path+'\\'+file, path+'\\'+FILE_DIRS[ex]+'\\'+file)

if __name__ == '__main__':
	sort_files()