# Object of products and their information for the bakery
Menu = [
    {name: 'Chocolate Chip Cookie', size: 1, price: 4}
    {name: 'Sugar Cookie', size: 1, price: 3}
    {name: 'Brownie Fudge', size: 2, price: 5}
    {name: 'Chocolate Cake', size: 7, price: 21}
    {name: 'Vanilla Cake', size: 7, price: 22}]


name_products = (x.name for x in Menu)
console.log name_products # print all product names

size_1 = (x.name for x in Menu when x.size == 1)
console.log size_1 # Print products that are for a single person

size_big = (x.name for x in Menu when x.size > 1)
console.log size_big # Print products that are for a group of people 