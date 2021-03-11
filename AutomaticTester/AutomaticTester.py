
SUCCESS_MESSAGE = "\n ***************** All right:) You are genius! *****************\n"
ERROR_MESSAGE = "ERROR:\nCheck if this folder contains the files: expected_output.txt, your_output.txt, and try again."

DIVIDER_LINE = "------------------------------------------------------------------"



user_input = "y"

while user_input in {"y", "Y", "yes", "Yes", "V", "v"}:
    
    print(DIVIDER_LINE)
    
    try:
        your_output = open("your_output.txt")
        expected_output = open("expected_output.txt")
        
        flag = True
        line_num = 1
        
        for your_line in your_output:
            expected_line = expected_output.readline()
            
            your_line = your_line.strip().strip('\n')
            expected_line = expected_line.strip().strip('\n')
            
            if your_line != expected_line:
                
                # Print different lines
                print("oops... (line {}):".format(line_num))
                print("Expected:", expected_line)
                print("Yours:   ", your_line)
                
                # Print arrows
                arrows = "".join([" " if your_line[i] == expected_line[i] else "^" for i in range(min(len(your_line), len(expected_line)))])
                arrows += "^" * (abs(len(your_line) - len(expected_line)))
                
                print("         ", arrows)
                
                flag = False
            
            line_num += 1
            
        if flag:
            print(SUCCESS_MESSAGE)
        
        your_output.close()
        expected_output.close()
    
    except:
        print(ERROR_MESSAGE)
    
    print(DIVIDER_LINE)

    user_input = input("Try again? y/n : ")
