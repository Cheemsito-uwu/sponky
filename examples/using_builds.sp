build Dog(this)
    def(1, this, "name", "Mr. Dogge")
    def(2, this, "age", 9)
    def(3, this, "favorite food", "chicken")
    def(4, this, "color", "a brown dog")

    return this
end

print("This is a dog!")

print("Favorite food: " + get(Dog("favorite food")))
var age = get(Dog("age"))
var color = get(Dog("color"))
var name = get(Dog("name"))

print("Name: " + name)
print("Age: " + age + " years")