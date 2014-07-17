import getSignatures
import getReasons
import getPetText
import os
from datetime import date

class CollectPetSig:

    def collect_pet_and_sig(self, path_to_file_out, recent_file, page_size):

	titles = open(recent_file, 'r')
	gs = getSignatures.GetSignatures()
	gr = getReasons.GetReasons()
        gpt = getPetText.GetPetText()

	if not os.path.exists(path_to_file_out + '/' + str(date.today())) and path_to_file_out != '':
	    
	    os.makedirs(path_to_file_out + '/' + str(date.today()))

	for line in titles:

	    wo_newline = line.strip()

	    gpt.get_petition_text(wo_newline, path_to_file_out + '/' + str(date.today()) + '/' + line)
	    
	    if (page_size == 1):

		gs.get_all_signatures('', '', wo_newline, page_size)

	    else:
		
		gs.get_all_signatures(str(date.today()), path_to_file_out, wo_newline, page_size)

        titles.close()

	gr.get_all_reasons(path_to_file_out, recent_file)
