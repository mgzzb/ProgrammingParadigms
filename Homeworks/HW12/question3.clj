;; Read the temperatures from the file temperatures.txt, which contains a list of temperatures in Fahrenheit.  Implement a Clojure program that prints the minimum, maximum, and average temperatures in Celsius (rather than Fahrenheit).
;; Conversion formula: °C = (°F − 32) × 5/9

(require '[clojure.string :as str])

(def file (str/split (slurp "temperatures.txt") #"\n"))
(def temps (map read-string file))
(defn cel [x] (* (- x 32) (/ 5 9)))
(def celsius (map cel temps))
(defn avg [x] (double (/ (reduce + x)  (count x))))
(println "Minimum temperature: " (apply min celsius) "°C")
(println "Maximum temperature: " (apply max celsius) "°C")
(println "Average temperature: " (avg celsius) "°C")