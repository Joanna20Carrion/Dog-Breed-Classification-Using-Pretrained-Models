#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: JOANNA ALEXANDRA CARRION PEREZ
# DATE CREATED: 15.01.2025                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from fileinput import filename

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    f_list = listdir(image_dir)
     
    print('\nThe ten filenames in pet_images folder are:')
    
    dog_labels = []     
    r_dic = dict()

    for ix in range(0, len(f_list), 1):
        if f_list[ix][0] != ".":
            dog_labels = ''
            p_i_f = f_list[ix]
            word_list_p_i_f = p_i_f.lower().split('_')
            dog_name = ''
            for w in word_list_p_i_f:
                if w.isalpha():
                    dog_name += w + " "
            dog_name = dog_name.strip()
            print('Filename = ', p_i_f, '    Label = ', dog_name)        
            print('\n{:2d} file: {:>25}'.format(ix + 1, f_list[ix]))
   
            # If filename doesn't exist in dictionary add it and it's pet label
            n0_items = len(r_dic)
            print('\nThe empty dictionary has {} items in total'.format(n0_items))
    
            if f_list[ix] not in r_dic:
                r_dic[f_list[ix]] = [dog_name]
            else:
                print('\nWARNING!!!: key =' , filename[ix],  'already exists in r_dic with value =', r_dic[filename[ix]])
    print('\nAll key-value pairs in r_dic:')
    for key in r_dic:
          print('\nFilename = ', key, '    Dog label = ', r_dic[key][0])
            
    n_full_d = len(r_dic)
    print('\nThe empty dictionary has {} items in total'.format(n_full_d))
    
    return r_dic 