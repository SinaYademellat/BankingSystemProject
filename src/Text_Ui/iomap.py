
# ===========================================================

def message_box(messag_text:str,size_x:int):
        

        row_start_and_end_ = '+' + ( (size_x-2) * '-' ) + '+'
        len_input = len(messag_text)

        size_x-=2
        start_index = (size_x//2) - (len_input//2) 

        if(len_input%2==0):
            new_row = '|'+ ( start_index * ' ' ) + messag_text + ( (   (size_x//2) - (len_input//2) )     * ' ') + '|' 
        else:
            new_row = '|'+ ( start_index * ' ' ) + messag_text + ( ( ( (size_x//2) - (len_input//2) ) -1) * ' ') + '|' 


        print(
                row_start_and_end_,
                new_row,
                row_start_and_end_,

                sep='\n'
          ) 

def item_box(item_text:str,size_x:int):
    
    row_start_and_end_ = '+' + ( size_x * '-' ) + '+'
    len_input = len(item_text)

    size_x-=2
    my_EndL            = '|' + ( size_x * ' ' ) + '|'
    start_index = (size_x//2) - (len_input//2) 

    if(len_input%2==0):
        new_row = '|'+ ( start_index * ' ' ) + item_text + ( (   (size_x//2) - (len_input//2) )     * ' ') + '|' 
    else:
        new_row = '|'+ ( start_index * ' ' ) + item_text + ( ( ( (size_x//2) - (len_input//2) ) -1) * ' ') + '|' 

    print(  
            my_EndL,
            new_row, 

            sep='\n'
          )

def input_box(size_x:int)->str:
    
    size_x-=2

    row_start_and_end_ = '+' + ( size_x * '-' ) + '+'
    print(row_start_and_end_)

    panding_ = ( (size_x//2) * ' ' )+ '> '
    result_is = input(panding_)

    return(result_is)


#  =========================================================================

def how_are_you_(display_size:int)->int:
    """
        input: 
                display size
        output: 
                1 --> Admin

                2 --> Customer
    """

    # step(1)
    message_box('Choose a number',display_size)
    item_box('(1) Admin   ',display_size)
    item_box('(2) Customer',display_size)
   

    while True:
        
        tmp_input = input_box(display_size)
        
        if (tmp_input in ['1', '2'] ):
                 return int(tmp_input) 
        else:
            print('please try again  << 1 or 2 >> ')


def admin_TUI(display_size:int)->int:
        
        message_box('Admin panel',display_size)
        item_box('(0) information',display_size)
        item_box('(1) Change password',display_size)
        item_box('(2) Insert into Bank',display_size)
        item_box('(3) Insert into Branch',display_size)
        item_box('(4) Branch  budget',display_size)
        item_box('(5) Check requests',display_size)
        item_box('(6) Monitoring',display_size)



        while True:
            tmp_input = input_box(display_size)
            if (tmp_input in ['0','1', '2', '3', '4', '5','6'] ):
                 return int(tmp_input) 
            else:
                print('please try again  << 0 - 6 >> ')
