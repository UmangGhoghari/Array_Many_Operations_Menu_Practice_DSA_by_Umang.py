# Umang Ghoghari
# Main Instagram : @Umang.66
# Instagram 2 : @thelatenightcoder
# Linkedin URL : https://www.linkedin.com/in/umang-ghoghari-773144325/

print("----- ARRAY MANY OPERATION PROGRAM BY UMANG || @thelatenightcoder ----- ")

array = [1,2,4,7,34,7,623,765,86,74,5264,85,3]

while(1):
    print(" 1 > TRAVERSAL\n 2 > SUM OF ALL ELEMENT\n 3 > REVERSE ARRAY\n 4 > SEARCH ELEMENT\n 5 > INSERT ELEMENT\n 6 > FIND MIN ELEMENT\n 7 > FIND MAX ELEMENT\n 8 > EXTRACT ARRAY\n 9 > AVG FINDER 10 > EXIT")
    operation = int(input("Enter Operation Which you Want to Select"))

    if operation == 1:
        print("You Are Selected TRAVERSAL")
        for i in range(0,len(array)):
            print(f"Element Traversal Is > {array[i]}")

    if operation == 2:
        print("You Are Selected SUM")
        sum = 0
        for i in range(0,len(array)):
            sum = sum + array[i]
        print(sum)
    if operation == 3:
        print("You Are Selected Reverse array")
        for i in range(len(array)-1,-1,-1):
            print(array[i])
    if operation == 4:
        print("You Are Selected Search Element ")
        location = int(input("Enter Location you Want to Access Only That Element "))
        location = location - 1
        
        user_selected_array_is = array[location]
        print(user_selected_array_is)
    if operation == 5:
        element = int(input("Enter Element You Want TO Enter > "))
        index = int(input("Enter Index/Location > "))
        index = index - 1
        array.append(0)

        for i in range(len(array)-1 , index,-1):
            array[i] = array[i-1]
        array[index] = element
        print(f"So The Final Array After Insertion is\n {array}")
    if operation == 6:
        minelement = array[0]  
        print("You Are Selected MIN ELEMENT FINDER from ARRAY")
        for i in range(1,len(array)):
                
                if(array[i] < minelement):
                    minelement = array[i]
        print(minelement)

    if operation == 7:
        maxelement = array[0]  
        print("You Are Selected MAX ELEMENT FINDER from ARRAY")
        for i in range(1,len(array)):
                
                if(array[i] > maxelement):
                    maxelement = array[i]
        print(maxelement)
    
    if operation == 8:
        print("You Are Selected SUB ARRAY EXTRACTOR")
        subarray = []
        index_start_by_umang = int(input("Enter Start index > "))
        index_start_by_umang = index_start_by_umang - 1
        index_end_by_umang = int(input("Enter End index > "))
        

        for i in range(index_start_by_umang,index_end_by_umang):
            subarray.append(array[i])
        print(f" Your Extracted Sub Array is {subarray}")
    
    if operation == 9:
        print("You Are Selected ARRAY AVG FINDER")
        avg = sum / len(array)
        print(f"Your avg is {avg}")

    
            
            
    

    if operation == 10:
        break
        print("Thanks For using our App :)")

        

