import hashlib
import csv
from collections import OrderedDict


def hash_password_hack(input_file_name, output_file_name):
    with open(output_file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        hash_dic=OrderedDict()
        final_dic=OrderedDict()
        with open(input_file_name, newline='') as f:
            reader = csv.reader(f)
            for hads in range(0000,9999):
                hads_code=hashlib.sha256(str(hads).encode('utf-8')).hexdigest()
                hash_dic[hads_code]=hads
            for row in reader:
                name=row[0]
                hash_password=row[1]
                final=hash_dic.get(str(hash_password))
                final_dic[name]=final
                final_dic.update(final_dic)
            final_dic=list(final_dic.items())
            for row in final_dic:
                writer.writerow(row)    



                 
