import glob,os

class ConcatFiles:
    
    def concat_files(self, file_ext, path_to_file_in, file_out):

	if (file_ext == 'sig'):

	    ext_tmp = '*.sigtmp'
	    ext = '.sig'

	elif (file_ext == 'reasons'):

	    ext_tmp = '*.reasonstmp'
	    ext = '.reasons'

	files = glob.glob(path_to_file_in + '*' + ext)

	output_file = open(file_out.strip('reasons') + ext + '.cat', 'wb')

	if (file_ext == 'sig'):
	    
	    output_file.write('Page,Total Pages,Signature Count,Signatures\n,,,Name,City,State/Province,Country Code,Country Name,Signed At\n')

	elif (file_ext == 'reasons'):

	    output_file.write('Page,Total Pages,Reasons\n,,Created At,Content,Like Count,Author Name,Author URL\n')

	for line in files:

	    input_files = open(line, 'r')

	    output_file.write(input_files.read())
	    output_file.write('\n')
	    input_files.close()

	for file_name in glob.glob(path_to_file_in + '/' + ext_tmp):
	
	    os.remove(file_name)

	output_file.close()

