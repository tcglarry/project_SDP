import os

data_path = './dataset/ARY_ADJ/'

def make_ok_ng_dir(data_path):

    final_dir =[]
    final_dir_files ={}
    for i in range (9):

        chosen_path = (data_path+str(i))
        #chosen_path = ('/dataset/'+str(i)+'/')
        #print (chosen_path)

        for root, dirs, files in os.walk(chosen_path, topdown=True):
            if not dirs:
                final_dir.append(root)
                final_dir_files[root] = os.listdir(root)

    print(final_dir)

    # check files that are not images, if yes, erase them
    for key in final_dir_files.keys():

        print (key, '\t', len(final_dir_files[key]))
        not_jpg = [f for f in final_dir_files[key] if f[-4:] !='.jpg']
        final_dir_files[key] = [f for f in final_dir_files[key] if f not in not_jpg]
    ok_dir = [f for f in final_dir if 'OK' in f ]
    print (ok_dir)
    ng_dir = [f for f in final_dir if f not in ok_dir]
    print (ng_dir)

    # making prefix, example: 0_NG_, 1_ok,..
    ng_prefix = {}
    for f in ng_dir:
        ng_prefix[f] = f[18:19] + '_NG_'
    print ('\n')
    print(ng_prefix)

    ok_prefix = {}
    for f in ok_dir:
        ok_prefix[f] = f[18:19] + '_OK_'
    print ('\n')
    print (ok_prefix)

    return ok_dir, ok_prefix, ng_dir,ng_prefix
