# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string should be a prefix
# The function appends every verb to the prefix and returns the list of the new verbs

def create_new_verbs(preverb, verbs):
    for i in verbs:
        i = preverb + i
        print(i, end='\n')


my_verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
my_preverb = "be"

print(create_new_verbs(my_preverb, my_verbs))
# The output should be: "bemegy", "bever", "bekapcsol", "berak", "benéz"
