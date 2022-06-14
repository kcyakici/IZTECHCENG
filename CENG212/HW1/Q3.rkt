#lang scheme

(define (square_of_list my_list)
 (map (lambda (number)
         (* number number))
       my_list))

(square_of_list (list 1 2 3 4 5 6)) ; Example call 1
(square_of_list (list 5 7 9 13 15)) ; Example call 2