(format t "Enter the size of the list : ")
(defvar m (read))

(defvar l '())

(format t "Enter the elements of the list : ~%")
(loop for x from 1 to m
      do (push (read) l)
)

(setq l (reverse l))

(format t "Entered List : ~a ~%" l)

(format t "Enter position of element in the list : ")
(defvar n (read))

(loop for x from 1 to (- n 1)
      do (setq l (cdr l))
)

(format t "The ~a element of list : ~a" n (car l))