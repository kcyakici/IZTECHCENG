#lang scheme

(define (sum list1)
  (if (null? list1) 0
      (+ (car list1) (sum (cdr list1)))))

(sum (list 1 2 3 4 5 6 7)) ; Example call 1
(sum (list 1 3 5 7)) ; Example call 2