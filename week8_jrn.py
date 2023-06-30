def handle_files():
     """This function reads an input text file and calls the inverted_dict1 function to invert the keys and 
     values then outputs the inverted dictionary to a new file """
     dict1 = {}
     #This part reads the file
     with open("input.txt", "r") as file_inp:
          for line in file_inp:
               (key, val) = line.split()
               dict1[key] = val
     #This calls the inverted dictionary function and creates an inverted dictionary
     dict2 = invert_dict1(dict1)
     #This outputs the new dictionary into a new output file
     with open("output.txt", "w") as file_out:
          for keys, values in dict2.items():
               file_out.writelines('{0} {1} \n'.format(keys, values))

     print("Inversion complete")


def invert_dict1(d):
     """This is the function to invert the dictionary"""
     inverse = dict()
     for key in d:
          val = d[key]
          if val not in inverse:
               inverse[val] = [key]
          else:
               inverse[val].append(key)

    #This is the part I added 
     for key, val in inverse.items():
          for i in val:
               inverse.update({key:i})
     return inverse


handle_files()
