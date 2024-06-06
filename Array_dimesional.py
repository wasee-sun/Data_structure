
#* Arrays

lst_1D = ["A", "B", "C", "D", "E"]
#*Indexing 0    1    2    3    4


# 2 dimensional square  list

lst_2D = [  
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]


# #3 dimensional square list

lst_3D = [
    [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

if __name__ == '__main__':
    #Accessing 1D list
    print(lst_1D[0]) # Accessing the first element
    
    #Accessing 2D list
    print(lst_2D[0][0]) # Accessing the first element of the first row
    #we access row first then column
    
    #Accessing 3D list
    print(lst_3D[0][0][0]) # Accessing the first element of the first row of the first column
    #we access row first then column then depth