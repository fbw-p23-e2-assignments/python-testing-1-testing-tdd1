# Test Driven Development at the Zoo

In this exercise, we'll be looking at the basic test driven development (TDD) in a zoo setting.

You are working at a major zoo that is maintaining its own software system for to control the
animals' cages and feeding machines.

The zoo is about to receive a new type of giant cat. A software class needs to be written to control its
meat and water dispensers and to lock its cage at night.

Your colleague Jill met up with the zoo director and received a list of exact requirements. She then
went ahead and assembled the file `src/test.py` which is supposed to test whether the class `CatController` works as
it is supposed to do or not. It is now your job to complete the programming by creating the class
`CatController` in the file `src/cat_controller.py`. Running the file `src/test.py` needs to return
the line "All tests ran successfully.".

**Note:** The `CatController` class only needs to return the correct status message about what it supposedly
did. You are not expected to write code that actually controls secured cage doors or feeding machines.
