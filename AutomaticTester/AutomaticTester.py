"""
GOOD LUCK!
"""
user_input = "y"
while user_input in {"y", "Y", "yes", "Yes", "V", "v"}:
    print("------------------------------------------------------------------")
    try:
        your_output = open("your_output.txt")
        expected_output = open("expected_output.txt")
        
        flag = True
        line_num = 1
        for line1 in your_output:
            line2 = expected_output.readline()
            line1 = line1.strip().strip('\n')
            line2 = line2.strip().strip('\n')
            if line1 != line2:
                
                # Print different lines
                print("oops... (line {}):".format(line_num))
                print("Expected:", line2)
                print("Yours:   ", line1)
                
                # Print arrows
                arrows = "".join([" " if line1[i] == line2[i] else "^" for i in range(min(len(line1), len(line2)))])
                arrows += "^" * (abs(len(line1) - len(line2)))
                print("         ", arrows)
                
                flag = False
            
            line_num += 1
            
        if flag:
            print("\n ***************** All right:) You are genius! *****************\n")
        
        your_output.close()
        expected_output.close()
    
    except:
        print("ERROR!")
        print("Check if this folder contains the files: expected_output.txt, your_output.txt, and try again.")

    print("------------------------------------------------------------------")

    user_input = input("Try again? y/n : ")
