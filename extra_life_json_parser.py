import json

#Load the json file
filename = 'json_donation_file.txt'
i = 0
flag100_set = 0
with open(filename,'r') as f:
    all_data = json.load(f)
    while i < len(all_data):
        data = all_data[i]
        #Parse into useful stuff
        #loop through each
        try:
            output_string = 'Donation ' + str(data['amount']) + ' by ' + str(data['displayName']) + ': '
            if str(data['message']) != "None":
                output_string += str(data['message'])
            if data['amount'] >= 100.0 and flag100_set:
                print(output_string + '\n')
            elif not flag100_set:
                print(output_string + '\n')

        except ValueError as err:
            print("Error parsing String! Sorry I'm lazy\n")
            #print(err)
            #print('\n')
        try:
            useless = input("Press Enter for next 100$+ donation\n")
        except SyntaxError:
            pass
        i+= 1
