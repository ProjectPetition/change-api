class RemoveDuplicates:

    def remove_duplicates(self, in_file, out_file):

	i_file = open(in_file, 'r')
	o_file = open(out_file, 'w')

	lines = set()

	for line in i_file:

	    if (line not in lines):

		o_file.write(line)
		lines.add(line)

        i_file.close()
	o_file.close()


