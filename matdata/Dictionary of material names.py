#list of function names
#list of full name
#list of lists of what properties there are

#easy to update and if the index mactch up....

#creat a class for the material that with a name entered can pull up info


#----------------------------------------------------#
#Example with two materials

function_names = ('Inconel_718','AL_ALY_1100')
full name = ('Inconel (UNS N107718)','3003F Aluminum (UNS A93003)')
data_included = ((True,True),(True,False))

class Materials_Data(object):

    def __init__(self, material_name):

        self.material_name = material_name


    #line to check if the material name is included in list or close to something

    #check what data is included

    #pull functions ... is T known? or will it be known....

    #the problem is that there are materials with multiple different types. they need to be combined or another way has to be looked at.
        
