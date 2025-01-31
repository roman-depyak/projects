TITLE Generating, Sorting, and Counting Random integers 

; Author: 
; Last Modified: 5/28/24
; OSU email address: @oregonstate.edu
; Course number/section:   CS271 Section 400
; Project Number: 5                Due Date: 5/26/24
; Description: This program generates a specified number of random integers between two bounds.
; Then it displays an unsorted list of the generated numbers, sorts the list, displays the median value
; of the list, displays the sorted list in ascending order, and displays the number of occurrences 
; of each value in the list starting with the lowest value in the sorted list of generated numbers. 

INCLUDE Irvine32.inc   

ARRAYSIZE = 200        
LO = 15               
HI = 50               

.data
intro1          BYTE    "Generating, Sorting, and Counting Random integers! Programmed by me",13,10,0
intro2          BYTE    "This program generates 200 random integers between 15 and 50, inclusive.",13,10
                BYTE    "It then displays the original list, sorts the list, displays the median value of the list,",13,10
                BYTE    "displays the list sorted in ascending order, and finally displays the number of instances",13,10
                BYTE    "of each generated value, starting with the number of lowest.",13,10,0
space           BYTE    " ",0
unsortedNums    BYTE    "Your unsorted random numbers: ",13,10,0
sortedNums      BYTE    "Your sorted random numbers: ",13,10,0
printCounts     BYTE    "Your list of instances of each generated number, starting with the smallest value: ",13,10,0
printMedian     BYTE    "The median value of the array: ",0
goodbye         BYTE    "Goodbye, and thanks for using my program!",0
medianValue     DWORD   ?  
randArray       DWORD   ARRAYSIZE DUP(?) ; Reserve space for the random array
counts          DWORD   HI - LO + 1 DUP(0) ; Reserve space for the counts array

.code
main PROC

    ; Displays the introductory messages
    PUSH OFFSET intro1
    PUSH OFFSET intro2
    CALL introduction

    ; Sets up random number generator
    CALL Randomize

    ; Adds the randomly generated numbers into fillArray
    PUSH OFFSET randArray
    CALL fillArray

    ; Displays the unsorted array
    PUSH OFFSET space
    PUSH LENGTHOF randArray
    PUSH OFFSET unsortedNums
    PUSH OFFSET randArray
    CALL displayList

    ; Sorts the array
    PUSH OFFSET randArray
    CALL sortList

    ; Calculates median of the array
    PUSH OFFSET randArray
    PUSH OFFSET medianValue
    CALL calculateMedian

    ; Displays median of the array
    PUSH OFFSET printMedian
    PUSH OFFSET medianValue
    CALL displayMedian

    ; Displays the sorted array
    PUSH OFFSET space
    PUSH LENGTHOF randArray
    PUSH OFFSET sortedNums
    PUSH OFFSET randArray
    CALL displayList

    ; Counts the occurrences of each number in the array
    PUSH OFFSET randArray
    PUSH OFFSET counts
    CALL countList

    ; Displays the counts array
    PUSH OFFSET space
    PUSH LENGTHOF counts
    PUSH OFFSET printCounts
    PUSH OFFSET counts
    CALL displayList

    ; Displays the goodbye message
    PUSH OFFSET goodbye
    CALL farewell

    INVOKE ExitProcess,0    ; Exit the program
main ENDP

; ---------------------------------------------------------------------------------
; Name: introduction
;
; Procedure to introduce the program. Displays program title, author's name,
; and informs user of the purpose and function of the program. 
;
; Preconditions: intro1 is a string that contains the author's name and program title.
; intro2 is a string that contains a brief explanation of what the program does.
; of the program. 
;
; Postconditions: none
;
; Receives: intro1, intro2
;
; Returns: none
; ---------------------------------------------------------------------------------

introduction PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    EDX

    ; Display intro1
    MOV     EDX, [EBP + 12]
    CALL    WriteString         
    CALL    CrLf    
    
    ; Display intro2
    MOV     EDX, [EBP + 8]  
    CALL    WriteString         
    CALL    CrLf            

    POP     EDX
    POP     EBP

    RET 8
introduction ENDP

; ---------------------------------------------------------------------------------
; Name: fillArray
;
; Generetes ARRAYSIZE random integers in the range from LO to HI and stores
; these values in consecutive elements of array randArray.
;
; Preconditions: randArray is an array with ARRAYSIZE uninitialized elements,
; Randomize has been called, ARRAYSIZE, LO, and HI are constants and are integer
; literal expressions. 
;
; Postconditions: none
;
; Receives: randArray, ARRAYSIZE, LO, HI
;
; Returns: alters the elements of randArray
; ---------------------------------------------------------------------------------

fillArray PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    EBX
    PUSH    ESI
    PUSH    ECX
    PUSH    EAX

    ; Adds ARRAYSIZE randomly generated numbers into randArray
    MOV     ESI, [EBP + 8]      
    MOV     ECX, ARRAYSIZE      
_fillArray:
    MOV     EBX, HI             
    SUB     EBX, LO             
    INC     EBX                 
    MOV     EAX, EBX            
    CALL    RandomRange         
    ADD     EAX, LO             
    MOV     [ESI], EAX          
    ADD     ESI, TYPE DWORD     
    LOOP    _fillArray          

    POP     EAX
    POP     ECX
    POP     ESI
    POP     EBX
    POP     EBP

    RET 4
fillArray ENDP

; ---------------------------------------------------------------------------------
; Name: displayList
;
; Displays a string to output describing an array then displays the array such as 
; randArray or counts to output.
;
; Preconditions: space is the string " ", the LENGTHOF randArray and counts are declared,
; unsortedNums, printCounts, and sortedNums are strings that describe an array,
; randArray and counts are an array of numbers.
;
; Postconditions: none
;
; Receives: space, LENGTHOF randArray, unsortedNums, sortedNums, LENGTHOF counts, 
; printCounts, counts, randArray
;
; Returns: none
; ---------------------------------------------------------------------------------

displayList PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    EDX
    PUSH    ECX
    PUSH    ESI
    PUSH    EBX        

    ; prints the string explaining the list
    MOV     EDX, [EBP + 12]
    CALL    WriteString

    MOV     ESI, [EBP + 8]      ; Copies address of first element of randArray into ESI
    MOV     ECX, [EBP + 16] 
    MOV     EBX, 0              ; Count for elements per line

    ; prints the array 20 elements per line
_PrintArr:
    MOV     EAX, [ESI]          
    CALL    WriteDec            
    INC     EBX                 
    CMP     EBX, 20             
    JE      _newLine           
    MOV     EDX, [EBP + 20]  
    CALL    WriteString         
    JMP     _nextNum            

_newLine:
    CALL    CrLf                
    MOV     EBX, 0              

    
_nextNum:
    ADD     ESI, TYPE DWORD     
    LOOP    _PrintArr           

    CALL    CrLf                
    POP     EBX
    POP     ESI
    POP     ECX
    POP     EDX
    POP     EBP
    RET 13
displayList ENDP

; ---------------------------------------------------------------------------------
; Name: sortList
;
; Sorts randArray in ascending order using bubble sort. 
;
; Preconditions: randArray is an array with two or more number elements, ARRAYSIZE
; is a constant and integer literal, each element of randArray is a DWORD.
;
; Postconditions: none
;
; Receives: randArray, ARRAYSIZE
;
; Returns: alters randArray
; ---------------------------------------------------------------------------------

sortList PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    ESI
    PUSH    EDI
    PUSH    EAX
    PUSH    EDX
    PUSH    ECX
    PUSH    EBX

    MOV     ESI, [EBP + 8]      ; Copies randArray into ESI
    MOV     ECX, ARRAYSIZE      
    DEC     ECX                 

_outerLoop:
    MOV     EDI, ESI            ; EDI is first element of array
    ADD     EDI, TYPE DWORD     
    MOV     EBX, ECX            

_innerLoop:
    MOV     EAX, [EDI - TYPE DWORD] 
    CMP     EAX, [EDI]                  ; If value of element at pos n-1 <= value at pos n then don't swap
    JLE     _noSwap         

    ; Swaps elements
    PUSH    EDI
    PUSH    EAX
    CALL    exchangeElements   

_noSwap:
    ADD     EDI, TYPE DWORD     
    DEC     EBX                 
    JNZ     _innerLoop          

    DEC     ECX                 
    JNZ     _outerLoop        

    POP     EBX 
    POP     ECX
    POP     EDX
    POP     EAX
    POP     EDI
    POP     ESI
    POP     EBP
    RET 4
sortList ENDP

; ---------------------------------------------------------------------------------
; Name: exchangeElements
;
; Swaps the position of two consecutive elements in randArray.
;
; Preconditions: value of element at pos n-1 > value of element at pos n,
; element at pos n-1 is in EAX, element at pos n is in EDI, elements of randArray
; are DWORD
;
; Postconditions: none
;
; Receives: EDI, EAX
;
; Returns: EDI, EDX, EAX
; ---------------------------------------------------------------------------------

exchangeElements PROC
    PUSH    EBP
    MOV     EBP, ESP

    MOV     EDI, [EBP + 12]     
    MOV     EDX, [EDI]          
    MOV     EAX, [EBP + 8]      
    MOV     [EDI], EAX                  ; Swaps value at pos n-1 into pos n
    MOV     [EDI - TYPE DWORD], EDX     ; Swaps value at pos n into n-1 to complete exchange

    POP     EBP
    RET 8
exchangeElements ENDP

; ---------------------------------------------------------------------------------
; Name: calculateMedian 
;
; Calculates the median of sorted randArray. 
;
; Preconditions: randArray is an array sorted in ascending order with number elements,
; medianValue is an uninitialized DWORD.
;
; Postconditions: none
;
; Receives: randArray, medianValue, ARRAYSIZE 
;
; Returns: alters medianValue
; ---------------------------------------------------------------------------------

calculateMedian PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    EBX
    PUSH    EDX
    PUSH    ESI
    PUSH    ECX
    PUSH    EAX
    PUSH    EDI

    MOV     ESI, [EBP + 8]      
    MOV     ECX, ARRAYSIZE / 2  

    ; Check if the array size is even
    MOV     EAX, ARRAYSIZE
    AND     EAX, 1                          ; Check if the array size is odd or even
    JZ      _evenSize           

    ; Array size is odd
    MOV     EAX, [ESI + ECX * TYPE DWORD]   ; Copy median value
    JMP     _storeMedian

_evenSize:
    ; Array size is even
    DEC     ECX                 
    MOV     EBX, [ESI + ECX * TYPE DWORD]   ; Copy the lower middle element into EBX
    INC     ECX                 
    ADD     EBX, [ESI + ECX * TYPE DWORD]   ; Add upper middle element to lower
    ADD     EBX, 1              
    SHR     EBX, 1              
    MOV     EAX, EBX                        ; Copy average into EAX

_storeMedian:
    MOV    EDI, [EBP + 8]
    MOV    [EDI], EAX

    POP     EDI
    POP     EAX
    POP     ECX
    POP     ESI
    POP     EDX
    POP     EBX
    POP     EBP
    RET 8
calculateMedian ENDP

; ---------------------------------------------------------------------------------
; Name: displayMedian
;
; Displays the median of randArray to output.
;
; Preconditions: randArray is an array sorted in ascending order with number elements,
; medianValue DWORD that equals the value of the median of randArray.
;
; Postconditions: none
;
; Receives: randArray, medianValue
;
; Returns: none
; ---------------------------------------------------------------------------------

displayMedian PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    EAX
    PUSH    EDX

    MOV     EDX, [EBP + 12] 
    CALL    WriteString         

    MOV     ESI, [EBP + 8]
    MOV     EDX, [ESI]          ; Copy the median value into EAX
    
    MOV     EAX, EDX
     
    CALL    WriteDec            ; Display the median value
    CALL    CrLf               
    CALL    CrLF                

    POP     EDX
    POP     EAX
    POP     EBP
    RET
displayMedian ENDP

; ---------------------------------------------------------------------------------
; Name: countList
;
; Counts the occurrences of each number in the range [LO, HI] is seen in randArray. 
;
; Preconditions: randArray is an array with number elements which is sorted in
; ascending order. Counts is an array with HI - LO + 1 number of elements. 
;
; Postconditions: none
;
; Receives: randArray, counts, ARRAYSIZE, HI, LO
;
; Returns: alters counts
; ---------------------------------------------------------------------------------

countList PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    ESI
    PUSH    EDI
    PUSH    ECX
    PUSH    EBX
    PUSH    EAX

    
    MOV     EDI, [EBP + 8]      
    MOV     ECX, HI - LO + 1    
    XOR     EAX, EAX            

    ; Count occurrences of each number in randArray
    MOV     ESI, [EBP + 12]     
    MOV     ECX, ARRAYSIZE      

_countList:
    MOV     EAX, [ESI]                  ; Copy the current element of randArray into EAX
    SUB     EAX, LO                     ; Adjust the value to use as an index
    INC     DWORD PTR [EDI + EAX * 4]   ; Increment the corresponding element in the counts array
    ADD     ESI, TYPE DWORD     
    LOOP    _countList          

    POP     EAX
    POP     EBX
    POP     ECX
    POP     EDI
    POP     ESI
    POP     EBP
    RET 8
countList ENDP

; ---------------------------------------------------------------------------------
; Name: farewell
;
; Displays a parting message to the user.
;
; Preconditions: goodbye is a string that displays a parting message and
; thanks the user for using the program.
;
; Postconditions: none
;
; Receives: goodbye

;Receives is like the input of a procedure; it describes everything
; the procedure is given to work. Parameters, registers, and global variables
; the procedure takes as inputs should be described here.
;
; Returns: Returns is the output of the procedure. Because assembly procedures don�t
; return data like high-level languages, returns should describe all the data
; the procedure intended to change. Parameters and global variables that the
; procedure altered should be described here. Registers should only be mentioned
; if you are trying to pass data back in them.
; ---------------------------------------------------------------------------------

farewell PROC
    PUSH    EBP
    MOV     EBP, ESP
    PUSH    EDX

    CALL    CrLf               
    MOV     EDX, [EBP + 8]      
    CALL    WriteString      
    CALL    CrLf              

    POP     EDX
    POP     EBP
    RET
farewell ENDP

END main
