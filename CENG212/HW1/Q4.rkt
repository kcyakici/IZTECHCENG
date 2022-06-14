#lang scheme

(define (cube_of_list my_list)
 (map (lambda (number)
         (* (* number number) number))
       my_list))

(cube_of_list (list 1 2 3 4 5 6)) ; Example call 1
(cube_of_list (list 5 7 9 13 15)) ; Example call 2