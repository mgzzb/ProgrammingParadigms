;;Create a namespace called “taxation” that includes a “tax” function.  The function takes two values: (1) the amount to be taxed and (2) the tax rate as a percent (e.g., 10 instead of 0.10) and computes the tax for a product. Use your new function together with println to report the tax that would be computed on an item that costs $117 with a 7% tax. Call your tax function from a different namespace called “application”. The program will output the tax for the product (which is 8.19).


(ns taxation) ;; namespace taxation
(defn tax [amount rate] (float (* amount (/ rate 100)))) ;;tax function

(ns application) ;; namespace application 
(println "The tax for the products is $" (taxation/tax 117 7)) ;; compute tax on item that costs $117 and has a 7% tax
