#add import
import question_c  

def main():
    global global_num 
    print("Before use_global, global_num =", question_c.global_num)  
    
    question_c.use_global()  
    
    
    print("After use_global, global_num =", question_c.global_num)  

main()  
question_c.test_use_global()
