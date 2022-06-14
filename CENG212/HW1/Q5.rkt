#lang scheme

(define (exponential_of_list exponential my_list)
  (map (lambda (number)
         (exponential number))
       my_list))

(define (cube number)
  (* (square number) number))

(define (square number)
  (* number number))

(exponential_of_list square (list 1 2 3 4 5)) ; Example call with square
(exponential_of_list cube (list 1 2 3 4 5)) ; Example call with cube