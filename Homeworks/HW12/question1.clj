(def n (+ 1 (Integer/parseInt (first *command-line-args*)))) ;; get input
(defn func [x] (* x x)) ;; function to get the square of value x
(doseq [i (map func (range 1 n))] (println i)) ;; map values to the function and print
(println "Sum =" (reduce + (map func (range 1 n)))) ;; sum square values


